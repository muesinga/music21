from music21 import *

a = sieve.Sieve('2@0', 200500)
# a.setZRange(0, 200)
print(a.segment())