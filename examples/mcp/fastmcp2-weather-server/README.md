# fastmcp2-weather-server

```
uvicorn fastmcp2_weather_server:app --host 0.0.0.0 --port 8020
```

```
docker buildx build --load -f Dockerfile -t danielpacak/fastmcp2-weather-server .
```

```
docker run --rm -it --name fastmcp2-weather-server -p 8020:8020 danielpacak/fastmcp2-weather-server
```

```
k apply -f all.yaml
```

http://fastmcp2-weather-server.fastmcp2-weather-server:8020/mcp