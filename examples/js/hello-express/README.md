### Building and running your application


### Deploying your application to the cloud

First, build your image, e.g.: `docker build -t hello-express .`.
If your cloud uses a different CPU architecture than your development
machine (e.g., you are on a Mac M1 and your cloud provider is amd64),
you'll want to build the image for that platform, e.g.:
`docker build --platform=linux/amd64 -t hello-express .`.

Then, push it to your registry, e.g. `docker push myregistry.com/myapp`.

Consult Docker's [getting started](https://docs.docker.com/go/get-started-sharing/)
docs for more detail on building and pushing.

### References
* [Docker's Node.js guide](https://docs.docker.com/language/nodejs/)

```
docker build -t danielpacak/hello-express:node20-bullseye .
```

```
docker run -d --rm --name hello-express -p 3000:3000 danielpacak/hello-express:node20-bullseye
```

```
docker stop hello-express
```

```
docker image save -o /tmp/hello-express.tar danielpacak/hello-express:node20-bullseye
sudo ctr -n k8s.io image import /tmp/hello-express.tar && rm /tmp/hello-express.tar
```

```
docker run -d --rm --name pyroscope -p 4040:4040 grafana/pyroscope:latest
```