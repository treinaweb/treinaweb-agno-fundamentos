from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from agno.tools.hackernews import HackerNewsTools
from dotenv import load_dotenv
from urllib.parse import quote_plus
import requests


def get_weather(location: str) -> dict:
    """
    Fetch weather information for a given location.

    Args:
        location (str): The name of the location to get weather for.

    Returns:
        dict: Weather data in JSON format from wttr.in API.
    """
    encoded_location = quote_plus(location)
    url = f"https://wttr.in/{encoded_location}?format=j1"

    response = requests.get(url, timeout=10)

    response.raise_for_status()

    return response.json()


load_dotenv()

agent = Agent(
    model=OpenAIResponses(id="gpt-4.1-mini"),
    tools=[HackerNewsTools(), get_weather],
)

agent.print_response("Me dê um resumo geral do clima na cidade de São Paulo")
