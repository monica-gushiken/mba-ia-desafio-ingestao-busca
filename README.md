# Desafio MBA Engenharia de Software com IA - Full Cycle

Sistema de busca semântica e chat baseado em RAG (Retrieval-Augmented Generation). Ingere documento PDF, armazena os chunks como embeddings no PostgreSQL com pgvector, e responde perguntas com base exclusivamente no conteúdo ingerido, usando LangChain e OpenAI.

## Pré-requisitos

- Docker e Docker Compose
- Python 3.10+
- Chave de API OpenAI
- Chave de API Google

## Configuração

Copie o arquivo de exemplo e preencha as variáveis:

```bash
cp .env.example .env
```

| Variável | Descrição | Exemplo |
|---|---|---|
| `OPENAI_API_KEY` | Chave da API OpenAI | `sk-...` |
| `GOOGLE_API_KEY` | Chave da API Google | `AIza...` |
| `OPENAI_EMBEDDING_MODEL` | Modelo de embeddings OpenAI | `text-embedding-3-small` |
| `GOOGLE_EMBEDDING_MODEL` | Modelo de embeddings Google | `models/embedding-001` |
| `DATABASE_URL` | String de conexão PostgreSQL | `postgresql+psycopg://postgres:postgres@localhost:5432/rag` |
| `PG_VECTOR_COLLECTION_NAME` | Nome da coleção no PGVector | `document_collection` |
| `PDF_PATH` | Caminho para o PDF a ser ingerido | `document.pdf` |

## Instalação

```bash
python -m venv venv
```

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

```bash
pip install -r requirements.txt
```

## Execução

### 1. Subir o banco de dados:

```bash
docker-compose up -d
```

### 2. Executar ingestão do PDF:

```bash
python src/ingest.py
```

### 3. Rodar o chat:

```bash
python src/chat.py
```
