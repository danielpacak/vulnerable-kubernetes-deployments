# Spring PetClinic Sample Application

https://github.com/spring-projects/spring-petclinic/

```
kubectl apply -f java/petclinic/
```

```
kubectl port-forward -n petclinic svc/petclinic 9090:80
```

Navigate to http://localhost:9090

To uninstall Spring PetClinic:

```
kubectl delete -f java/petclinic/
```
