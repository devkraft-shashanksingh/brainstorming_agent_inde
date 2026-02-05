
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys
# API Keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Model Configuration
# We use standard Flash for prompt engineering for thought traces
GEMINI_THINKING_MODEL = "gemini-3-flash-preview"
# We use standard Flash for fast File Search retrieval
GEMINI_RAG_MODEL = "gemini-3-flash-preview"
GEMINI_CORPUS_NAME = "brainstorming-research-library"

# Available Models for User Selection
AVAILABLE_MODELS = ("gemini-3.0-flash", "gemini-3-pro-preview")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Constants
# Constants
FILE_SEARCH_STORE_NAME = "pharma-brand-library"
# Resolve paths relative to this file to ensure consistency regardless of CWD
BASE_DIR = Path(__file__).resolve().parent.parent

if os.getenv("VERCEL"):
    # Vercel filesystem is read-only except for /tmp
    DATA_DIR = Path("/tmp")
else:
    DATA_DIR = BASE_DIR / "data"

DB_PATH = DATA_DIR / "agents_v2.db"
SESSIONS_DB_PATH = DATA_DIR / "sessions.db"
DOCS_PATH = DATA_DIR / "documents"

# Ensure directories exist
# On Vercel, this will be in /tmp so it should succeed
try:
    if not DATA_DIR.exists():
        DATA_DIR.mkdir(parents=True, exist_ok=True)
    if not DOCS_PATH.exists():
        DOCS_PATH.mkdir(parents=True, exist_ok=True)
except Exception as e:
    # Log error but don't crash immediately if possible, though needed for DB
    print(f"Warning: Could not create data directories: {e}")
