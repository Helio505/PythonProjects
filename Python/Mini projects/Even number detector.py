"""
    -- Even number detector --
    Input number and it will analyse if it's even or not.
"""

input_number = int(input("Put the number here: "))

if (input_number % 2) == 0:
    print(f"{input_number} Is even")
else:
    print(f"{input_number} Is odd")
