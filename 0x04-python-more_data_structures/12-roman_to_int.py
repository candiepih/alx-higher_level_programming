#!/usr/bin/python3
romans = {
    "I": 1,
    "IV": 4,
    "V": 5,
    "IX": 9,
    "X": 10,
    "XL": 40,
    "L": 50,
    "XC": 90,
    "C": 100,
    "CD": 400,
    "D": 500,
    "CM": 900,
    "M": 1000
}


def number_to_subtract(char, prev_char):
    if (char == "X" or char == "V") and prev_char == "I":
        return (romans[prev_char] + 1)
    elif (char == "L" or char == "C") and prev_char == "X":
        return (romans[prev_char] + 10)
    elif (char == "D" or char == "M") and prev_char == "C":
        return (romans[prev_char] + 100)
    else:
        return 0


def roman_to_int(roman_string):
    if (type(roman_string)) != str or (roman_string is None):
        return 0
    roman_string = roman_string.upper()
    sum = 0
    for index, c in enumerate(roman_string):
        if c not in romans:
            return 0
        sum += romans[c]
        prev_char = roman_string[index - 1] if index - 1 >= 0 else None
        sum -= number_to_subtract(c,  prev_char)
    return sum
