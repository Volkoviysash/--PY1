def get_count_char(str_):
    number_of_characters = {}
    str_ = str_.lower()
    for char_ in str_:
        # Для каждого символа в строке
        if char_.isalpha():
            if char_ not in number_of_characters: #Если символ встретился впервые - его еще нет в словаре
                number_of_characters[char_] = 1
            else: #иначе в словаре символ уже есть, тогда к счетчику добавить 1
                number_of_characters[char_] += 1
    return number_of_characters


def get_percent_count_char(number_of_characters):
    percent_count_char = {}
    total_characters = sum(number_of_characters.values()) #сколько всего символов в строке
    for char_ in number_of_characters:
        # Разделить его значение на сумму всех значений всех ключей словаря, умножить на 100% и округлить до целых
        percent_count_char[char_] = round(number_of_characters[char_] / total_characters * 100)
    
    #Доп.задание
    delta = 100 - sum(percent_count_char.values()) #нахожу отклонение суммы всех весов от 100%
    percent_count_char[list(percent_count_char.keys())[0]] += delta #к первому значению добавим дельту    
    #Смотреть комментарий на github

    return percent_count_char

main_str = "Данное предложение будет разбиваться на отдельные слова. В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!"

print(get_count_char(main_str))
#print(get_percent_count_char(get_count_char(main_str)))
