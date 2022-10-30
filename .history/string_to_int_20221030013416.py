import numpy as np
import re

from music21 import *

siev = '((3@2)&(3@1))&(2@1)'

numbers = [int(s) for s in re.findall(r'\d+', siev)]
unique_numbers = list(set(numbers))
prod = np.prod(unique_numbers)

a = sieve.Sieve(siev)
a.setZRange(0, prod)


print(prod)

#https://stackoverflow.com/questions/4289331/how-to-extract-numbers-from-a-string-in-python