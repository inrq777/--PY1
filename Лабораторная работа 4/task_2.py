def get_count_char(str_):
    # TODO посчитать количество каждой буквы в строке в аргументе str_
    count_char_dict = {}
    for sumbol in str_.lower():
        if sumbol.isalpha():
            if sumbol in count_char_dict:
                count_char_dict[sumbol] += 1
            else:
                count_char_dict[sumbol] = 1
    return count_char_dict

def percent_char(count_char_dict):
    i = 0
    percent_dict = {}
    for char in count_char_dict:
        i += count_char_dict.get(char) #общее количество букв
    #print(i)
    for char in count_char_dict:
        percent_dict[char] = round((count_char_dict.get(char)/i)*100, 2)
    #проверка, что сумма процентов равна 100
    check = 0
    for char in percent_dict:
        check += percent_dict.get(char)
    #print(round(check, 1))
    return percent_dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
#print(percent_char(get_count_char(main_str)))
