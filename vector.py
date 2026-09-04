import hashlib
from pathlib import Path

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings


PROJECT_DIR = Path(__file__).resolve().parent
DATA_FILE = PROJECT_DIR / "data.txt"
DB_DIRECTORY = PROJECT_DIR / "chroma_langchain_db"

if not DATA_FILE.exists():
    raise FileNotFoundError(
        f"{DATA_FILE.name} was not found. Create it in {PROJECT_DIR} and add "
        "the information that the assistant should use."
    )

text = DATA_FILE.read_text(encoding="utf-8").strip()
if not text:
    raise ValueError("data.txt is empty. Add your source information first.")

embeddings = OllamaEmbeddings(model="mxbai-embed-large")

# A different collection is selected whenever data.txt changes, preventing old
# restaurant embeddings from being returned without requiring manual cleanup.
content_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]
collection_name = f"documents_{content_hash}"

vector_store = Chroma(
    collection_name=collection_name,
    persist_directory=str(DB_DIRECTORY),
    embedding_function=embeddings,
)

if vector_store._collection.count() == 0:
    chunk_size = 1000
    overlap = 150
    step = chunk_size - overlap
    chunks = [text[start : start + chunk_size] for start in range(0, len(text), step)]
    documents = [
        Document(page_content=chunk, metadata={"source": DATA_FILE.name})
        for chunk in chunks
    ]
    ids = [f"{content_hash}-{index}" for index in range(len(documents))]
    vector_store.add_documents(documents=documents, ids=ids)

retriever = vector_store.as_retriever(search_kwargs={"k": 5})
