import random
import pathlib
import sys

d = pathlib.Path(__file__).resolve().parent.parent
sys.path.append(str(d))

from src import quick


a = random.sample(list(range(0, 10)), k=10)
b = quick.quick(a, 0, len(a) - 1)
print(b)
