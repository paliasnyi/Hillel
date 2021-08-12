## 7 - revised ###############
def find_same_letter(my_str, my_str_2):
    str_list = [i for i in my_str if my_str.count(i) == 1]
    str_list_2 = [j for j in my_str_2 if my_str_2.count(j) == 1]
    new_list = [k for k in str_list if k in str_list_2]
    return new_list


print(find_same_letter('aaaaaabc', 'abcccccc'))

## 11 d - revised ###############

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
dict_list_d2 = {i: [my_dict_1[i], my_dict_2[i]] for i in dict_list_1 if i in dict_list_2} #values included in list
dict_list_d3 = {**dict_list_d, **dict_list_d2}
print("d)", dict_list_d3)

