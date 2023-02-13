def from_roman(roman_numeral):
    roman_map = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
    }

    decimal_number = 0
    i = 0
    while i < len(roman_numeral):
        if i+1 < len(roman_numeral) and roman_numeral[i:i+2] in roman_map:
            decimal_number += roman_map[roman_numeral[i:i+2]]
            i += 2
        else:
            decimal_number += roman_map[roman_numeral[i]]
            i += 1
    return decimal_number
roman_numeral=input("enter the roman number=")
print(from_roman(roman_numeral))
