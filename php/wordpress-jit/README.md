# Wordpress with and without JIT enabled

## Build container image with JIT enabled

```
docker buildx build --load -t wordpress:6.8-php8.1-jit -f Dockerfile .
```

```
docker image save -o /tmp/wordpress-jit.tar wordpress:6.8-php8.1-jit
sudo ctr -n k8s.io image import /tmp/wordpress-jit.tar && rm /tmp/wordpress-jit.tar
```

vim /usr/local/etc/php/conf.d/docker-php-ext-opcache.ini

* https://doinwp.com/best-php-opcache-settings-for-wordpress/#php-op-cache-word-press-and-jit-compilation
* https://dev.to/tugboatqa/php-8-0-is-almost-here-how-to-turn-on-jit-compiling-1l6l
* https://wordpress.org/plugins/atec-cache-info/#installation
