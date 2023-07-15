import pickle

def take_recipe():
    name = input("Name of the recipe: ")
    cooking_time = int(input("Cooking time in minutes: "))
    ingredients = input("Enter the ingredients for this recipe: ").split()
    recipe = {
      "name": name, 
      "cooking_time": cooking_time,
      "ingredients": ingredients
    }
    difficulty = calc_difficulty(recipe)
    recipe["difficulty"] = difficulty
    return recipe

def calc_difficulty(recipe):
    if (recipe["cooking_time"]) < 10 and len(recipe["ingredients"]) < 4:
      difficulty = "easy"
    elif (recipe["cooking_time"]) < 10 and len(recipe["ingredients"]) >= 4:
      difficulty = "medium"
    elif (recipe["cooking_time"]) >= 10 and len(recipe["ingredients"]) < 4:
      difficulty = "intermediate"
    elif (recipe["cooking_time"]) >= 10 and len(recipe["ingredients"]) >= 4:
      difficulty = "hard"
    return difficulty

recipes_list = []
all_ingredients = []

filename = input("Enter the filename where you have stored your recipes: ")
try:
    recipe_name = open(filename, 'r')
    data = pickle.load(recipe_name)
except FileNotFoundError:
    print("File doesn't exist. New file being created.")
    data = {"recipes_list": [], "all_ingredients": []}
except: 
    print("Unexpected error. New file being created.")
    data = {"recipes_list": [], "all_ingredients": []}
else:
    recipe_name.close()
finally: 
    recipes_list = data["recipes_list"]
    all_ingredients = data["all_ingredients"]


n = int(input("How many recipes would you like to enter? "))

for i in range(n):
  recipe = take_recipe()
  for ingredient in recipe["ingredients"]:
    if ingredient not in all_ingredients:
      all_ingredients.append(ingredient)
  recipes_list.append(recipe)

data = {
  "recipes_list": recipes_list,
  "all_ingredients": all_ingredients
}  

my_file = open(filename, "wb")
pickle.dump(data, my_file)
my_file.close()

