from pprint import pprint

with open('recipes.txt', encoding='utf-8') as a:
    cook_book = {}
    for line in a:
        dish = line.strip()
        ingredients_count_in_dish = int(a.readline().strip())
        ingredients = []
        for _ in range(ingredients_count_in_dish):
            ing = a.readline().strip()
            ingredient_name, count, unit, = ing.split(' | ')
            ingredients.append(
                {'ingredient_name': ingredient_name,
                 'quantity': count,
                 'measure': unit}
            )
        cook_book[dish] = ingredients
        a.readline()

# pprint(cook_book, sort_dicts=False, width=100)


def get_shop_list_by_dishes(dishes, person_count):
    platter = []
    all_ingredients = {}
    for dish in cook_book.keys():
        if dish in dishes:
            platter.append(dish)

    for dish in platter:
        for ingredient in cook_book[dish]:
            count_on_person = {}
            for key, value in ingredient.items():
                if key == 'ingredient_name':
                    continue
                else:
                    if value.isdigit() is True:
                        value = int(value) * person_count
                    count_on_person[key] = value

            all_ingredients[ingredient['ingredient_name']] = count_on_person

    pprint(all_ingredients)
    return

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 4)
