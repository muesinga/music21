import numpy as np
import re

siev = 

numbers = [int(s) for s in re.findall(r'\d+', )]
unique_numbers = list(set(numbers))


print(unique_numbers)

#https://stackoverflow.com/questions/4289331/how-to-extract-numbers-from-a-string-in-python