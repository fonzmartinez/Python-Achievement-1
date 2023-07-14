## Exercise 1.4 - File Handling in Python

Task Requirements:
  - For this task, you’ll revisit what you’ve produced in the previous Exercises when managing recipes—with the added feature of being able to store these recipes on your machine! This task is divided into two scripts: “recipe_input.py” and “recipe_search.py”.

First, “recipe_input.py” takes recipes from the user, compiles them and their ingredients into a list, and stores all this in a binary file for later use. The script can be run again later to add more recipes.

Then, “recipe_search.py” accesses the binary file and lists all the ingredients that are available. The user enters an ingredient, and the script displays every recipe containing that specific ingredient.


Task Directions:

Part 1: recipe_input.py Script

  - Import the "pickle" module so you can work with binary files.

  - Define a function called "take_recipe()" to take recipes from the user, which performs the following operations:
  1. Taking in the recipe name, cooking time, and ingredients from the user.
  2. Calculating the difficulty of the recipe by calling the "calc_difficulty()" function.
  3. Gathering all these attributes into a dictionary and returning it.

  - Define the function "calc_diffficulty()", where the difficulty is returned as 'Easy', 'Medium', 'Intermediate' or 'Hard' based on the following logic:
  1. If "cooking_time" is less than 10 minutes and the number of ingredients is less than 4, set a variable called "difficulty" to the value of 'Easy'.
  2. If "cooking_time" is less than 10 minutes and the number of ingredients is greater than or equal to 4, set a variable called "difficulty" to 'Medium'.
  3. If "cooking_time" is greater than or equal to 10 minutes and the number of ingredients is less than 4, set a variable called "difficulty" to the value of 'Intermediate'.
  4. If "cooking_time" is greater than or equal to 10 minutes and the number of ingredients is greater than or equal to 4, set a variable called "difficulty" to 'Hard'.

  - Next, you’ll work on the main code. Have the user enter a filename, which would attempt to open a binary file in read mode. Define a "try-except-else-finally" block as follows:
  1. The 'try' block will open the given file, and load its contents through the 'pickle' module into a variable called "data". The incoming data is expected to be a dictionary containing two key-value pairs: "recipes_list" (a list of all recipes); "all_ingredients" (a list of all ingredients across all recipes).
  2. An 'except' clause handles the "FileNotFoundError" exception if a file with the given name isn’t found. The code block after will create a new dictionary called "data", which contains the "recipes list" under the key recipes_list and another list containing all the ingredients under "all_ingredients".
  3. Another 'except' clause that handles other exceptions and performs the same operations as the first 'except' block.
  4. An 'else' block that closes the file stream that would’ve been opened in the 'try' block.
  5. A 'finally' block that extracts the values from the dictionary into two separate lists: "recipes_list" and "all_ingredients".

  - Ask the user how many recipes they’d like to enter, and define a 'for' loop that calls the "take_recipe()" function. You can append the output of this function into "recipes_list". Next, define an inner loop that scans through the recipe’s ingredients and adds them to "all_ingredients" if they’re not already there.

  - Gather the updated "recipes_list" and "all_ingredients" into the dictionary called "data".

  - Finally, open a binary file with the user-defined filename and write "data" to it using the 'pickle' module.

Part 2 - recipe_search.py Script

  - Import the 'pickle' module.

  - Define a function to display a recipe called "display_recipe()", which takes in one recipe (of the dictionary type) as an argument and prints all of its attributes including the recipe name, cooking time, ingredients, and difficulty.

  - Define another function called "search_ingredient()" to search for an ingredient in the given data. The function takes in a dictionary called "data" as its argument. The function will perform the following steps:
  1. First, it shows the user all the available ingredients contained in "data", under the key "all_ingredients". Each ingredient is displayed with a number (take the index of each ingredient for this purpose using the "enumerate()" function).
  2. Define a 'try' block where the user gets to pick a number from this list. This number is used as the index to retrieve the corresponding ingredient, which is then stored into a variable called "ingredient_searched".
  3. Make an 'except' clause that warns the user if the input is incorrect.
  4. Add an 'else' clause that goes through every recipe in "data" (hint: "recipes_list" is the key that holds every recipe). Each recipe that contains the given ingredient will be printed.

  - In the main code, ask the user for the name of the file that contains your recipe data.

  - Use a 'try' block to open the file, and then extract its contents into "data" (from Step 3) using the 'pickle' module.

  - For when the 'try' block fails, add an 'except' block to warn the user that the file hasn’t been found.

  - Define an 'else' block that calls "search_ingredient()" while passing "data" into it as an argument.

Part 3: Final Steps

  - Run “recipe_input.py” and enter a few sample recipes of your choice. Make sure the script can generate a binary file after execution. 

  - Run “recipe_search.py”, enter the ingredient to be searched for, and make sure you get the desired output with the relevant recipes. 
