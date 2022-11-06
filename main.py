from functions import make_csv_list, record_csv, merge_doubles

if __name__ == '__main__':
    contact_list = make_csv_list('phonebook_raw.csv')
    headers = contact_list.pop(0)

    res = merge_doubles(contact_list)
    record_csv('fixed_phonebook', headers, res)
