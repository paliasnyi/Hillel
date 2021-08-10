my_int = str(54678096976003939304000)
print(f'Число {my_int}:')
###########################

my_count = my_int.count("0")
print(f"Я нашел {my_count} нулей")
###########################

r_int = int(my_int[::-1])
number = len(my_int) - len(str(r_int))
print(f"{number} нуля в конце")
###########################

my_list_1 = [1, 2, 3, 4, 5]
my_list_2 = [6, 7, 8, 9, 10]
result = my_list_1[::2] + my_list_2[1::2]
print(result)
###########################

my_list = [4, 7, 8, 9, 10]
new_l = my_list.copy()
new_list = new_l[1::] + my_list[0:1]
print(new_list)
###########################

my_list = [4, 7, 8, 9, 10]
value = my_list.pop(0)
my_list.append(value)
print(my_list)
###########################

my_str = '66 69 73'
my_split = my_str.split()
my_split = [int(i) for i in my_split]
value = sum(my_split)
print(value)
###########################

my_str = 'Python course in Hillel is fun'
l_limit, r_limit = 't', 'n'
l_limit_i, r_limit_i = my_str.index(l_limit, 0), my_str.index(r_limit, -1)
sub_str = my_str[l_limit_i: r_limit_i]
print(sub_str)

###########################
my_str = 'Hillel'
my_list = []
for letter in range(0, len(my_str), 2):
    if letter < len(my_str) - 1:
        my_list.append(my_str[letter] + my_str[letter + 1])
    else:
        my_list.append(my_str[letter] + '_')
print(my_list)

###########################

my_list = [1, 2, 4, 4, 2, 8, 8, 4]
new_list = []
for number in my_list[1:-1]:
    if sum(my_list[number - 1: number + 1]) < number:
        new_list.append(number)
print(new_list)

