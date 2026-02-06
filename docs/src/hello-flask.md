# Hello Flask Web App

The purpose is to have an app with vulnerable HTTP endpoints that we can
test for thread detection. For example, there are endpoits that led to
command execution or other serialization issues such as Python Pickle.

## Versions

Currently we have the same code but shipped and built into Docker containers
for the following Python versions:

* Python 3.9
* Python 3.10
* Python 3.13

## Run

```
uv run --no-sync flask run --host=0.0.0.0 --port=5050
```

Open <http://localhost:5050> in your web browser.

## Build Container image

```
cd examples/python/hello-flask-python3.13
docker buildx build --load -t docker.io/danielpacak/python-hello-flask:python3.13-glibc -f Dockerfile .
```

```
docker run --rm -it --name python-hello-flask -p 5050:5050 docker.io/danielpacak/python-hello-flask:python3.13-glibc
```

Open <http://localhost:5050> in your web browser.

## Kubernetes

=== "Hello Flask Python 3.13"

    ```
    k apply -f examples/python/hello-flask-python3.13/deploy/kubernetes/all.yaml
    ```

=== "Hello Flask Python 3.10"

    ```
    k apply -f examples/python/hello-flask-python3.10/deploy/kubernetes/all.yaml
    ```

=== "Hello Flask Python 3.9"

    ```
    k apply -f examples/python/hello-flask-python3.9/deploy/kubernetes/all.yaml
    ```

## TODO

1. Switch to production WSIG server
