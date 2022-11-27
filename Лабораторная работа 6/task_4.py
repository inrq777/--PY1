import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(csv_file, delimiter=',', linefeed='\n') -> list[dict]:

    list_ = []
    list_dict = []
    with open(csv_file) as f:
        for line in f:
            list_.append(line.split(f'{delimiter}'))
    for last_element in list_:
        last_element[-1] = last_element[-1].rstrip(f'{linefeed}')

    headers_list = list_.pop(0)

    for line in list_:
        dict_ = {}
        count = 0
        for element in line:
            dict_.update({headers_list[count]: element})
            count += 1
        list_dict.append(dict_)
    return list_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
