#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Morse Code Decoder

"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.
"""
__author__ = 'r-bolling with help from Kenzie Academy Lessons'

from morse_dict import MORSE_2_ASCII


def decode_bits(bits):
    # your code here
    return


def decode_morse(morse):
    # inputs: morse code(string)
    # outputs: translated morse code(string)
    # vars: split morse code(list), returned translated string(string)
    split_morse = morse.split(' ')
    translated_morse = ''
    for count, morse in enumerate(split_morse):
        if morse == '' and count == 0:
            pass
        elif morse == '' and split_morse[count - 1] == '':
            pass
        elif morse == '':
            translated_morse += ' '
        else:
            translated_morse += MORSE_2_ASCII[morse]
    return translated_morse.strip()


if __name__ == '__main__':
    hey_jude_morse = ".... . -.--   .--- ..- -.. ."
    hey_jude_bits = "11001100110011000000110000001111110011001111110011111100000000000000000000011001111110011111100111111000000110011001111110000001111110011001100000011" # noqa

    # Be sure to run all included unit tests, not just this one.
    print("Morse Code decoder test")
    print("Part A:")
    print(f"'{hey_jude_morse}' -> {decode_morse(hey_jude_morse)}")
    print()
    print("Part B:")
    print(f"'{hey_jude_bits}' -> {decode_morse(decode_bits(hey_jude_bits))}")

    print("\nCompleted.")
