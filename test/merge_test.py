import random
import pathlib
import sys

d = pathlib.Path(__file__).resolve().parent.parent
sys.path.append(str(d))

from src.merge import merge


# a random list including repeated
a = random.choices(list(range(10)), k=10)
b = merge(a)
print(b)
