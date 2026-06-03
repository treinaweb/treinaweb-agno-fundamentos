from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=OpenAIResponses(id="gpt-4.1-mini"),
)

agent.print_response("Me explique o que é uma LLM?")

# result = agent.run("Me explique o que é uma LLM?")
# print(result)
