
cook_book_dict = {}
keys = ['ingredient_name', 'quantity', 'measure']  # список ключей для каждого ингредиента

with open('cook_book.txt') as text:
    lines = []

    for line in text:  # итерируем File object
        line = line.strip()
        if line:
            lines.append(line)  # в список линий добавляем только линии с буквами
        continue

    lines = iter(lines)  # получаем итератор, который выдает последовательные значения из итерируемого списка lines

    for dish in lines:  # в этой линии содержится название блюда - key для cook_book_dict
        cook_book_dict[dish] = []
        number_of_ingredients = next(lines)  # получаем следующее значение из итератора - кол-во ингредиентов блюда
        for line in range(int(number_of_ingredients)):
            ingr_line = next(lines)  # следующее значение - линия ингредиента
            ingredient = ingr_line.split(' | ')  # разбиваем строку по разделителю символу ' | '
            ingr_zp = zip(keys, ingredient)  # создаем кортежи из значений списка keys и списка ingredient
            ingr_dict = {k: v for (k, v) in ingr_zp}  # создаем dict для текущего ингредиента
            cook_book_dict[dish].append(ingr_dict)  # собираем словари ингредиентов в общий словарь
        continue  # переходим к следующему dish



    def get_shop_list_by_dishes(dishes, person_count):
        shop_list_by_dishes = {}
        ingredient = {}

        for dish in dishes:

            for key in cook_book_dict.keys():

                if key == dish:
                    ingr_list = cook_book_dict[dish]

                    for value in ingr_list:
                        name = value['ingredient_name']
                        measure = value['measure']
                        quantity = int(value['quantity']) * person_count
                        ingredient = {'measure': measure, 'quantity': quantity}

                        if name not in shop_list_by_dishes.keys():
                            shop_list_by_dishes[name] = ingredient
                        else:
                            shop_list_by_dishes[name]['quantity'] += ingredient['quantity']

        print(shop_list_by_dishes)

    get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)



