"""
    -- Sorting list --
    Sorts inputed list. User can choose between sorting options.
    
    Information:
        asc = ascending order.
        dsc = descending order.
        none = prints the list unchanged.

        list should be int numbers separated by commas, and no spaces.
        This uses Python's sorting modules.
"""

input_list = input("Insert your list here. Just int numbers. Like this: 2,3,42...: ")
input_list = input_list.replace(",", " ")
input_list = input_list.split()

list_formatted = []
for i in input_list:
    i = int(i) # change to float if you want float numbers.
    list_formatted.append(i)

sorting_choice = input("Choose the operation (asc, dsc, none): ")

if sorting_choice == "asc":
    list_formatted.sort(reverse=False)
    print(list_formatted)
elif sorting_choice == "dsc":
    list_formatted.sort(reverse=True)
    print(list_formatted)
elif sorting_choice == "none":
    print(list_formatted)
else:
    print("invalid operation")