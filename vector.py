from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

df = pd.read_csv("nba_player_stats_2025.csv")
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

db_location = "./chroma_langchain_db"
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids = []

    for i, row in df.iterrows():
        document = Document(
            page_content = f"{row['Player']} | PTS: {row['PTS']} | FG%: {row['FG%']} | 3P%: {row['3P%']}",
            metadata = {
                "FGM": row["FGM"], "FGA": row["FGA"],
                "FTM": row["FTM"], "FTA": row["FTA"],
            },
            id=str(i),
        )
        ids.append(str(i))
        documents.append(document)

vector_store = Chroma(
    collection_name="nba_player_stats",
    persist_directory=db_location,
    embedding_function=embeddings,
)

if add_documents:
    vector_store.add_documents(documents=documents, ids=ids)

retriever = vector_store.as_retriever(
    search_kwargs={"k": 5},
)
