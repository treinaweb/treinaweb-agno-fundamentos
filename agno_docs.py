from dotenv import load_dotenv

from knowledge import knowledge

load_dotenv()

knowledge.insert(url="https://docs.agno.com/sdk/introduction.md")
knowledge.insert(url="https://docs.agno.com/sdk/setup.md")
knowledge.insert(url="https://docs.agno.com/agents/overview.md")
knowledge.insert(url="https://docs.agno.com/agents/building-agents.md")
