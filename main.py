value = int(input('Введите число: '))

##############################
new_value = value / 2 if value < 100 else value * (-1)
print(new_value)

##############################
new_value = 1 if value < 100 else 0
print(new_value)

##############################
new_value = True if value < 100 else False
print(new_value)

##############################
my_str = input('Введите любые символы: ')

##############################
my_list = my_str[1::2]
print(my_list)

####Сделал на нечетных местах#####
print(my_str[0::2])

####### Один вариант сделал через if #############
if len(my_str) < 5:
    print(my_str * 2)
else:
    print(my_str)

######а этот тернарный :) ###########
my_list = print( my_str + my_str[::-1]) if len(my_str) < 5 else print(my_str)
