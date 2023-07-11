recipes_list = []
ingredients_list = []


def take_recipe():
    name = input("Name of the recipe: ")
    cooking_time = int(input("Cooking time in minutes: "))
    ingredients = input("Enter the ingredients for this recipe: ").split()
    recipe = {
      "name": name, 
      "cooking_time": cooking_time,
      "ingredients": ingredients
    }
    return recipe


n = int(input("How many recipes would you like to enter? "))


for i in range(n):
  recipe = take_recipe()
  for ingredient in recipe["ingredients"]:
    if ingredient not in ingredients_list:
      ingredients_list.append(ingredient)
  recipes_list.append(recipe)


for recipe in recipes_list:
    if (recipe["cooking_time"]) < 10 and len(recipe["ingredients"]) < 4:
      difficulty = "easy"
    elif (recipe["cooking_time"]) < 10 and len(recipe["ingredients"]) >= 4:
      difficulty = "medium"
    elif (recipe["cooking_time"]) >= 10 and len(recipe["ingredients"]) < 4:
      difficulty = "intermediate"
    elif (recipe["cooking_time"]) >= 10 and len(recipe["ingredients"]) >= 4:
      difficulty = "hard"


    print(" ")
    print("Recipe: ", recipe["name"])
    print("Cooking Time in minutes: ", recipe["cooking_time"])
    print("Ingredients: ")
    for ingredient in recipe["ingredients"]:
        print(ingredient)
    print("Difficulty Level: ", difficulty)
    print(" ")


print("Ingredients Avaialable Across All Recipes")
print("-----------------------------------------")

ingredients_list.sort()

for ingredient in ingredients_list:
  print(ingredient)
