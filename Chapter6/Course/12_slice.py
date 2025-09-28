my_list = [1, 2, 3, 4, 5]
new_list = my_list[1:4]
print(new_list)

my_tuple = (1, 2, 3, 4, 5)
new_tuple1 = my_tuple[1:]
print(new_tuple1)
new_tuple2 = my_tuple[:4]
print(new_tuple2)
new_tuple3 = my_tuple[:]
print(new_tuple3)

my_list2 = [1, 2, 3, 4, 5]
new_list2 = my_list2[::2]
print(new_list2)

my_str = "12345"
new_str1 = my_str[1:4]
print(new_str1)
new_str2 = my_str[:3:2]
print(new_str2)
new_str3 = my_str[::-1]
print(new_str3)
