IMAGE_REF="docker.io/danielpacak/python-hello-fastapi:python3.9-glibc"
IMAGE_TAR="/tmp/python-hello-fastapi.tar"

docker buildx build --load -t $IMAGE_REF -f Dockerfile .

docker image save -o $IMAGE_TAR $IMAGE_REF
sudo ctr -n k8s.io image import $IMAGE_TAR && rm $IMAGE_TAR
