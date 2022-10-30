from music21 import *

a = sieve.Sieve('(3@0)&(2@0)')
a.setZRange(0, 200)
print(a.segment(segmentFormat='binary'))

#repeating 