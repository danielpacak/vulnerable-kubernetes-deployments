# python-hello-flask

```
uv venv
```

```
source .venv/bin/activate
```

```
uv run app.py
```

```
uv run flask --app app run
# or
flask run
```

``` console
$ flask routes
Endpoint           Methods    Rule
-----------------  ---------  -----------------------
hello              GET, POST  /hello
index              GET        /
show_user_profile  GET        /user/<username>
static             GET        /static/<path:filename>
```



# Docker

> ```
> echo "$GH_PAT" | docker login ghcr.io -u danielpacak --password-stdin
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

## Kubernetes

```
docker image save -o /tmp/python-hello-flask.tar python-hello-flask:latest
sudo ctr -n k8s.io image import /tmp/python-hello-flask.tar && rm /tmp/python-hello-flask.tar
```

```
k apply -f deploy/kubernetes/all.yaml
```

```
k port-forward -n python-hello-flask svc/python-hello-flask 5050:5050
```

## Further Reading

* https://flask.palletsprojects.com/en/stable/quickstart/
* https://realpython.com/python-uv/
* https://github.com/astral-sh/uv-docker-example
* https://docs.astral.sh/uv/guides/integration/docker/
* https://docs.astral.sh/ruff/installation/
