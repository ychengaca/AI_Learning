# LlamaIndex Learning Path

A comprehensive collection of Python notebooks to learn LlamaIndex from beginner to advanced levels.

## Overview

[LlamaIndex](https://developers.llamaindex.ai/) is a data framework for building LLM-powered applications. It provides tools for:
- **Data Ingestion**: Connect to 100+ data sources
- **Data Indexing**: Structure your data for LLM consumption
- **Query Interface**: Natural language querying over your data
- **Agents & Workflows**: Build autonomous AI systems

## Prerequisites

- Python 3.9+
- OpenAI API key (for most examples)
- Basic Python knowledge
- Understanding of LLMs (helpful but not required)

## Setup

### 1. Create Virtual Environment

```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure API Keys

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your-openai-api-key
ANTHROPIC_API_KEY=your-anthropic-api-key  # Optional
LLAMA_CLOUD_API_KEY=your-llamacloud-key   # Optional, for LlamaCloud features
```

## Learning Path Structure

### Level 1: Basic (Start Here)
| Notebook | Description | Duration |
|----------|-------------|----------|
| `01-basic/01_introduction.ipynb` | LlamaIndex overview, installation, first query | 30 min |
| `01-basic/02_simple_rag.ipynb` | Build your first RAG pipeline | 45 min |
| `01-basic/03_querying_basics.ipynb` | Query engines, response modes, streaming | 45 min |

### Level 2: Intermediate
| Notebook | Description | Duration |
|----------|-------------|----------|
| `02-intermediate/01_index_types.ipynb` | Vector, Summary, Tree, Keyword indexes | 60 min |
| `02-intermediate/02_custom_retrieval.ipynb` | Custom retrievers, reranking, fusion | 60 min |
| `02-intermediate/03_chat_engine.ipynb` | Conversational interfaces with memory | 45 min |

### Level 3: Advanced
| Notebook | Description | Duration |
|----------|-------------|----------|
| `03-advanced/01_agents.ipynb` | Building autonomous agents with tools | 90 min |
| `03-advanced/02_workflows.ipynb` | Complex multi-step workflows | 90 min |
| `03-advanced/03_custom_components.ipynb` | Custom LLMs, embeddings, retrievers | 60 min |

### Level 4: Specialty Topics
| Notebook | Description | Duration |
|----------|-------------|----------|
| `04-specialty/01_multimodal_rag.ipynb` | RAG with images, tables, and documents | 60 min |
| `04-specialty/02_graph_rag.ipynb` | Knowledge graphs and GraphRAG | 90 min |
| `04-specialty/03_llama_cloud.ipynb` | LlamaCloud Parse, Extract, Index | 60 min |

## Key Concepts

### RAG (Retrieval-Augmented Generation)
RAG enhances LLM responses by retrieving relevant context from your data:
1. **Load** - Ingest documents from various sources
2. **Index** - Create searchable representations
3. **Query** - Retrieve relevant chunks and generate responses

### Core Components
- **Documents**: Raw data containers
- **Nodes**: Chunks of documents with metadata
- **Index**: Data structure for efficient retrieval
- **Query Engine**: Interface for querying indexed data
- **Chat Engine**: Conversational interface with memory

## Tips for Learning

1. **Run code cells sequentially** - Each notebook builds on previous cells
2. **Experiment with parameters** - Modify chunk sizes, models, prompts
3. **Check the data folder** - Sample data files are provided
4. **Read error messages** - They often indicate missing API keys or dependencies

## Resources

- [LlamaIndex Documentation](https://docs.llamaindex.ai/)
- [LlamaIndex GitHub](https://github.com/run-llama/llama_index)
- [LlamaIndex Discord](https://discord.gg/llamaindex)
- [LlamaCloud](https://cloud.llamaindex.ai/)

## Sample Data

The `data/` folder contains sample documents for the exercises:
- `data/sample_docs/` - Text and PDF files for basic exercises
- `data/paul_graham/` - Paul Graham essays (classic LlamaIndex example)

## Troubleshooting

### Common Issues

**API Key errors**: Ensure `.env` file exists and keys are valid

**Import errors**: Run `pip install -r requirements.txt` again

**Async errors in Jupyter**: Add this to notebook cells:
```python
import nest_asyncio
nest_asyncio.apply()
```

---

Happy Learning!
