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
