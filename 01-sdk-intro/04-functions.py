import asyncio
from dotenv import load_dotenv

from agents import Agent, Runner, function_tool

load_dotenv()


@function_tool
def get_weather(city: str) -> str:
    return f"The weather in {city} is sunny"


agent = Agent(
    name="Weather Agent",
    instructions="You are a helpful weather agent",
    tools=[get_weather],
)


async def main():
    result = await Runner.run(agent, "What's the weather in New York?")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
