#!/usr/bin/python3

import random
import sys

major_triads = {'C': 'CEG', 'D': 'DF#A', 'E': 'EG#B', 'F': 'FAC', 'G': 'GBD', 'A': 'AC#E', 'B': 'BD#F#'}
minor_triads = {'Cm': 'CEbG', 'Dm': 'DFA', 'Em': 'EGB', 'Fm': 'FAbC', 'Gm': 'GBbD', 'Am': 'ACE', 'Bm': 'BDF#'}
all_triads = {**major_triads, **minor_triads}

# B# and E# are some kind of rule in chords construction

semitones_sarps = ['C', 'C#', 'D', 'D#', 'E', 'E#', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'B#']
semitones_flat = ['C', 'Cb', 'D', 'Db', 'E', 'Eb', 'F', 'Fb', 'G', 'Gb', 'A', 'Ab', 'B', 'Bb']


# chords_minor
# chords_major
# chords_sus2
# chords_sus2

# semitones_b_sharps = []
# semitones_b_flat

class Chord:
    pass


def chord_by_note():
    pass


def get_answer(notes_dict):
    random_chord = random.choice(list(notes_dict))
    answer = input("Enter triads in chord {} : ".format(random_chord))
    if answer.upper() == notes_dict.get(random_chord):
        return 'Y\'re right'
    else:
        return 'Nope. It is {} '.format(notes_dict.get(random_chord))


def main():
    try:
        while True:
            print(get_answer(all_triads))
    except KeyboardInterrupt:
        print("Exiting")
        sys.exit(0)


if __name__ == "__main__":
    main()
