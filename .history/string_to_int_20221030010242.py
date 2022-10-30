import re

print(int(s) for s inre.findall(r'\d+', '((3@2)&(3@1))&(2@1)'))

#https://stackoverflow.com/questions/4289331/how-to-extract-numbers-from-a-string-in-python