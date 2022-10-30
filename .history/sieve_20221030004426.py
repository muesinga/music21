from music21 import *

a = sieve.Sieve('((3@2)&(3@1))&(2@1)')

[int(s) for s in txt.split() if s.isdigit()]

a.setZRange(0, 1000)
print(a.segment(segmentFormat='binary'))

#find periodicity by finding lowest common demonator of all modulo