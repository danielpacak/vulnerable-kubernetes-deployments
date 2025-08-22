docker buildx build --load -t python-hello-fastapi -f Dockerfile .

docker image save -o /tmp/python-hello-fastapi.tar python-hello-fastapi:latest
sudo ctr -n k8s.io image import /tmp/python-hello-fastapi.tar && rm /tmp/python-hello-fastapi.tar
