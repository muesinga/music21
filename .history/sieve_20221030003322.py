from music21 import *

a = sieve.Sieve('(3@0)&(2@0)')
a.setZRange(0, 6)
print(a.segment(segmentFormat='binary'))

#find periodicity by finding lowest common demonator of all modulo