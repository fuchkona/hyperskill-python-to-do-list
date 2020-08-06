# use the function blackbox(lst) that is already defined

my_list = [1, 2, 3]

new_list = blackbox(my_list)

print("modifies" if id(my_list) == id(new_list) else "new")
