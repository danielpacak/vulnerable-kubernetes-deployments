# .NET eShop

```
aspire do build-webhooksclient
aspire do build-webhooks-api
aspire do build-basket-api
aspire do build-catalog-api
aspire do build-identity-api
aspire do build-order-processor
aspire do build-ordering-api
aspire do build-payment-processor
aspire do build-webapp
```

```
docker image tag webhooksclient:latest danielpacak/dotnet-eshop-webhooksclient:latest
docker image tag webhooks-api:latest danielpacak/dotnet-eshop-webhooks-api:latest
docker image tag basket-api:latest danielpacak/dotnet-eshop-basket-api:latest
docker image tag catalog-api:latest danielpacak/dotnet-eshop-catalog-api:latest
docker image tag identity-api:latest danielpacak/dotnet-eshop-identity-api:latest
docker image tag order-processor:latest danielpacak/dotnet-eshop-order-processor:latest
docker image tag ordering-api:latest danielpacak/dotnet-eshop-ordering-api:latest
docker image tag payment-processor:latest danielpacak/dotnet-eshop-payment-processor:latest
docker image tag webapp:latest danielpacak/dotnet-eshop-webapp:latest
```

```
docker image push danielpacak/dotnet-eshop-webhooksclient:latest
docker image push danielpacak/dotnet-eshop-webhooks-api:latest
docker image push danielpacak/dotnet-eshop-basket-api:latest
docker image push danielpacak/dotnet-eshop-catalog-api:latest
docker image push danielpacak/dotnet-eshop-identity-api:latest
docker image push danielpacak/dotnet-eshop-order-processor:latest
docker image push danielpacak/dotnet-eshop-ordering-api:latest
docker image push danielpacak/dotnet-eshop-payment-processor:latest
docker image push danielpacak/dotnet-eshop-webapp:latest
```

```
docker image save --output /tmp/dotnet-eshop-images.tar \
  danielpacak/dotnet-eshop-webhooksclient:latest \
  danielpacak/dotnet-eshop-webhooks-api:latest \
  danielpacak/dotnet-eshop-basket-api:latest \
  danielpacak/dotnet-eshop-catalog-api:latest \
  danielpacak/dotnet-eshop-identity-api:latest \
  danielpacak/dotnet-eshop-order-processor:latest \
  danielpacak/dotnet-eshop-ordering-api:latest \
  danielpacak/dotnet-eshop-payment-processor:latest \
  danielpacak/dotnet-eshop-webapp:latest
```

```
sudo ctr -n k8s.io image import /tmp/dotnet-eshop-images.tar && rm /tmp/dotnet-eshop-images.tar
```

```
helm install dotnet-eshop ./k8s-artifacts \
  --namespace dotnet-eshop --create-namespace \
  --values values.yaml
```

```
helm install dotnet-eshop ./dotnet-eshop \ 
  --namespace dotnet-eshop --create-namespace \
  --values ./dotnet-eshop/values.override.yaml
```


```
helm uninstall -n dotnet-eshop dotnet-eshop
```
