from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql://cf-python:password@localhost/task_database")

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Recipe(Base):
    __tablename__ = "final_recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    def __repr__(self):
        return "<Recipe ID: " + str(self.id) + "-" + self.name + "-" + self.difficulty + ">"

    def __str__(self):
        return "\nRecipe ID: " + str(self.id) + "\nName: " + self.name + \
        "\nIngredients: " + self.ingredients + "\nCooking time: " + str(self.cooking_time) + \
        " minutes" + "\nDifficulty: " + self.difficulty

def calculate_difficulty(cooking_time, ingredients):
  if cooking_time < 10 and len(ingredients) < 4:
    Recipe.difficulty = "easy"
  elif cooking_time < 10 and len(ingredients) >= 4:
    Recipe.difficulty = "medium"
  elif cooking_time >= 10 and len(ingredients) < 4:
    Recipe.difficulty = "intermediate"
  elif cooking_time >= 10 and len(ingredients) >= 4:
    Recipe.difficulty = "hard"
  return Recipe.difficulty


def return_ingredients_as_list():
  if Recipe.ingredients == " ":
    return []
  else:
    return list(Recipe.ingredients.lower().split(',').strip())


Base.metadata.create_all(engine)


def create_recipe():

    name_is_valid = False
    while name_is_valid == False:
      name_input = input("Enter name of the recipe: ")
      if len(name_input) <=50:
        name = name_input
        name_is_valid = True
      else:
        print("\nThe number of characters for the name of your recipe cannot exceed 50. Try again.")

    ingredients = []
    num_ingredients_is_valid = False
    while num_ingredients_is_valid == False:
      number_of_ingredients = input("How many ingredients would you like to enter?: ")
      if number_of_ingredients.isnumeric() == True:
        num_ingredients_is_valid = True
        for i in range(int(number_of_ingredients)):
          ingredient = input("Enter ingredient: ")
          ingredients.append(ingredient)
      else:
        num_ingredients_is_valid = False
        print("\nYou must enter a number. Try again")

    cooking_time_is_valid = False
    while cooking_time_is_valid == False:
      cooking_time_input = input("\nEnter the cooking time in minutes: ")
      if cooking_time_input.isnumeric():
        cooking_time = int(cooking_time_input)
        cooking_time_is_valid = True
      else:
        print("\nYour cooking time must be a number. Try again.")

    ingredients_str = ', '.join(ingredients)

    recipe_entry = Recipe(
        name = name,
        ingredients = ingredients_str,
        cooking_time = cooking_time,
        difficulty = calculate_difficulty(cooking_time, ingredients)
    )
    session.add(recipe_entry)
    session.commit()
    print("\nRecipe saved.")


def view_all_recipes():                                            
    recipes_list = session.query(Recipe).all()                                
    if recipes_list == []:
        print("\nThere are no recipes in database.")
        return None                                                          
    else:
        for recipe in recipes_list:
            print(recipe)                  


def search_by_ingredients():
    
    if session.query(Recipe).count() == 0:
      print("\nNo recipes have been entered.")
      return None
    else:
      results = session.query(Recipe.ingredients).all()
      all_ingredients = []
      for result in results:
        ingredient_list = list(result[0].split(', '))
        for ingredient in ingredient_list:
          if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)
      
      printed_ingredients = list(enumerate(all_ingredients, 1))
      for ingredient in printed_ingredients:
        print(str(ingredient[0]) + ". " + ingredient[1])
      
      try: 
        search_input = input("\nEnter the number of the ingredient you want to search: ")
        search_input_list = list(search_input.split(" "))
        search_ingredients = []
        for item in search_input_list:
          search_ingredients.append(all_ingredients[int(item)-1])
        print("\nThe following recipes include your selected ingredients: ")
      except:
        print("\nIngredient number is not valid.")
        return None
      else:
        conditions = []
        for ingredient in search_ingredients:
          like_term = "%" + ingredient + "%"
          conditions.append(Recipe.ingredients.like(like_term))
        searched_recipes = session.query(Recipe).filter(*conditions).all()
        for recipe in searched_recipes:
          print(recipe)
    

def edit_recipe():
  if session.query(Recipe).count() == 0:
    print("\nThere are no recipes in database.")
    return None
  else:
    results = session.query(Recipe.id, Recipe.name).all()
    print("Your recipes: ")
    for result in results:
      print("\nRecipe ID: ", result[0], "--", result[1])
    try:
      selected_id = input("\nEnter recipe ID to choose to edit: ")
      recipe_to_edit = session.query(Recipe).filter(Recipe.id == int(selected_id)).one()
      print("\n1. Name: " + recipe_to_edit.name)
      print("\n2. Ingredients: " + recipe_to_edit.ingredients)
      print("\n3. Cooking Time: " + str(recipe_to_edit.cooking_time) + " minutes")
    except:
      print("Recipe ID not valid. Try again.")
    else:
      edit_input = input("\nWhat part of the recipe do you want to edit? 1, 2, or 3?: ")
      if edit_input == "1":
        new_name = input("Enter the new name: ")
        if len(new_name) <=50:
          recipe_to_edit.name = new_name
          session.commit()
          print("\nNew name for recipe has been updated to: " + recipe_to_edit.name)
        else:
          print("Recipe name exceeds 50 characters. Try again.")
      elif edit_input == "2":
        new_ingredients = input("List new ingredients separated by commas: ")
        if len(new_ingredients) <=255:
          new_ingredients_list = list(new_ingredients.lower().split(', '))
          new_difficulty = calculate_difficulty(recipe_to_edit.cooking_time, new_ingredients_list)
          recipe_to_edit.ingredients = new_ingredients
          recipe_to_edit.difficulty = new_difficulty
          session.commit()
          print("\nNew ingredients for recipe has been updated to: " + recipe_to_edit.ingredients)
        else:
          print("\nMax number of ingredients is 255. Try again.")
      elif edit_input == "3":
        new_cooking_time = input("Enter new cooking time in minutes: ")
        if new_cooking_time.isnumeric():
          new_difficulty = calculate_difficulty(int(new_cooking_time), list(recipe_to_edit.ingredients.lower().split(', ')))
          recipe_to_edit.cooking_time = int(new_cooking_time)
          recipe_to_edit.diffculty = new_difficulty
          session.commit()
          print("\nNew cooking time has been updated to: " + str(recipe_to_edit.cooking_time) + " minutes")
        else: 
          print("Cooking time must be a number. Try again.")
      else:
        print("You must choose 1, 2, or 3. Try again.")
        

def delete_recipe():

    if session.query(Recipe).count() == 0:
      print("\nThere are no recipes in database.")
      return None
    else:
      results = session.query(Recipe.id, Recipe.name).all()
      print("Your recipes: ")
      for result in results:
        print("\nRecipe ID: ", result[0])
        print("Recipe name: ", result[1])
      try:
        selected_id = input("\nEnter Recipe ID of recipe you want to delete: ")
        recipe_to_delete = session.query(Recipe).filter(Recipe.id == int(selected_id)).one()
        print("Recipe " + recipe_to_delete.name + " will be deleted.")
      except:
        print("Recipe ID not valid.")
      else:
        confirmation = input("\nAre you sure you want to delete this recipe? Enter 'yes' or 'no': ")
        if confirmation == "yes":
          session.delete(recipe_to_delete)
          session.commit()
          print("\nRecipe has been deleted.")
        elif confirmation == "no":
          print("Returning to the main menu.")
          return None
        else:
          print("Something went wrong.")
          return None


def main_menu():
    choice = ''
    while(choice != "quit"):
      print("\nMAIN MENU")
      print("=========================")
      print("Pick a choice:")
      print("     1. Create a new recipe")
      print("     2. View all recipes")
      print("     3. Search for a recipe by ingredient")
      print("     4. Update an existing recipe")
      print("     5. Delete a recipe")
      print("     Type 'quit' to exit the program.")
      choice = input("Your choice: ")
    
      if choice == "1":
        create_recipe()
      elif choice == "2":
        view_all_recipes()
      elif choice == "3":
        search_by_ingredients()
      elif choice == "4":
        edit_recipe()
      elif choice == "5":
        delete_recipe()
      elif choice == "quit":
        print("\nGoodbye!")
      else:
        print("Something went wrong.")


main_menu()
session.close()
engine.dispose()
