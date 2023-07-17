## Exercise 1.5 - Object-Oriented Programming in Python

Task Requirement: 
  - For this task, instead of storing recipes into dictionaries, you’ll now store them as objects with their own data attributes and custom methods. This will make your scripts more efficient and concise.

In this task, you’ll be performing three main operations:
  1. Building a 'Recipe' class with relevant data and procedural attributes.
  2. Creating and storing recipes using class methods (same as procedural attributes).
  3. Using these class methods to search for recipes according to specific ingredients.


Task Directions:

To begin, open a script file named “recipe_oop.py” and perform the following steps.

  - Define a class Recipe, with the following data attributes:
  1. "name": the name of a recipe
  2. "ingredients": a list containing the ingredients for a recipe
  3. "cooking_time": the time taken in minutes to carry out a recipe
  4. "difficulty": an auto-generated attribute that says whether the recipe is 'Easy', 'Medium', 'Intermediate', or 'Hard' based on the following logic (this attribute will be updated by the upcoming "calculate_difficulty()" class method):
  a. If "cooking_time" is less than 10 minutes, and the number of "ingredients" is less than 4, set a variable called "difficulty" to the value of 'Easy'.
  b. If "cooking_time" is less than 10 minutes, and the number of "ingredients" is greater than or equal to 4, set a variable called "difficulty" to the value of 'Medium'.
  c. If "cooking_time" is greater than or equal to 10 minutes, and the number of "ingredients" is less than 4, set a variable called "difficulty" to the value of 'Intermediate'.
  d. If "cooking_time" is greater than or equal to 10 minutes, and the number of "ingredients" is greater than or equal to 4, set a variable called "difficulty" to the value of 'Hard'.

  - Define the following procedural attributes (methods) for the class as well:
  1. An initialization method that takes in the "name" for the recipe and initializes the other data attributes too. Getter and setter methods for "name" and "cooking_time".
  2. A method called "add_ingredients" that takes in variable-length arguments for the recipe’s ingredients. For example, the arguments could be either ("Salt") or even ("Salt", "Pepper", "Flour", "Water", "Bananas", "Marzipan"); your method should take in these ingredients and add them to "ingredients". Once all the ingredients are added, this function calls "update_all_ingredients()" , which you’ll define shortly.
  3. A getter method for "ingredients" that returns the list itself.
  4. A method called "calculate_difficulty()" that uses the logic in part 1 of this task, and updates the difficulty of the recipe.
  5. A getter method for "difficulty" which also calls "calculate_difficulty()" if "difficulty" hasn’t been calculated.
  6. A search method called "search_ingredient()" that takes an ingredient as an argument, searches for it in the recipe, and returns 'True' or 'False' appropriately.
  7. A method called "update_all_ingredients()" that goes through the current object’s ingredients and adds them to a class variable called "all_ingredients", if they’re not already present. This class variable keeps track of all the ingredients that exist across all recipes.
 8. A string representation that prints the entire recipe over a well formatted string.

  - To find recipes that contain a specific ingredient, define a method called "recipe_search()":
  1. Define 2 parameters for this method:
  a. "data": takes in a list of "Recipe" objects to search from
  b. "search_term": the ingredient to be searched for
  2. Run a 'for' loop that traverses through 'data', and performs the following steps:
  a. Within the object that is in focus, call the "search_ingredient" method to see if the ingredient is present or not.
  b. If the above condition is satisfied, print the recipe.

  - In the main code, make an object under the "Recipe" class:
  1. Initialize an object named 'tea' under this class, and set the recipe’s name as "Tea" through the initialization step.
  2. Add the following ingredients to this recipe: 'Tea Leaves', 'Sugar', 'Water'.
  3. Set the cooking time for this recipe as "5" (in minutes).
  4. Display the string representation of this object.

  - Make a few more recipes with the given attributes, and display their respective string representations as well:
  1. "Coffee":

        a. "Ingredients": Coffee Powder, Sugar, Water
        b. "Cooking time": 5 minutes
  2. "Cake":

        a. "Ingredients": Sugar, Butter, Eggs, Vanilla Essence, Flour, Baking Powder, Milk
        b. "Cooking time": 50 minutes
  3. "Banana Smoothie":
  
        a. "Ingredients": Bananas, Milk, Peanut Butter, Sugar, Ice Cubes
        b. "Cooking time": 5 minutes

  - Wrap the recipes into a list called "recipes_list".

  - Use the "recipe_search()" method to search for recipes that contain each ingredient out of: 'Water', 'Sugar', 'Bananas'.