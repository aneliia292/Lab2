#1

#функция изменят структуру списка парами
def list_reorder(ref_list):
    #Сохраняем список имен и фамилий в переменные
    names = ref_list[0]
    surnames = ref_list[1]
    result = [[names[i], surnames[i]] for i in range(min(len(names), len(surnames)))]
    #отсортированный список
    return result

# Пример:
ref_list = [['Олег', 'Мария'], ['Баранов', 'Иванова']]
reordered_list = list_reorder(ref_list)
print(reordered_list)

#2
def del_rep(nums):
    # Удаляем дубликаты, преобразуя список во множество (множество не содержит дубликатов)
    unique_nums = set(nums)
    # Сортируем уникальные числа и возвращаем результат как список
    return sorted(list(unique_nums))

# Пример
num = [3,6,2,8,5,8,3,1,0]
result = del_rep(num)
print(result)

#3
def lim_max(nums, limit):
    max_val = 1  # Изначально устанавливаем максимальное значение как 1

    for num in nums:
        if num < limit and num > max_val:
            max_val = num

    return max_val

# Пример
nums = (10,35,40,60,75,95,115)
limit = 90  #ограничение
result = lim_max(nums, limit)
print(result)  #75-максимальный ограниченный символ

#4
def temp_cat(temp):
    #устанавливаем рамки и категории температуры
    if temp < -20:
        return 0  #холодно
    elif temp < 0:
        return 1 #прохладно
    elif temp < 15:
        return 2 #зябко
    elif temp < 25:
        return 3 #тепло
    else:
        return 4 #жфрко

temp = 15
category = temp_cat(temp)
print("Ответ:", category)


#5

import re
def check_phn(phones):
    result = []
    # Удаляем все символы, кроме цифр, чтобы проверить длину номера
    for phone in phones: digits_only = re.sub(r'\D', '', phone)

    if len(digits_only) != 11 or digits_only[0] not in ['7', '8']:
    # Номер не соответствует требованиям
        result.append(-1)
    else:
# Номер соответствует требованиям, форматируем его
        formatted_phone = ('+7(' +
        digits_only[1:4] + ')' +
        digits_only[4:7] + '-' +
        digits_only[7:9] + '-' +
        digits_only[9:])
        result.append(formatted_phone)

    return result

# Пример использования:
phones = ['+25234652345']
result = check_phn(phones)
print("Ответ:", result)
