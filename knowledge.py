from agno.knowledge.knowledge import Knowledge
from agno.vectordb.chroma import ChromaDb
from agno.vectordb.search import SearchType
from agno.knowledge.embedder.openai import OpenAIEmbedder

knowledge = Knowledge(
    vector_db=ChromaDb(
        collection="docs",
        path="./data/chroma",
        persistent_client=True,
        search_type=SearchType.hybrid,
        embedder=OpenAIEmbedder(id="text-embedding-3-small"),
    ),
)
