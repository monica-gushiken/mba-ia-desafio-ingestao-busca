import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document
from langchain_postgres import PGVector

load_dotenv()
for k in ("GOOGLE_API_KEY", "OPENAI_API_KEY", "DATABASE_URL","PG_VECTOR_COLLECTION_NAME", "PDF_PATH"):
    if not os.getenv(k):
        raise RuntimeError(f"Environment variable {k} is not set")

PDF_PATH = os.getenv("PDF_PATH")
loader = PyPDFLoader(PDF_PATH)
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
chunks = splitter.split_documents(docs)
print(f"Total de chunks: {len(chunks)}")

if not chunks:
    raise RuntimeError("No chunks found")

enriched =[
    Document(
        page_content=d.page_content,
        metadata={k: v for k, v in d.metadata.items() if v not in ("",None)}
    ) for d in chunks
]

ids = [f"doc-{i}" for i in range(len(enriched))]

# OpenAI embeddings
embeddings = OpenAIEmbeddings(model=os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small"))

# Google embeddings
# embeddings = GoogleGenerativeAIEmbeddings(model=os.getenv("GOOGLE_EMBEDDING_MODEL", "models/embedding-001"))

store = PGVector(
    embeddings = embeddings,
    collection_name = os.getenv("PG_VECTOR_COLLECTION_NAME"),
    connection = os.getenv("DATABASE_URL"),
    use_jsonb = True
)

store.add_documents(documents=enriched, ids=ids)
print(f"Total de documentos adicionados: {len(enriched)}")