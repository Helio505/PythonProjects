## Even number detector
# Input number and it will analyse if it's even or not.
import math

input_number = int(input("Put the number here: "))

# Remainder of (input_number / 2)
if math.remainder(input_number, 2) == 0:
    print("Is even")
else:
    print("Isn't even")
