import os
import sys

is_bundled = getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS')

def get_file(filename):
    if is_bundled:
        return os.path.join(sys._MEIPASS, filename)
    else:
        return os.path.join(os.getcwd(), filename)