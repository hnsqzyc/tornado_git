import os
import sys

print(sys.path)

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

print(sys.path)