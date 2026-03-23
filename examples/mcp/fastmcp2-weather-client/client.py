from fastapi import FastAPI
import uvicorn
import weather

app = FastAPI()


@app.get("/health")
async def handle_health():
    return {"status": "healthy"}


@app.get("/weather")
async def handle_weather_by_location(location: str):
    summary = await weather.get_weather_summary(location)
    return {"summary": summary}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
