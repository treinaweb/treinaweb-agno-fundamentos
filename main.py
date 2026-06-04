from dotenv import load_dotenv
from agno.agent import Agent
from agno.db.sqlite import SqliteDb

load_dotenv()


agent = Agent(
    model="openai:gpt-4.1-mini",
    db=SqliteDb("agent.db"),
    enable_agentic_memory=True,
)

memories = agent.get_user_memories(user_id="cleyson@mail.com")

for memory in memories:
    print(memory.memory)
