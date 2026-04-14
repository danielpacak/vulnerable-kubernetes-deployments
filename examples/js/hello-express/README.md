# Hello Express

The simplest Express app with the `GET /process/exec` endpoint to capture Node
stack trace that led to command execution.

## CVE-2026-40175
CVE-2025-62718

docker push danielpacak/hello-express:node24-bookworm-production

## Build and Run Locally

```
mise use node@24
```

```
npm install && npm start
```


## Build and Run in Docker

```
docker build \
  --build-arg NODE_VERSION=24 \
  --build-arg NODE_ENV=production \
  --tag danielpacak/hello-express:node24-bookworm-production .
```

```
docker build \
  --build-arg NODE_VERSION=20.10.0 \
  --build-arg NODE_ENV=production \
  --tag danielpacak/hello-express:node20-prd-bullseye .
```

```
docker build \
  --build-arg NODE_VERSION=20.10.0 \
  --build-arg NODE_ENV=development \
  --tag danielpacak/hello-express:node20-dev-bullseye .
```

```
docker run -d --rm --name hello-express-prd -p 3000:3000 \
  danielpacak/hello-express:node20-prd-bullseye
```

```
docker run -d --rm --name hello-express-dev -p 3001:3000 \
  danielpacak/hello-express:node20-dev-bullseye
```

```
docker stop hello-express-prd hello-express-dev
```

```
IMAGE_TAR="/tmp/hello-express.tar"
docker image save -o $IMAGE_TAR danielpacak/hello-express
sudo ctr -n k8s.io image import $IMAGE_TAR && rm $IMAGE_TAR
```

```
docker run -d --rm --name pyroscope -p 4040:4040 grafana/pyroscope:latest
```

## References

* [Docker's Node.js guide](https://docs.docker.com/language/nodejs/)
