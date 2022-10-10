from music21 import *

note1 = note.Note("C4")
note2 = note.Note("F#4")
note3 = note.Note("B-2")

noteList = [note1, note2, note3]

note1.duration.type = 'half'

stream1 = stream.Stream()

stream1.append(note1)
stream1.append(note2)
stream1.append(note3)

# stream2 = stream.Stream()
# n3 = note.Note('D#5')
# stream2.repeatAppend(n3, 3)
# stream2.show()

stream1.show('midi')