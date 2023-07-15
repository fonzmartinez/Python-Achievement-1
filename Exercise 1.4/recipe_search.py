import pickle

def display_recipe(recipe):
    print("Recipe: ", recipe["name"])
    print("Cooking Time in minutes: ", recipe["cooking_time"])
    print("Ingredients: ")
    for ingredient in recipe["ingredients"]:
        print(ingredient)
    print("Difficulty Level: ", recipe["difficulty"])

def search_ingredient(data):
    for position, ingredient in enumerate(data["all_ingredients"]):
        print("Item " + str(position) + ": " + ingredient)

    try:
        print("\n")
        ingredient_num = data["all_ingredients"][
          int(input("Pick the ingredients number you want to search: "))
        ]
    except:
      print("An unexpected error has occured.")
    else: 
      print("\n")
      print("The following recipes were found")
      print("--------------------------------")
      for recipe in data["recipes_list"]:
            if ingredient_num in recipe["ingredients"]:
              (display_recipe(recipe))


filename = input("Enter the filename where you have stored your recipes: ")

try:
    recipe_file = open(filename, "rb")
    data = pickle.load(recipe_file)
except: 
    print("File not found")
else:
    search_ingredient(data)
finally:
    recipe_file.close()

