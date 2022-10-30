from music21 import *

a = sieve.Sieve('(3@2)&2@1')
# a.setZRange(0, 200)
print(a.segment())