# Mirth Connect by NextGen Healthcare

```
kubectl apply -f java/mirth
```

```
kubectl port-forward -n mirth svc/mirth-connect 8443
```

Navigate to https://localhost:8443/ and sign in as `admin:admin`.

To uninstall Mirth Connect:

```
kubectl delete -f java/mirth/
```

We expect that the dynamic-ebpf agent detects the following packages when the
Mirth Connect deployment is created:

```
docker pull docker.io/nextgenhealthcare/connect:4.5@sha256:3c39d537d0b253d99d1c56d4a6d099f0e958e2e40eb6e2076a0bc4ff70338889
```

```
/opt/connect/extensions/doc/lib/itext-2.1.7.jar
/opt/connect/extensions/doc/lib/itext-rtf-2.1.7.jar
/opt/connect/extensions/doc/lib/flying-saucer-core-9.0.1.jar
/opt/connect/extensions/doc/lib/flying-saucer-pdf-9.0.1.jar
/opt/connect/extensions/doc/lib/openhtmltopdf-core-1.0.9.jar
/opt/connect/extensions/doc/lib/openhtmltopdf-pdfbox-1.0.9.jar
/opt/connect/extensions/doc/lib/xmpbox-2.0.24.jar
/opt/connect/extensions/doc/lib/fontbox-2.0.24.jar
/opt/connect/extensions/doc/lib/graphics2d-0.32.jar
...
```
