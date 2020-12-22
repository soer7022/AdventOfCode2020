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

unsafe_ingredients = set()
for item in food_map.values():
    unsafe_ingredients.update(item)

total = 0
for item in all_ingredients:
    if item not in unsafe_ingredients:
        total += 1

print(total)

