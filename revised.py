import os
import time


def get_file_name(filename):
    dot = filename.find(".")
    name = filename[0:dot]
    return name

##############################


def get_content(filename):
    with open(file_name, "r") as txt_file:
        return [item.strip().replace('.', '') for item in txt_file.readlines()]


file_name = 'domains.txt'
print(get_file_name(file_name), get_content(file_name))

#############################################


def get_content(filename):
    with open(file_name, "r") as txt_file:
        return [i.split('\t')[1] for i in txt_file.readlines()]


file_name = 'names.txt'
print(get_file_name(file_name), get_content(file_name))


############################################

def get_date_list(filename):
    with open(file_name, "r") as txt_file:
        return [i.strip().split(' - ')[0] for i in txt_file.readlines() if i[:1].isdigit()]


def convert_date(original_date):
    day, month, year = original_date.split()
    day = day[:-2]
    date_without_suffix = " ".join([day, month, year])
    input_date = time.strptime(date_without_suffix, '%d %B %Y')
    output_date = time.strftime("%d/%m/%Y", input_date)
    return output_date


def convert_date_list(convert_d):
    return [convert_date(convert_d[i]) for i in range(0, len(convert_d))]


def create_dict(first, second):
    my_dict = [{"date_original": first[i], "date_modified": second[i]} for i in range(0, len(first))]
    return my_dict


file_name = 'authors.txt'
date_original = get_date_list(file_name)
date_modified = convert_date_list(date_original)
dict_list = create_dict(date_original, date_modified)
print(get_file_name(file_name), dict_list)

