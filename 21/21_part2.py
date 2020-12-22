with open("input.txt") as f:
    foods = f.read().split("\n")

food_map = dict()
all_ingredients = []

for food in foods:
    ingredients, allergens = food.split(" (contains ")
    allergens = allergens[:-1]
    allergens = allergens.split(", ")
    ingredients = ingredients.split(" ")
    for ingredient in ingredients:
        all_ingredients.append(ingredient)

    ingredients = set(ingredients)
    for allergen in allergens:
        try:
            food_map[allergen] = food_map[allergen] & ingredients
        except KeyError:
            food_map[allergen] = ingredients

finished = False
correct_list = []
while not finished:
    finished = True
    for key,value in food_map.items():
        if len(value) == 1:
            ingredient = value.pop()
            correct_list.append((key,ingredient))
            finished = False
            for value in food_map.values():
                try:
                    value.remove(ingredient)
                except KeyError:
                    pass
final = sorted(correct_list, key= lambda x: x[0])
for item in final:
    print(item[1],end=",")
