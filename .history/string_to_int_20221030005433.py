# a = '((3@2)&(3@1))&(2@1)'

txt = "h3110 23 cat 444.4 rabbit 11 2 dog"

print([int(s) for s in txt.split() if s.isdigit()])
