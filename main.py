from pprint import pprint

def create_cook_book(recipes) :
    cook_book = {}
    try:
        with open("recipes.txt", encoding='utf-8') as f:
            lst = [line.strip() for line in f]


        for i, c in enumerate(lst):
            if c.isdigit():
                cook_book[lst[i-1]] = []
                for ingr in lst[i+1:i+int(c)+1]:
                    ingredient_name = ingr.split('|')[0]
                    quantity = int(ingr.split('|')[1])
                    measure = ingr.split('|')[2]

                    cook_book[lst[i - 1]].append({'ingredient_name':ingredient_name,
                                                'quantity':quantity,
                                                'measure':measure})
        return cook_book


    except FileNotFoundError:
        return(f'Файл: {recipes.txt} не найден.')

    except Exception as error:
        return f'Ошибка - {error}'


def get_shop_list_by_dishes(dishes, cooking_book, person_count):
    try:
        for key in dishes:
            if key in cooking_book.keys():
                print(key)

                for value in cooking_book[key]:
                    value['quantity'] *= person_count
                    print(value)
                print()
            else:
                pass
    except AttributeError:
        print('Файл не найден')

print('Задание №1:\n')
pprint(create_cook_book('recipes.txt'))
print('\n' * 2)

print('Задание №2:\n')
get_shop_list_by_dishes(['Омлет', 'Запеченный картофель','Фахитос'],\
                        create_cook_book('recipes.txt'), 2)
