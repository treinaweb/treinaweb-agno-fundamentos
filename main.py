from dotenv import load_dotenv
from agno.agent import Agent
from agno.db.sqlite import SqliteDb

load_dotenv()


agent = Agent(
    model="openai:gpt-4.1-mini",
    db=SqliteDb("agent.db"),
    add_history_to_context=True,
)

agent.print_response(
    "Qual o meu nome?",
    session_id="0d581f97fd5491f900971d7704b24d42360f73cc7887fbe5ccae26fa1dcad280",
)
