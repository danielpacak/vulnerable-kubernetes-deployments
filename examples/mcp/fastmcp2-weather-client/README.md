# fastmcp-weather-client

```
uv run fastapi run client.py --port 8000
```

```
docker buildx build --load -f Dockerfile -t danielpacak/fastmcp2-weather-client .
```

```
docker run --rm -it --name fastmcp2-weather-client -p 8000:8000 \
  -e FASTMCP_WEATHER_SERVER_URL="http://localhost:8082/mcp" \
  danielpacak/fastmcp2-weather-client
```

```
k apply -f all.yaml
```

```
k port-forward -n fastmcp2-weather-client svc/fastmcp2-weather-client 8000:8000
```

```
curl -v "http://localhost:8000/weather?location=WARSAW,%20PL"
```

```
curl -v "http://localhost:8000/weather?location=TEL%20AVIV,%20IL"
```
