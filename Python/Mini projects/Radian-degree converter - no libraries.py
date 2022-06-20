"""
    -- Radian-degree converter - no libraries --
    basic, imprecise, conversion with no libraries.
"""

operation_choice = str(input("radians to degrees, or degrees to radians? rd/dr:"))
PI = 3.1415926535

if operation_choice == "rd":
    radian_value = float(input("Put the radian value here: "))
    final_result = (radian_value * 180)/PI
    print(final_result)
elif operation_choice == "dr":
    degree_value = float(input("Put the degree value here: "))
    final_result = (degree_value * PI)/180
    print(final_result)
else:
    print("invalid input")
