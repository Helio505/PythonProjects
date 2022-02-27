operation_choice = str(input("radians to degrees, or degrees to radians? rd/dr"))

if operation_choice == "rd":
    radian_value = float(input("Put the radian value here: "))
    final_result = radian_value * 57.29
    print(final_result)

if operation_choice == "dr":
    degree_value = float(input("Put the degree value here: "))
    final_result = degree_value / 57.29
    print(final_result)
