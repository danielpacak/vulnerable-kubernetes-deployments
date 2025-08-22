docker buildx build --load -t python-hello-flask -f Dockerfile .

docker image save -o /tmp/python-hello-flask.tar python-hello-flask:latest
sudo ctr -n k8s.io image import /tmp/python-hello-flask.tar && rm /tmp/python-hello-flask.tar
