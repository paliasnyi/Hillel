import json
import re


def get_math(filename):
    with open(filename, "r") as json_file:
        new_data = json.load(json_file)
    return new_data


file_name = 'data.json'
mathematics = get_math(file_name)
print('Data sorted by:')
###########################################################


def sort_by_author(data):
    return sorted(data, key=lambda k: k['name'].split()[-1])


by_authors = sort_by_author(mathematics)
print('Authors: ', by_authors)
############################################################


def sort_by_dod(data):
    list_bc = []
    list_ac = []
    for i in data:
        if 'BC' in i['years']:
            list_bc.append(i)
        else:
            list_ac.append(i)
    pattern = r'[0-9]+'
    sorted_bc = sorted(list_bc, key=lambda k: int(re.findall(pattern, k['years'])[-1]),
                       reverse=True)
    sorted_ac = sorted(list_ac, key=lambda k: int(re.findall(pattern, k['years'])[-1]))
    return sorted_bc + sorted_ac


by_date = sort_by_dod(mathematics)
print('Date Of Death: ', by_date)

##################################################################


def sort_by_text_len(data):
    return sorted(data, key=lambda k: len(k['years']))


by_len = sort_by_text_len(mathematics)
print('Text Length: ', by_len)
