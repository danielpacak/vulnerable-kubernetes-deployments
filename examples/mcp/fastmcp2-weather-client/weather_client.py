from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport
import asyncio

transport = StreamableHttpTransport(url="http://localhost:8020/mcp")
client = Client(transport)


async def main():
    print("Hello from fastmcp2-weather-client!")
    async with client:
        print(f"Client connected: {client.is_connected()}")
        tools = await client.list_tools()
        print(f"Available tools: {tools}")
        if any(tool.name == "get_weather_conditions" for tool in tools):
            result = await client.call_tool(
                "get_weather_conditions", {"location": "Warsaw, PL"}
            )
            print(f"Call result: {result}")

    print(f"Client connected: {client.is_connected()}")


if __name__ == "__main__":
    asyncio.run(main())
