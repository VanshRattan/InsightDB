import os
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv

# Always load .env from the project root, regardless of the process working directory.
_PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(_PROJECT_ROOT / ".env", override=True)

# API Keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GEMINI_FALLBACK_MODEL = os.getenv("GEMINI_FALLBACK_MODEL", "gemini-3.6-flash")

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@localhost:5432/autonomous_data_analyst",
)
POSTGRES_ENABLED = os.getenv("POSTGRES_ENABLED", "false").strip().lower() in {"1", "true", "yes", "on"}


def _is_configured_key(value: Optional[str]) -> bool:
    if not value:
        return False
    normalized = value.strip().lower()
    return normalized not in {"", "your_groq_api_key", "your_gemini_api_key"}

# Sandbox limits
SANDBOX_TIMEOUT_SECONDS = int(os.getenv("SANDBOX_TIMEOUT_SECONDS", "10"))
SANDBOX_MEMORY_LIMIT_MB = int(os.getenv("SANDBOX_MEMORY_LIMIT_MB", "256"))

def get_llm(temperature: float = 0.0):
    """
    Initializes the LLM. Groq is preferred when configured; otherwise Gemini is used.
    """
    from langchain_groq import ChatGroq
    from langchain_google_genai import ChatGoogleGenerativeAI

    groq_ready = _is_configured_key(GROQ_API_KEY)
    gemini_ready = _is_configured_key(GOOGLE_API_KEY)

    if not groq_ready and not gemini_ready:
        raise ValueError(
            "No LLM API key configured. Set GROQ_API_KEY and/or GOOGLE_API_KEY in the project `.env` file."
        )

    if groq_ready:
        primary_llm = ChatGroq(
            api_key=GROQ_API_KEY,
            model_name=GROQ_MODEL,
            temperature=temperature
        )
        if gemini_ready:
            fallback_llm = ChatGoogleGenerativeAI(
                api_key=GOOGLE_API_KEY,
                model=GEMINI_FALLBACK_MODEL,
                temperature=temperature
            )
            return primary_llm.with_fallbacks([fallback_llm])
        return primary_llm

    return ChatGoogleGenerativeAI(
        api_key=GOOGLE_API_KEY,
        model=GEMINI_FALLBACK_MODEL,
        temperature=temperature
    )
