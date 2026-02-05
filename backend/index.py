import sys
import os

# Add the current directory to sys.path to ensure 'data_library' is importable
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from data_library.api import app
