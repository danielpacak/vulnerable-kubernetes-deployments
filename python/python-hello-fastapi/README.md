# python-hello-fastapi

This app is a bunch of URL endpoints that allow running crazy insecure Python code. Don't deploy it in production unless
you sabotage your employer.

## Development

1. Create a virtual environment:
   ```
   uv venv
   ```
2. Activate the virtual environment
   ```
   source .venv/bin/activate
   ```
3. Update the project's environment:
   ```
   uv sync --frozen
   ```
4. Run the server in development mode:
   ```
   fastapi dev main.py
   ```
5. Open http://127.0.0.1:8000/items/5?q=somequery in your browser and you'll the see the following response:
   ``` json
   {"item_id": 5, "q": "somequery"}
   ```
6. Open http://127.0.0.1:8000/docs in your browser to see the automatic interactive API documentation provided by Swagger UI.
7. Open http://127.0.0.1:8000/redoc in your browser to see the alternative automatic documentation provided by ReDoc.

## Deployment
### Docker

> [!NOTE]
> Use uv to create requirements.txt:
> ```
> uv pip freeze > requirements.txt
> ```

```
docker buildx build --load -t python-hello-fastapi -f Dockerfile .
```

```
docker run --name python-hello-fastapi -p 80:80 python-hello-fastapi
```
### Kubernetes

1. Load docker image from a local host to cluster nodes:
   ```
   # Kind cluster
   kind load docker-image python-hello-fastapi:latest
   ```
   ```
   # Cluster created with kubeadm
   docker image save -o /tmp/python-hello-fastapi.tar python-hello-fastapi:latest
   sudo ctr -n k8s.io image import /tmp/python-hello-fastapi.tar && rm /tmp/python-hello-fastapi.tar
   ```
2. Create Kubernetes deployment:
   ```
   kubectl apply -f deploy/kubernetes/all.yaml
   ```
3. Forward local port 8000 to a pod:
   ```
   kubectl port-forward -n python-hello-fastapi svc/python-hello-fastapi 8000:8000
   ```

## Further Reading

* https://fastapi.tiangolo.com/
* https://www.starlette.io/
* https://fastapi.tiangolo.com/async/#in-a-hurry
* https://fastapi.tiangolo.com/tutorial/
* https://fastapi.tiangolo.com/deployment/docker/
* https://github.com/astral-sh/uv-docker-example