import asyncio
import dotenv

from agents import Agent, ModelSettings, Runner, function_tool, trace

dotenv.load_dotenv()


@function_tool
def get_food_calories(food_item: str) -> str:
    """
    Get calorie information for common foods to help  with nutrition tracking.

    Args:
        food_item (str): The name of the food item (e.g., "banana", "apple")

    Returns:
        str: Calorie information per standard serving size.
    """
    calories_data = {
        "apple": "80 calories per medium apple (182g)",
        "banana": "105 calories per medium banana (118g)",
        "broccoli": "25 calories per 1 cup chopped (91g)",
        "almonds": "164 calories per 1oz (28g) or about 23 nuts",
    }

    food_key = food_item.lower()
    if food_key in calories_data:
        return f"{food_item.title()}: {calories_data[food_key]}"

    return f"Sorry, I don't have calorie information for {food_item}."


nutrition_agent = Agent(
    name="Nutrition Assistant",
    instructions="""
    You are a helpful assistant giving out nutrition advice.
    You give concise answers.
    """,
    tools=[get_food_calories],
    # model_settings=ModelSettings(tool_choice="get_food_calories"),
)


async def main():
    with trace("Nutrition Assistant with tools"):
        response = await Runner.run(
            nutrition_agent, "How many calories are in total in a banana and an apple?"
        )
        print(response.final_output)


if __name__ == "__main__":
    asyncio.run(main())
