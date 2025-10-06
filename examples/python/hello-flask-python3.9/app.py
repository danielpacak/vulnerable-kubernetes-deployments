import logging
import os
import platform
import subprocess
import sys
from kubernetes import client, config

import pyroscope
from flask import Flask, render_template, redirect, url_for
import flask
from markupsafe import escape

from fibonacci import fibonacci
from prime_numbers import is_prime
from login import do_the_login, show_the_login_form
from service import my_service_function
from flask import request

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

MEMORY_BYTES = 512
DYNAMIC_RULES_COUNT = 10

app = Flask(__name__)


@app.route("/")
def index():
    return redirect(url_for("hello"))


@app.route("/hello", methods=["GET", "POST"])
def hello():
    app.logger.debug("Handling /hello request")
    return "<p>" + my_service_function() + "</p>"


@app.route("/user/<username>")
def show_user_profile(username):
    # show the user profile for that user
    return f"User {escape(username)}"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return do_the_login()
    else:
        return show_the_login_form()


@app.route("/is_prime/<number>", methods=["GET"])
def is_prime_route(number):
    return f"<p>Is {number} prime number? {is_prime(int(number))}</p>"


@app.route("/fibonacci/recursive/<number>", methods=["GET"])
def fibonacci_recursive_handler(number):
    return {"fibonacci": fibonacci(int(number))}


@app.route("/hello_template/")
@app.route("/hello_template/<name>")
def hello_template(name=None):
    return render_template("hello.html", person=name)


@app.route("/linux/subprocess/run/id")
def linux_subprocess_run_id_handler():
    completed_process = subprocess.run(["id"], capture_output=True)
    return {
        "return_code": completed_process.returncode,
        "stdout": str(completed_process.stdout),
        "stderr": str(completed_process.stderr),
    }


# clone3 -> execve
@app.route("/python/eval/subprocess/run/id")
def python_eval_subprocess_run_id_handler():
    completed_process: subprocess.CompletedProcess = eval(
        "__import__('subprocess').run(['id'], capture_output=True)"
    )
    return {
        "return_code": completed_process.returncode,
        "stdout": str(completed_process.stdout),
        "stderr": str(completed_process.stderr),
    }


# vfork -> execve
@app.get("/python/eval/os/system/id")
def python_eval_os_system_id_handler():
    out = eval("__import__('os').system('id')")
    return {"stdout": out}


@app.route("/python/eval")
def python_eval_handler():
    output = eval("__import__('subprocess').getoutput('uname -a')")
    return {"result": str(output)}


@app.route("/health")
def health_handler():
    logger.debug("Handling /health request")
    return "OK", 200


@app.route("/system/info")
def system_info_handler():
    return {
        "system": {
            "pid": os.getpid(),
            "ppid": os.getppid(),
            "sys_version_info": sys.version_info,
            "platform_python_version": platform.python_version(),
            "flask_version": flask.__version__,
        }
    }


@app.route("/kubernetes/serviceaccount/token")
def kubernetes_serviceaccount_token_handler():
    """
    Return the content of the /var/run/secrets/kubernetes.io/serviceaccount/token
    For testing if we can do more than necessary with this service account
    """
    try:
        with open("/var/run/secrets/kubernetes.io/serviceaccount/token") as f:
            return f.read()
    except FileNotFoundError:
        flask.abort(404, "Service account token not found")


@app.route("/kubernetes/serviceaccount/token/json")
def kubernetes_serviceaccount_token_json_handler():
    # TODO Parse the token and return JSON
    pass


@app.route("/kubernetes/eks/serviceaccount/token")
def kubernetes_eks_serviceaccount_token_handler():
    try:
        with open("/var/run/secrets/eks.amazonaws.com/serviceaccount/token") as f:
            return f.read()
    except FileNotFoundError:
        flask.abort(404, "Amazon EKS service account token not found")


@app.route("/kubernetes/serviceaccount/deployment/create")
def kubernetes_serviceaccount_deployment_create_handler():
    """Use KSA to create pod in kube-system namespace that has privileges
    and exfiltrates some data from the host, e.g. /etc/passwd or other
    metadata"""
    DEPLOYMENT_NAME = "kube-ingress-controller"
    DEPLOYMENT_NAMESPACE = "kube-system"
    # config.load_kube_config()
    config.load_incluster_config()
    apps_v1 = client.AppsV1Api()

    # Configure Pod template container
    container = client.V1Container(
        name="nginx",
        image="nginx:1.15.4",
        ports=[client.V1ContainerPort(container_port=80)],
        resources=client.V1ResourceRequirements(
            requests={"cpu": "100m", "memory": "200Mi"},
            limits={"cpu": "500m", "memory": "500Mi"},
        ),
        security_context=client.V1SecurityContext(
            privileged=True,
        ),
    )

    # Create and configure a spec section
    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"app": "nginx"}),
        spec=client.V1PodSpec(containers=[container]),
    )

    # Create the specification of deployment
    spec = client.V1DeploymentSpec(
        replicas=1, template=template, selector={"matchLabels": {"app": "nginx"}}
    )

    # Instantiate the deployment object
    deployment = client.V1Deployment(
        api_version="apps/v1",
        kind="Deployment",
        metadata=client.V1ObjectMeta(name=DEPLOYMENT_NAME),
        spec=spec,
    )

    resp = apps_v1.create_namespaced_deployment(
        body=deployment, namespace=DEPLOYMENT_NAMESPACE
    )

    return {
        "namespace": resp.metadata.namespace,
        "name": resp.metadata.name,
        "generation": resp.metadata.generation,
        "image": resp.spec.template.spec.containers[0].image,
    }


@app.route("/kubernetes/serviceaccount/pod/list")
def kubernetes_serviceaccount_pod_list_handler():
    # Configs can be set in Configuration class directly or using helper utility
    # config.load_kube_config()
    config.load_incluster_config()

    v1 = client.CoreV1Api()
    app.logger.debug("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)

    pods = []
    for i in ret.items:
        pods.append(
            {
                "name": i.metadata.namespace,
                "namespace": i.metadata.name,
                "ip": i.status.pod_ip,
            }
        )

    return pods


# Simulate that we do allocate quite some memory. We can make it more
# complex and allocate more object in different memory pages.
memory_bytes = int(os.environ.get("HELLO_FLASK_MEMORY_BYTES", MEMORY_BYTES))
logger.debug("Allocating {bytes} of memory".format(bytes=memory_bytes))
memory = bytearray(memory_bytes)


def dynamic_view_func_generator(x):
    def dynamic_view_func():
        return "<p>Dynamic view response <b>{x}</b> <b>{y}</b></p>".format(
            x=x, y=len(memory)
        )

    dynamic_view_func.__name__ = "dynamic_view_func_{x}".format(x=x)
    return dynamic_view_func


def add_dynamic_rules():
    dynamic_rules_count = int(
        os.environ.get("HELLO_FLASK_DYNAMIC_RULES_COUNT", DYNAMIC_RULES_COUNT)
    )
    logger.debug("Adding {count} dynamic rules".format(count=dynamic_rules_count))
    for x in range(dynamic_rules_count):
        rule = "/dynamic_rule_{x}".format(x=x)
        logger.debug("Adding dynamic rule {x}".format(x=rule))
        app.add_url_rule(rule=rule, view_func=dynamic_view_func_generator(x))


add_dynamic_rules()

# Configure Grafana PyroscopeSDK
# docker run --rm -d --name pyroscope -p 4040:4040 grafana/pyroscope
pyroscope_application_name = (
    os.getenv("PYROSCOPE_APPLICATION_NAME") or "hello-flask-python3.9"
)
pyroscope_server_address = (
    os.getenv("PYROSCOPE_SERVER_ADDRESS") or "http://localhost:4040"
)

pyroscope.configure(
    application_name=pyroscope_application_name,
    server_address=pyroscope_server_address,
    sample_rate=100,
    detect_subprocesses=True,
    enable_logging=True,
)

if __name__ == "__main__":
    app.run()
