import os
import sys

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
LIB_DIR = os.path.join(ROOT_DIR, "lib")

for path in (ROOT_DIR, LIB_DIR):
    if path not in sys.path:
        sys.path.insert(0, path)