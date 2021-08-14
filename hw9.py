def reverse_second(list):
    new_list = [list[i][::-1] if not i % 2 else list[i] for i in range(0, len(list))]
    return new_list


my_list = ['Alfa', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot']
print(reverse_second(my_list))
###############################


def find_first(list, letter):
    new_list = [list[i] for i in range(0, len(list)) if list[i].lower().startswith(letter)]
    return new_list


my_list = ['Alfa', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot']
start_with = 'a'
print(find_first(my_list, start_with))

################################


def find_any_a(list, letter):
    new_list = [list[i] for i in range(0, len(list)) if list[i].lower().find(letter) >= 0]
    return new_list


my_list = ['Alfa', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot']
any_letter = 'a'
print(find_any_a(list, any_letter))

################################


def find_str(str1ng):
    new_list = [i for i in str1ng if isinstance(i, str)]
    return new_list


my_list = ['654', '7897', 13, 11, '45', 'Foxtrot']
print(find_str(my_list))

################################



def find_unique(letter):
    my_set = list(set(my_str))
    return my_set

my_str = 'hlksjfdjskdjhfksjdfksajldfhs'
print(find_unique(letter))

################################


def find_at_least_1(str_1, str_2):
    my_list = sorted([s for s in str_1 if str_2.find(s) >= 0])
    return my_list


my_str = 'hlksjfdjskdjhfksjdfksajldfhs'
my_str_2 = 'klsfdjhskjdfkasdljfhaksldjhf'
print(find_at_least_1(my_str, my_str_2))

#################################


def find_same_letter(my_str, my_str_2):
    str_list = [i for i in my_str if my_str.count(i) == 1]
    str_list_2 = [j for j in my_str_2 if my_str_2.count(j) == 1]
    new_list = [k for k in str_list if k in str_list_2]
    print(new_list)
    return new_list


find_same_letter('aaaaaabc', 'abcccccc')

###############################

import random
import string


def create_email(domains, names):
    domain = random.choice(domains)
    name = random.choice(names)
    letters = ''.join(random.choices(string.ascii_lowercase, k=6))
    e_mail = f"{name}.{random.randint(100, 999)}@{letters}.{domain}"
    return e_mail


names = ["python", "javascript", "php", "html", "css"]
domains = ["org", "com", "ua", "gov", "gb", "md"]
e_mail = create_email(domains, names)
print(e_mail)

