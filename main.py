import os
import os.path

def acounting(file: str) -> int:
    with open(file, 'rt', encoding='utf-8') as f:
        return sum(1 for _ in f)

# Задача 1
with open('ingridients.txt', encoding='utf-8') as file:
    cook_book = {}
    while True:
        recipe_name = file.readline().strip()
        if not recipe_name:
            break
        ingredient_count = int(file.readline().strip())
        ingredients = []
        for _ in range(ingredient_count):
            ingredient_data = file.readline().strip().split(' | ')
            ingredient_name, quantity, measure = ingredient_data
            ingredients.append({'Ingredient': ingredient_name, 'Quantity': int(quantity), 'Measure': measure})
        file.readline()  # Пропускаем разделительную строку
        cook_book[recipe_name] = ingredients

# Задача 2
def get_shop_list_by_dishes(person_count, dishes):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient['Ingredient'] in result:
                    result[ingredient['Ingredient']]['Quantity'] += ingredient['Quantity'] * person_count
                else:
                    result[ingredient['Ingredient']] = {'Measure': ingredient['Measure'], 'Quantity': ingredient['Quantity'] * person_count}
        else:
            print(f'Блюдо "{dish}" не найдено в кулинарной книге')
    print(result)

get_shop_list_by_dishes(2, ['Запеченный картофель', 'Омлет'])

# Задача 3
def rerecord(file_for_writing: str, base_path, location):
    files = []
    for i in list(os.listdir(os.path.join(base_path, location))):
        files.append([acounting(os.path.join(base_path, location, i)), os.path.join(base_path, location, i), i])
    for file_from_list in sorted(files):
        opening_files = open(file_for_writing, 'a')
        opening_files.write(f'{file_from_list[2]}\n')
        opening_files.write(f'{file_from_list[0]}\n')
        with open(file_from_list[1], 'r', encoding='utf-8', errors='ignore') as file:
            counting = 1
            for line in file:
                opening_files.write(f'Строка № {counting} в файле {file_from_list[2]} : {line}')
                counting += 1
        opening_files.write(f'\n')
        opening_files.close()


file_for_writing = os.path.abspath('/Users/nikita/Desktop/txt/new/4.txt')
base_path = os.getcwd()
location = os.path.abspath('/Users/nikita/Desktop/txt/new')
rerecord(file_for_writing, base_path, location)