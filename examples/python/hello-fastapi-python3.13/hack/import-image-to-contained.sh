docker buildx build --load -t docker.io/danielpacak/python-hello-fastapi:python3.13 -f Dockerfile .

docker image save -o /tmp/python-hello-fastapi.tar docker.io/danielpacak/python-hello-fastapi:python3.13
sudo ctr -n k8s.io image import /tmp/python-hello-fastapi.tar && rm /tmp/python-hello-fastapi.tar
