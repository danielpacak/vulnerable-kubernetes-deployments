# phpMyAdmin 4.8.1 Base Image

```
docker buildx build -t docker.io/danielpacak/vulhub-phpmyadmin:4.8.1 .
```

```
docker image save -o /tmp/phpmyadmin.tar docker.io/danielpacak/vulhub-phpmyadmin:4.8.1
sudo ctr -n k8s.io image import /tmp/phpmyadmin.tar && rm /tmp/phpmyadmin.tar
```