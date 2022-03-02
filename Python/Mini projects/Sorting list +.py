## Sorting list +
# asc = ascending order
# dsc = descending order
# none = prints the list unchanged

user_list_0 = input("Insert your list here. Just numbers, \
and just integers.\nLike this: 2,3,4,5,6,2.3 or separated by spaces: ")

user_list_1 = user_list_0.replace(",", " ")
user_list_2 = user_list_1.split()
# print(f"{user_list_0} \n{user_list_1} \n{user_list_2}")

sorting_choice = input("Choose the operation (asc, dsc, none): ")
    
user_list_formatted_final = []
for x in user_list_2:
    user_list_formatted_final.append(int(x))

if sorting_choice == "asc":
    user_list_formatted_final.sort(reverse=False)
    print(user_list_formatted_final)

if sorting_choice == "dsc":
    user_list_formatted_final.sort(reverse=True) #the reverse is descending by default
    print(user_list_formatted_final)

if sorting_choice == "none":
    print(user_list_formatted_final)
