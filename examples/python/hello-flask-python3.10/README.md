# python-hello-flask

## Development

1. Create a virtual environment:
   ```
   uv venv
   ```
2. Activate the virtual environment:
   ```
   source .venv/bin/activate
   ```
3. Update the project's environment:
   ```
   uv sync --frozen
   ```
4. Run Flask app:
   ```
   flask run --host=0.0.0.0 --port=5050
   # or
   HELLO_FLASK_MEMORY_BYTES=512 HELLO_FLASK_DYNAMIC_RULES_COUNT=10 flask run --host=0.0.0.0 --port=5050
   ```

> [!NOTE]
> Show all registered routes with endpoints and methods:
> ``` console
> $ flask routes
> Endpoint           Methods    Rule
> -----------------  ---------  -----------------------
> hello              GET, POST  /hello
> index              GET        /
> show_user_profile  GET        /user/<username>
> static             GET        /static/<path:filename>
> ```

## Deployment

### Docker

> [!NOTE]
> Authenticate to GitHub Container Registry (gcr.io):
> ```
> echo "$GH_PAT" | docker login ghcr.io -u "$GH_USER" --password-stdin
> ```


```
docker buildx build --load -t python-hello-flask -f Dockerfile .
```

```
docker run -it -p 5050:5050 python-hello-flask
```

Open http://localhost:5050 in your web browser.

```
docker run --rm --entrypoint="" python-hello-flask flask --app /app/app.py routes
```

### Kubernetes

1. Load docker image from a local host into cluster nodes:
   1. Kind
      ```
      kind load docker-image python-hello-flask:latest
      ```
   2. Cluster created with kubeadm:
      ```
      docker image save -o /tmp/python-hello-flask.tar python-hello-flask:latest
      sudo ctr -n k8s.io image import /tmp/python-hello-flask.tar && rm /tmp/python-hello-flask.tar
      ```
2. Create Kubernetes deployment:
   ```
   kubectl apply -f deploy/kubernetes/all.yaml
   ```
3. Forward local port 5050 to a pod:
   ```
   kubectl port-forward -n python-hello-flask svc/python-hello-flask 5050:5050
   ```

## Further Reading

* https://flask.palletsprojects.com/en/stable/quickstart/
* https://realpython.com/python-uv/
* https://github.com/astral-sh/uv-docker-example
* https://docs.astral.sh/uv/guides/integration/docker/
* https://docs.astral.sh/ruff/installation/

## Stack Trace

compare stack trace run in a containe and outside container

```
------------------- New Sample --------------------
  thread.name: python3
  process.executable.name: python3.10
  process.executable.path: /usr/bin/python3.10
  process.pid: 144899
  thread.id: 145883
---------------------------------------------------
Instrumentation: cpython, Function: fibonacci, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-hello-flask/fibonacci.py, Line: 2, Column: 0
Instrumentation: cpython, Function: fibonacci, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-hello-flask/fibonacci.py, Line: 2, Column: 0
Instrumentation: cpython, Function: fibonacci, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-hello-flask/fibonacci.py, Line: 2, Column: 0
Instrumentation: cpython, Function: fibonacci, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-hello-flask/fibonacci.py, Line: 2, Column: 0
Instrumentation: cpython, Function: fibonacci, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-hello-flask/fibonacci.py, Line: 2, Column: 0
Instrumentation: cpython, Function: fibonacci, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-hello-flask/fibonacci.py, Line: 2, Column: 0
Instrumentation: cpython, Function: fibonacci, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-hello-flask/fibonacci.py, Line: 2, Column: 0
Instrumentation: cpython, Function: fibonacci, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-hello-flask/fibonacci.py, Line: 2, Column: 0
Instrumentation: cpython, Function: fibonacci, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-hello-flask/fibonacci.py, Line: 2, Column: 0
Instrumentation: cpython, Function: fibonacci, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-hello-flask/fibonacci.py, Line: 2, Column: 0
Instrumentation: cpython, Function: fibonacci, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-hello-flask/fibonacci.py, Line: 2, Column: 0
Instrumentation: cpython, Function: fibonacci, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-hello-flask/fibonacci.py, Line: 2, Column: 0
Instrumentation: cpython, Function: fibonacci, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-hello-flask/fibonacci.py, Line: 2, Column: 0
Instrumentation: cpython, Function: fibonacci, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-hello-flask/fibonacci.py, Line: 2, Column: 0
Instrumentation: cpython, Function: fibonacci, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-hello-flask/fibonacci.py, Line: 2, Column: 0
Instrumentation: cpython, Function: fibonacci, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-hello-flask/fibonacci.py, Line: 2, Column: 0
Instrumentation: cpython, Function: fibonacci, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-hello-flask/fibonacci.py, Line: 2, Column: 0
Instrumentation: cpython, Function: fibonacci, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-hello-flask/fibonacci.py, Line: 2, Column: 0
Instrumentation: cpython, Function: fibonacci_recursive_handler, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-hello-flask/app.py, Line: 58, Column: 0
Instrumentation: cpython, Function: dispatch_request, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-hello-flask/.venv/lib/python3.10/site-packages/flask/app.py, Line: 889, Column: 0
Instrumentation: cpython, Function: full_dispatch_request, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-hello-flask/.venv/lib/python3.10/site-packages/flask/app.py, Line: 911, Column: 0
Instrumentation: cpython, Function: wsgi_app, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-hello-flask/.venv/lib/python3.10/site-packages/flask/app.py, Line: 1506, Column: 0
Instrumentation: cpython, Function: __call__, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-hello-flask/.venv/lib/python3.10/site-packages/flask/app.py, Line: 1536, Column: 0
Instrumentation: cpython, Function: execute, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-hello-flask/.venv/lib/python3.10/site-packages/werkzeug/serving.py, Line: 331, Column: 0
Instrumentation: cpython, Function: run_wsgi, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-hello-flask/.venv/lib/python3.10/site-packages/werkzeug/serving.py, Line: 249, Column: 0
Instrumentation: cpython, Function: handle_one_request, File: /usr/lib/python3.10/http/server.py, Line: 401, Column: 0
Instrumentation: cpython, Function: handle, File: /usr/lib/python3.10/http/server.py, Line: 431, Column: 0
Instrumentation: cpython, Function: handle, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-hello-flask/.venv/lib/python3.10/site-packages/werkzeug/serving.py, Line: 398, Column: 0
Instrumentation: cpython, Function: __init__, File: /usr/lib/python3.10/socketserver.py, Line: 742, Column: 0
Instrumentation: cpython, Function: finish_request, File: /usr/lib/python3.10/socketserver.py, Line: 360, Column: 0
Instrumentation: cpython, Function: process_request_thread, File: /usr/lib/python3.10/socketserver.py, Line: 682, Column: 0
Instrumentation: cpython, Function: run, File: /usr/lib/python3.10/threading.py, Line: 952, Column: 0
Instrumentation: cpython, Function: _bootstrap_inner, File: /usr/lib/python3.10/threading.py, Line: 1001, Column: 0
Instrumentation: cpython, Function: _bootstrap, File: /usr/lib/python3.10/threading.py, Line: 973, Column: 0
```

```
------------------- New Sample --------------------
  thread.name: python3
  process.executable.name: python3.10
  process.executable.path: /usr/bin/python3.10
  process.pid: 144899
  thread.id: 152170
---------------------------------------------------
Instrumentation: native: Function: 0x118b80, File: libc.so.6
Instrumentation: native: Function: 0x2c1f51, File: python3.10
Instrumentation: native: Function: 0x199948, File: python3.10
Instrumentation: cpython, Function: select, File: /usr/lib/python3.10/selectors.py, Line: 406, Column: 0
Instrumentation: cpython, Function: _communicate, File: /usr/lib/python3.10/subprocess.py, Line: 1969, Column: 0
Instrumentation: cpython, Function: communicate, File: /usr/lib/python3.10/subprocess.py, Line: 1128, Column: 0
Instrumentation: cpython, Function: run, File: /usr/lib/python3.10/subprocess.py, Line: 491, Column: 0
Instrumentation: cpython, Function: , File: , Line: 0, Column: 0
Instrumentation: cpython, Function: python_eval_subprocess_run_id_handler, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-hello-flask/app.py, Line: 81, Column: 0
Instrumentation: cpython, Function: dispatch_request, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-hello-flask/.venv/lib/python3.10/site-packages/flask/app.py, Line: 889, Column: 0
Instrumentation: cpython, Function: full_dispatch_request, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-hello-flask/.venv/lib/python3.10/site-packages/flask/app.py, Line: 911, Column: 0
Instrumentation: cpython, Function: wsgi_app, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-hello-flask/.venv/lib/python3.10/site-packages/flask/app.py, Line: 1506, Column: 0
Instrumentation: cpython, Function: __call__, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-hello-flask/.venv/lib/python3.10/site-packages/flask/app.py, Line: 1536, Column: 0
Instrumentation: cpython, Function: execute, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-hello-flask/.venv/lib/python3.10/site-packages/werkzeug/serving.py, Line: 331, Column: 0
Instrumentation: cpython, Function: run_wsgi, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-hello-flask/.venv/lib/python3.10/site-packages/werkzeug/serving.py, Line: 249, Column: 0
Instrumentation: cpython, Function: handle_one_request, File: /usr/lib/python3.10/http/server.py, Line: 401, Column: 0
Instrumentation: cpython, Function: handle, File: /usr/lib/python3.10/http/server.py, Line: 431, Column: 0
Instrumentation: cpython, Function: handle, File: /home/dpacak/go/src/github.com/danielpacak/vulnerable-kubernetes-deployments/examples/python/python3.10-hello-flask/.venv/lib/python3.10/site-packages/werkzeug/serving.py, Line: 398, Column: 0
Instrumentation: cpython, Function: __init__, File: /usr/lib/python3.10/socketserver.py, Line: 742, Column: 0
Instrumentation: cpython, Function: finish_request, File: /usr/lib/python3.10/socketserver.py, Line: 360, Column: 0
Instrumentation: cpython, Function: process_request_thread, File: /usr/lib/python3.10/socketserver.py, Line: 682, Column: 0
Instrumentation: cpython, Function: run, File: /usr/lib/python3.10/threading.py, Line: 952, Column: 0
Instrumentation: cpython, Function: _bootstrap_inner, File: /usr/lib/python3.10/threading.py, Line: 1001, Column: 0
Instrumentation: cpython, Function: _bootstrap, File: /usr/lib/python3.10/threading.py, Line: 973, Column: 0
```
