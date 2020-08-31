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


def find_time_multiplier(stripped_bits):
    zeros = '0'
    ones = '1'
    for bit in enumerate(stripped_bits):
        if stripped_bits.find(zeros + '0') == -1:
            break
        else:
            zeros += '0'
    for bit in enumerate(stripped_bits):
        if stripped_bits.find(ones + '1') == -1:
            break
        else:
            ones += '1'
    if len(ones) == len(zeros):
        time = len(ones)
    elif len(ones) < len(zeros):
        if len(zeros) % 7 == 0:
            time = len(zeros) // 7
        elif len(zeros) % 3 == 0:
            time = len(zeros) // 3
    elif len(ones) > len(zeros):
        if len(ones) % 7 == 0:
            time = len(ones) // 7
        elif len(ones) % 3 == 0:
            time = len(ones) // 3
    return time


def decode_bits(bits):
    # inputs: binary time input(string)
    # outputs: morse code(string)
    # vars: time multiplier(int), binary input "bits"(string),
    #   returned translated string(string)
    # CONSIDER creating more functions to help be concise
    stripped_bits = bits.strip('0')
    if stripped_bits.find('0') == -1:
        return '.'
    one_count = 0
    zero_count = 0
    morse = ''
    time = find_time_multiplier(stripped_bits)
    for counter, bit in enumerate(stripped_bits):
        if bit == '1':
            one_count += 1
        if bit == '0':
            zero_count += 1
        if bit == '1' and zero_count > 0 and zero_count // 7 == time:
            morse += '   '
        elif bit == '1' and zero_count > 0 and zero_count // 3 == time:
            morse += ' '
        if one_count > 0 and one_count // 3 == time:
            if bit == '0' or counter == len(stripped_bits) - 1:
                morse += '-'
        elif one_count > 0 and one_count // 1 == time:
            if bit == '0' or counter == len(stripped_bits) - 1:
                morse += '.'
        if bit == '1':
            zero_count = 0
        if bit == '0':
            one_count = 0
    return morse


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
