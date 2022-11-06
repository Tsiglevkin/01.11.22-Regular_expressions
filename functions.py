import csv
from tqdm import tqdm
# from time import sleep
import re


def make_csv_list(some_csv):
    with open(f'{some_csv}', encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=',')
        contact_list = list(rows)
        return contact_list


def record_csv(csv_name, headers, some_list):
    with open(f'{csv_name}.csv', 'w', encoding='utf-8', newline='') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerow(headers)
        datawriter.writerows(some_list)
        print('File is recorded.')


def _fix_name(some_list):
    """You can put lastname, surname and firstname to correct column. You'll get a list"""
    for row in some_list:
        temp = ' '.join(row[:3])
        temp_list = temp.split()
        for i in range(len(temp_list)):
            row[i] = temp_list[i]
    return some_list


def _fixed_phones(some_list):
    """Make an impression of phone numbers correct. You'll get a list"""
    pattern = r'(\+7|8)\D*(495)\D*(\d+)\D*(\d{2})\D*(\d{2})(\W*( доб.\s*\d+)\)*)?'
    new_pattern = r'+7(\2)\3-\4-\5\7'
    for row in some_list:
        res = re.sub(pattern, new_pattern, row[-2])
        row[-2] = res
    return some_list


def merge_doubles(some_list):
    """Fix full name, fix phones, merge the doubles. You'll get a list"""
    temp_list = _fixed_phones(some_list)
    work_list = _fix_name(temp_list)
    for origin_row in tqdm(work_list, desc='Проверяем дубли', unit=' запись'):
        # sleep(0.1)
        for check_row in work_list:
            while len(check_row) > 7:
                del check_row[-1]
            if origin_row != check_row and origin_row[0] == check_row[0] and origin_row[1] == check_row[1]:
                for i in range(len(origin_row)):
                    if origin_row[i] == '':
                        origin_row[i] = check_row[i]
                work_list.remove(check_row)

    return work_list

