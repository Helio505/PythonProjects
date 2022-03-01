user_list0 = input("Insert your list here. Just numbers. Like this: 2,3,4,5,6,2.3...etc: ")
user_list1 = user_list0.replace(",", " ")
user_list_formatted = user_list1.split()

# print(f"{user_list0} \n {user_list1} \n {user_list_formatted}")

# This also works:
# user_list = input("Insert your list here. Just numbers. Separated by spaces. Like this: 2 3 4 5 6 2.3 etc: ")
# user_list.split()

sorting_choice = input("Choose the operation (asc, dsc, none): ")

if sorting_choice == "asc":
    user_list_formatted.sort(reverse=False)
    print(user_list_formatted)

if sorting_choice == "dsc":
    user_list_formatted.sort(reverse=True) #the reverse is descending by default
    print(user_list_formatted)

if sorting_choice == "none":
    print(user_list_formatted)
