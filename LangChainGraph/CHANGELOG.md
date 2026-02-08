# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Added
- Global model configuration (`config.py`) with GPT-4o-mini and Gemini 2.0 Flash
- Model registry with `get_model()` and `list_available_models()` helper functions
- API key validation with warnings on missing keys
- Python dependencies file (`requirements.txt`) with all required packages
- Environment variable template (`.env.example`) for API keys

#### Learning Notebooks
- **01 Entry Level** (`notebooks/01_entry_level_langchain_basics.ipynb`)
  - Chat models, message types, prompt templates
  - LCEL chains with pipe operator
  - Tools and basic ReAct agents
  - Streaming responses and structured output
- **02 Intermediate** (`notebooks/02_intermediate_langchain_langgraph.ipynb`)
  - LCEL advanced patterns: RunnableParallel, RunnableLambda, RunnablePassthrough
  - LangGraph fundamentals: StateGraph, nodes, edges
  - Conditional edges and agent loops with tool integration
  - Graph visualization
- **03 Advanced** (`notebooks/03_advanced_langgraph.ipynb`)
  - Persistence and checkpointing with MemorySaver
  - Human-in-the-loop with interrupt_before
  - Streaming graph events in real-time
  - Subgraphs for modular architectures
  - Custom state reducers
  - Error handling and fallback patterns in graphs
- **04 Specialty** (`notebooks/04_specialty_rag_and_multi_agent.ipynb`)
  - Complete RAG pipeline with ChromaDB vector store
  - Multi-agent system: Researcher -> Writer -> Reviewer
  - Production patterns: fallback chains, retry logic
  - LangSmith observability and tracing
  - Cross-model evaluation with structured output
