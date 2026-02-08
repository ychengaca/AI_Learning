"""
Global Configuration for Anthropic SDK Learning Notebooks
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# =============================================================================
# API Configuration
# =============================================================================
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# =============================================================================
# Model Configuration
# =============================================================================
# Global model variable - Claude 3 Haiku (fastest and most cost-effective)
MODEL = "claude-3-haiku-20240307"

# Alternative models for reference:
# MODEL_SONNET = "claude-3-sonnet-20240229"      # Balanced performance
# MODEL_OPUS = "claude-3-opus-20240229"          # Most capable
# MODEL_SONNET_35 = "claude-3-5-sonnet-20241022" # Latest Sonnet

# =============================================================================
# Default Parameters
# =============================================================================
DEFAULT_MAX_TOKENS = 1024
DEFAULT_TEMPERATURE = 1.0  # Range: 0.0 to 1.0

# =============================================================================
# Validation
# =============================================================================
def validate_api_key():
    """Validate that the API key is configured."""
    if not ANTHROPIC_API_KEY or ANTHROPIC_API_KEY == "your-api-key-here":
        raise ValueError(
            "Please set your ANTHROPIC_API_KEY in the .env file.\n"
            "Get your API key from: https://console.anthropic.com/"
        )
    return True

if __name__ == "__main__":
    print(f"Model configured: {MODEL}")
    try:
        validate_api_key()
        print("API key is configured.")
    except ValueError as e:
        print(f"Warning: {e}")
