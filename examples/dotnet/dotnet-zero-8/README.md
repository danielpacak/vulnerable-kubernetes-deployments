# dotnet-zero-8

## Build and run locally

```
mise use dotnet@8
```

```
dotnet build
```

```
dotnet run
```

## Build and run in container

```
docker buildx build --push --platform linux/amd64,linux/arm64 -t danielpacak/dotnet-zero:8 -f Dockerfile .
```

```
docker run --rm --name dotnet-zero-8 -p 8080:8080 danielpacak/dotnet-zero:8
```
