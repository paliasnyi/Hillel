import os
from time import strptime

os.chdir('/home/vlad/Python/')  # захожу в необходимую папку и подпапку
path = 'os'

#############################################


def get_file_name(filename):
    dot = filename.find(".")
    name = filename[0:dot]
    return name


def get_content(filename):
    path_filename = os.path.join(path, file_name)
    dot = filename.find(".")
    name = filename[0:dot]
    with open(path_filename, "r") as txt_file:
        line_strip = [line.strip() for line in txt_file.readlines()]
        now = [item.replace('.', '') for item in line_strip]
    return now


file_name = 'domains.txt'
print(get_file_name(file_name), get_content(file_name))

#############################################


def get_content(filename):
    path_filename = os.path.join(path, file_name)
    with open(path_filename, "r") as txt_file:
        content = txt_file.readlines()
        tabs = [i.split('\t')[1] for i in content]
    return tabs


file_name = 'names.txt'
print(get_file_name(file_name), get_content(file_name))


############################################

def get_file_name(filename):
    dot = filename.find(".")
    name = filename[0:dot]
    return name


def get_date(filename):
    path_filename = os.path.join(path, file_name)
    with open(path_filename, "r") as txt_file:
        content = [line.strip() for line in txt_file.readlines()]
        date = [i.split(' - ')[0] for i in content if i[:1].isdigit()]
    return date


def convert_day(date):
    day_list = [i.split(' ')[0] for i in date]
    day_num = [i[:2] if i[:2].isdigit() else i[0] for i in day_list]
    day = ['0' + i if int(i) <= 9 else i for i in day_num]
    return day


def convert_month(date):
    month_list = [i.split(' ')[1] for i in date]
    month_num = [strptime(i, '%B').tm_mon for i in month_list]
    month = ['0' + str(i) if i <= 9 else i for i in month_num]
    return month


def get_year(date):
    year = [i.split(' ')[2] for i in date]
    return year


def convert_date(original):
    day = convert_day(date_original)
    month = convert_month(date_original)
    year = get_year(date_original)
    new_date = [str(day[i]) + '/' + str(month[i]) + '/' + str(year[i]) for i in range(0, len(original))]
    return new_date


def create_dict(first, second):
    my_dict = [{"date_original": first[i], "date_modified": second[i]} for i in range(0, len(first))]
    return my_dict


file_name = 'authors.txt'
date_original = get_date(file_name)
date_modified = convert_date(date_original)
dict_list = create_dict(date_original, date_modified)
print(get_file_name(file_name), dict_list)

