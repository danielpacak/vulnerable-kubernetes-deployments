# Vulnerable Kubernetes Deployments

For learning, researching, testing and \[ evaluating | evading \] Kubernetes
security tools. This project is inspired by [Vulhub] but uses Kubernetes
deployments instead of Docker Compose services.

[Vulhub]: https://github.com/vulhub/vulhub

## Quick Start

Deploy a vulnerable pgAdmin:

```
k apply -f python/pgadmin/CVE-2023-5002/all.yaml
```

```
k port-forward -n pgadmin-cve-2023-5002 svc/pgadmin 5050:5050
```

Open http://localhost:5050 in your web browser to access pgAdmin console.

> Uninstall pgAdmin with:
>
> ```
> k delete -f python/pgadmin/CVE-2023-5002/all.yaml
> ```

## Catalog

## ADRMetry Pulse

TBD

## ADRMetry Pulse

TBD

## ProfileMetry Pulse

## Contributing

At your own risk!

## License

TBD
