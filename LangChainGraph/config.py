# =============================================================================
# Global Model Configuration for LangChain & LangGraph Learning Notebooks
# =============================================================================
#
# This module provides centralized model configuration used across all notebooks.
# Two models are configured:
#   - GPT-4o-mini (OpenAI) - Fast, cost-effective model for learning
#   - Gemini Flash (Google) - Google's fast multimodal model
#
# Usage:
#     from config import GPT_MODEL, GEMINI_MODEL, get_model, list_available_models
# =============================================================================

# Install dependencies (run once)
# !pip install langchain langchain-openai langchain-google-genai langgraph python-dotenv

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# =============================================================================
# GLOBAL CONFIGURATION
# =============================================================================
GPT_MODEL_NAME = "gpt-4o-mini"         # Change to "gpt-4o" for more capable model
GEMINI_MODEL_NAME = "gemini-3-flash-preview"  # Google's fast multimodal model
# =============================================================================

from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

# ---------------------------------------------------------------------------
# API Key Validation
# ---------------------------------------------------------------------------
_missing_keys = []
if not os.getenv("OPENAI_API_KEY"):
    _missing_keys.append("OPENAI_API_KEY")
if not os.getenv("GEMINI_API_KEY"):
    _missing_keys.append("GEMINI_API_KEY")

if _missing_keys:
    print(f"WARNING: Missing API keys: {', '.join(_missing_keys)}")
    print("Set them in your .env file or as environment variables.")
    print("Some model calls will fail without the corresponding API key.\n")

# ---------------------------------------------------------------------------
# Global Model Instances
# ---------------------------------------------------------------------------

# OpenAI GPT-4o-mini
GPT_MODEL = ChatOpenAI(
    model=GPT_MODEL_NAME,
    temperature=0,
    api_key=os.getenv("OPENAI_API_KEY"),
)

# Google Gemini 2.0 Flash
GEMINI_MODEL = ChatGoogleGenerativeAI(
    model=GEMINI_MODEL_NAME,
    temperature=0,
    google_api_key=os.getenv("GEMINI_API_KEY"),
)

# ---------------------------------------------------------------------------
# Model Registry (for easy switching in notebooks)
# ---------------------------------------------------------------------------
MODEL_REGISTRY = {
    "gpt-4o-mini": GPT_MODEL,
    "gemini-3-flash-preview": GEMINI_MODEL,
}

DEFAULT_MODEL = GPT_MODEL


def get_model(name: str = "gpt-4o-mini"):
    """
    Retrieve a model by name.

    Args:
        name: One of 'gpt-4o-mini' or 'gemini-flash'

    Returns:
        A LangChain ChatModel instance.
    """
    if name not in MODEL_REGISTRY:
        raise KeyError(
            f"Model '{name}' not found. Available: {list(MODEL_REGISTRY.keys())}"
        )
    return MODEL_REGISTRY[name]


def list_available_models():
    """Print all available models."""
    print("Available Models:")
    print("-" * 55)
    for name, model in MODEL_REGISTRY.items():
        model_id = getattr(model, "model_name", None) or getattr(model, "model", "unknown")
        provider = model.__class__.__name__
        print(f"  {name:20s} -> {provider}({model_id})")
    print("-" * 55)


# ---------------------------------------------------------------------------
# Confirmation
# ---------------------------------------------------------------------------
print(f"OpenAI client initialized  -> model: {GPT_MODEL_NAME}")
print(f"Google client initialized  -> model: {GEMINI_MODEL_NAME}")
