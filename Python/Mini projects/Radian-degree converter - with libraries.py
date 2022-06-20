"""
    -- Radian-degree converter - more advanced --
    Uses Python's standard libraries.
"""

import math

operation_choice = str(input("Radians to Degrees, or Degrees to Radians? rd/dr: "))

if operation_choice == "rd":
    radian_value = float(input("Put the radian value here: "))
    rad_to_deg_calc = math.degrees(radian_value)
    print(rad_to_deg_calc)
elif operation_choice == "dr":
    degree_value = float(input("Put the degree value here: "))
    deg_to_rad_calc = math.radians(degree_value)
    print(deg_to_rad_calc)
else:
    print("Invalid choice")