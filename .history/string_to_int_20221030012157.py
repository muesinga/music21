import re

numbers = [int(s) for s in re.findall(r'\d+', '((3@2)&(3@1))&(2@1)')]

uniquelist(set(numbers))

#https://stackoverflow.com/questions/4289331/how-to-extract-numbers-from-a-string-in-python