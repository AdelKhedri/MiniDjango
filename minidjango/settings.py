import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATES = {
    'DIRS': [os.path.join(BASE_DIR, 'templates')]
}