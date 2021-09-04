import requests
import csv


def get_raw_quote(index):
    params = {"method": "getQuote", "format": "json", "key": index}
    r = requests.get('http://api.forismatic.com/api/1.0/', params=params)
    return r.json()


def get_quotes(number):
    return [get_raw_quote(i) for i in range(number)
            if get_raw_quote(i)['quoteAuthor'] != '']


quotes = get_quotes(6)

############################################################################


def create_sorted_dict(quotes_list):
    sorted_quotes = sorted(quotes_list, key=lambda k: k['quoteAuthor'])
    sorted_dict = [{'Author': i['quoteAuthor'], 'Quote': i['quoteText'],
                   'URL': i['quoteLink']} for i in sorted_quotes]
    return sorted_dict


def write_csv(data):
    fieldnames = ["Author", "Quote", "URL"]
    with open('quotes.csv', "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


my_dict = create_sorted_dict(quotes)
write_csv(my_dict)

