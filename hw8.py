my_list = ['Alfa', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot']
new_list = []
for i in range(0, len(my_list)):
    if i % 2 == 0:
        new_list.append(my_list[i][::-1])
    else:
        new_list.append(my_list[i])
print(new_list)
###########################

my_list = ['Alfa', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot']
new_list = [my_list[i] for i in range(0, len(my_list)) if my_list[i].lower().startswith('a')]
print(new_list)
###########################

my_list = ['Alfa', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot']
new_list = [my_list[i] for i in range(0, len(my_list)) if my_list[i].lower().find('a') >= 0]
print(new_list)
###########################

my_list = ['654', '7897', 13, 11, '45', 'Foxtrot']
new_list = [i for i in my_list if isinstance(i, str)]
print(new_list)
############################

my_str = 'hlksjfdjskdjhfksjdfksajldfhs'
my_set = list(set(my_str))
print(my_set)
############################

my_str = 'hlksjfdjskdjhfksjdfksajldfhs'
my_str_2 = 'klsfdjhskjdfkasdljfhaksldjhf'
my_set = set(my_str) & set(my_str_2) #### or my_set = [i for i in set(my_str) if i in set(my_str_2)]
print(my_set)
###########################

my_set = set(my_str)
my_set_2 = str(set(my_str_2))
my_list = sorted([s for s in my_set if my_set_2.find(s) >= 0])
print(my_list)
###########################

boogeyman = { 'Name': 'John', 'Surname': 'Wick', 'Age': 33,
             'Place': {'Country': 'USA', 'City': 'New York', 'Street': 'Main Street'},
             'Occupation': {'Available': 'Yes', 'Position': 'Killer'}
}
print(boogeyman['Place']['City'])

###########################

from random import randint as ran

my_cake = {'Shell': {'flour': ran(0, 250), 'milk': ran(0, 250), 'butter': ran(0, 250), 'eggs': ran(0, 250)},
           'Cream': {'sugar': ran(0, 250), 'butter': ran(0, 250), 'vanilla': ran(0, 250), 'sour cream': ran(0, 250)},
           'Glaze': {'cocoa': ran(0, 250), 'sugar': ran(0, 250), 'butter': ran(0, 250)}
           }
###########################

persons = [{"name": "Robert", "age": 18},
           {"name": "Bruce", "age": 44},
           {"name": "Kim", "age": 33},
          {"name": "Arthur", "age": 18}]

age_list = [person['age'] for person in persons]
min_age = [person['name']for person in persons if person['age'] == min(age_list)]
print(f'a) Youngest: {min_age}, age: {min(age_list)}')

names = [person['name'] for person in persons]
max_length = [name for name in names if len(name) == len(max(names))]
print(f'b) Longest name: {max_length}')

avrg_age = sum(age for age in age_list) // len(age_list)
print(f'c) Average age of persons in list: {avrg_age}')

#############################

my_dict_1 = {'One': 211, 'Two': 2212, 'Three': 53}
my_dict_2 = {'Two': 12111, 'One': 2332, 'Five': 4444}

dict_list_1 = [key for key in my_dict_1]
dict_list_2 = [key for key in my_dict_2]
dict_list_a = [i for i in dict_list_1 if i in dict_list_2]
print("a)", dict_list_a)

list_b = [i for i in dict_list_1 if i not in dict_list_2]
print("b)", list_b)

dict_list_c = {i: my_dict_1[i] for i in dict_list_1 if i not in dict_list_2}
print("c)", dict_list_c)

dict_list_d = {i: my_dict_1[i] for i in dict_list_1 if i not in dict_list_2}
dict_list_d2 = {i: my_dict_2[i] for i in dict_list_1 if i in dict_list_2}
dict_list_d3 = {**dict_list_d, **dict_list_d2}
print("d)", dict_list_d3)

