def find_at_least_1(str_1, str_2):
    my_list = [s for s in set(str_1) if str_2.find(s)]
    return my_list


my_str = 'hlksjfdjskdjhfksjdfksajldfhs'
my_str_2 = 'klsfdjhskjdfkasdljfhaksldjhf'
print(find_at_least_1(my_str, my_str_2))

#####################################################

def find_same_letter(my_str, my_str_2):
    str_list = [i for i in set(my_str) if my_str.count(i) == 1]
    str_list_2 = [j for j in set(my_str_2) if my_str_2.count(j) == 1]
    new_list = [k for k in str_list if k in str_list_2]

    return new_list

print(find_same_letter('aaaaaabc', 'abcccccc'))



#####################################################



import random
import string


def create_email(domains, names):
    domain = random.choice(domains)
    name = random.choice(names)
    letters = ''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 7)))
    e_mail = f"{name}.{random.randint(100, 999)}@{letters}.{domain}"
    return e_mail


names = ["python", "javascript", "php", "html", "css"]
domains = ["org", "com", "ua", "gov", "gb", "md"]
e_mail = create_email(domains, names)
print(e_mail)

