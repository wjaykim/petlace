import os
from pathlib import Path
import sys

is_bundled = getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS')

def get_file(filename: str):
    if is_bundled:
        return os.path.join(sys._MEIPASS, *filename.split('/'))
    else:
        return os.path.join(Path(__file__).resolve().parent.parent, *filename.split('/'))