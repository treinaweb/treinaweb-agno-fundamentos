from dotenv import load_dotenv
from agno.agent import Agent

from knowledge import knowledge

load_dotenv()


agent = Agent(
    model="openai:gpt-4.1-mini",
    markdown=True,
    knowledge=knowledge,
    search_knowledge=True,
)

agent.print_response("Me explique como implementar um agent de ia usando o Agno.")
