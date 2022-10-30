from music21 import *


sieve = '((3@2)&(3@1))&(2@1)'
a = sieve.Sieve('((3@2)&(3@1))&(2@1)')

a.setZRange(0, 1000)
print(a.segment(segmentFormat='binary'))

#find periodicity by finding lowest common demonator of all modulo