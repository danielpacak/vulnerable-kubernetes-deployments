import logging
import os
import subprocess

from flask import Flask, render_template, redirect, url_for
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


@app.route("/fibonacci/<number>", methods=["GET"])
def fibonacci_route(number):
    return f"<p>Fibonacci number: {fibonacci(int(number))}</p>"


@app.route("/hello_template/")
@app.route("/hello_template/<name>")
def hello_template(name=None):
    return render_template("hello.html", person=name)


@app.route("/linux/process/id")
def linux_process_id():
    completed_process = subprocess.run(["id"], capture_output=True)
    return {
        "return_code": completed_process.returncode,
        "stdout": str(completed_process.stdout),
        "stderr": str(completed_process.stderr),
    }


@app.route("/python/eval")
def python_eval():
    x = eval("__import__('subprocess').getoutput('uname -a')")
    return {"result": str(x)}


@app.route("/health")
def health_check():
    logger.debug("Handling /health request")
    return "OK", 200


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

if __name__ == "__main__":
    app.run()
