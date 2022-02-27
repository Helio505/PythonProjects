import math
import sys

operation_choice = str(input("Radians to Degrees, or Degrees to Radians? rd/dr: "))
if operation_choice != ("rd" or "dr"):
    print("Invalid choice")
    sys.exit()

if operation_choice == "rd":
    radian_value = float(input("Put the radian value here: "))
    rad_to_deg_calc = math.degrees(radian_value)
    print(rad_to_deg_calc)

if operation_choice == "dr":
    degree_value = float(input("Put the degree value here: "))
    deg_to_rad_calc = math.degrees(degree_value)
    print(deg_to_rad_calc)
