import asyncio
import dotenv
import os

from agents import Agent, Runner, trace
from openai.types.responses import ResponseTextDeltaEvent

dotenv.load_dotenv()

nutrition_agent = Agent(
    name="Nutrition Assistant",
    instructions="""
  You are a helpful assistant giving out nutrition advice.
  You give concise answers.
  """,
)


async def main():
    response_stream = Runner.run_streamed(nutrition_agent, "How health are bananas?")

    async for event in response_stream.stream_events():
        if event.type == "raw_response_event" and isinstance(
            event.data, ResponseTextDeltaEvent
        ):
            print(event.data.delta, end="", flush=True)


if __name__ == "__main__":
    asyncio.run(main())
