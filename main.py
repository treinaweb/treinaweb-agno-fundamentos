from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from agno.tools.hackernews import HackerNewsTools
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=OpenAIResponses(id="gpt-4.1-mini"),
    tools=[HackerNewsTools()],
)

agent.print_response("Quais os tópicos mais discutidos no Hacker News hoje?")
