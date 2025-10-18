import asyncio
from dotenv import load_dotenv

from agents import Agent, Runner, SQLiteSession

load_dotenv()


async def main():
    # Create agent
    agent = Agent(
        name="Assistant",
        instructions="Reply very concisely",
    )

    # Create session instance
    session = SQLiteSession("conversation_dlopera")

    # First turn
    result = await Runner.run(
        agent,
        "What city is the Golden Gate Bridge in?",
        session=session,
    )
    print("First turn:", result.final_output)

    # Second turn - Agent automatically remembers previous conversation
    result = await Runner.run(
        agent,
        "What state is it in?",
        session=session,
    )
    print("Second turn:", result.final_output)

    # Third turn
    result = await Runner.run(
        agent,
        "What is the population?",
        session=session,
    )
    print("Third turn:", result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
