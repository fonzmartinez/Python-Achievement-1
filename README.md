# Python
## Exercise 1.1
Task Requirements:
  - Install Python 3.8.7 
  - Set up a new virtual environment
  - Install Visual Studio Code
  - Set up an IPython shell
  - Export a requirements file
  - Create a Github repo for this course

Task Directions: 
  - Install Python 3.8.7 on your system.  Verify you’re able to access the correct Python installation from your terminal and check that it’s running the correct version by using the python --version command.
  - Set up a new virtual environment with command "mkvirtualenv" and name it “cf-python-base”.
  - Install Visual Studio Code and make a script called “add.py” that adds two numbers that the user enters. Input from a user can be stored into a variable with the following syntax (don’t include < and > in your code): variable_name = int(input("<any prompt you'd like to give to the user>")).
Store two values a and b from the user and add them to a variable c.
Finally, print the value of c to the screen. The print() function can be used to print variable values with the following syntax: print(<variable name>).
  - Set up an IPython shell in the virtual environment “cf-python-base”. The name of the package to be installed is “ipython,” via command "pip install ipython".  Verify your installation by launching an IPython shell with the command ipython.
  - Export a requirements file. 
First, generate a “requirements.txt” file from your source environment. To do this, you use the pip freeze command and all packages (including version numbers) installed in the currently activated environment will be compiled: > pip freeze > requirements.txt.
Next, create a new environment called “cf-python-copy”. In this new environment, install packages from the “requirements.txt” file that you generated earlier. To install the packages from this file in any other environment, you run the pip install command with the extra -r argument, followed by the name of your requirements file: > pip install -r requirements.txt.
  - Create a Github repo for this course. In this Github repo, you’ll make separate folders for each Exercise. You’ll upload any deliverables from an Exercise to its designated folder, so, for example, you’ll add the deliverables specified in the final step here to a folder named “Exercise 1.1.” This way, you can keep all your work properly arranged. Keep your mentor informed about this arrangement.

## Exercise 1.2 - Data Types in Python

Task Requirements:
  - Create a structure that contains a set of attributes related to a specific recipe, and several of these “recipe structures” need to be stored sequentially in another outer structure.

PLEASE NOTE: The data structure being used for this particular task of a recipe 
             will be Dictionaries.  A dictionary would work best as different 
             value types would be used in a recipe (ex/ strings, integers, 
             lists). Since a dictionary stores values and objects within itself 
             indexed by keys, it is easier to locate item and update as needed.  
             With the use of key-value pairing, a dictionary is versatile and 
             would be best for building a recipe.


Task Directions:
  - Create a structure named 'recipe_1' that contains the following keys:
  1. name (str): Contains the name of the recipe 
  2. cooking_time (int): Contains the cooking time in minutes       
  3. ingredients (list): Contains a number of ingredients, each of the str data type

Decide what data structure you would use for this purpose, and in your README file in the repository for this task, describe in approx. 50-75 words why you’ve chosen to use it.

  - The 'recipe_1' structure that you create will be for a cup of tea, with the following attributes:
  1. Name: Tea
  2. Cooking time: 5 minutes
  3. Ingredients: Tea leaves, Sugar, Water

  - Create an outer structure called 'all_recipes', and then add 'recipe_1' to it. Figure out what type of structure you would consider for 'all_recipes'. 

PLEASE NOTE: For this task listed I would feel the type of structure to be used for 'all_recipes' would be a list.  This would be best for multiple recipes which can be stored and modified as required.

  - Generate 4 more recipes as 'recipe_2, recipe_3, recipe_4, and recipe_5', and then add them as well to all_recipes.

  - Once you’re done setting up all_recipes, print the ingredients of each recipe as five different lists, inside the IPython shell.

## Exercise 1.3 - Operators and Functions in Python

Task Requirements:
  - For this task The goal is to read any number of recipes from the user, and then add them into a list for later use, along with another list for the ingredients that you’ve come across so far. Once complete, display each recipe with its details, along with an extra feature - the difficulty level. You’ll have the difficulty level of each recipe calculated and displayed based on a few of its own attributes.


Task Directions:
  - Open a Python script in an editor of your choice and name it “Exercise_1.3.py”.

  - Initialize two empty lists: 'recipes_list' and 'ingredients_list'.

  - Define a function called 'take_recipe', which takes input from the user for the following variables:
  1. 'name'(str): Stores the name of the recipe.
  2. 'cooking_time'(int): Stores the cooking time (in minutes).
  3. 'ingredients'(list): A list that stores ingredients, each of the string data type.
  4. 'recipe'(dictionary): Stores the 'name', 'cooking_time', and 'ingredients' variables (e.g., 'recipe' = {'name': name, 'cooking_time': cooking_time, 'ingredients': ingredients}).

  - In the main section of your code, ask the user how many recipes they would like to enter. Their response will be linked to a variable 'n'. 

  - Run a 'for' loop, which runs 'n' times to perform the following steps:
  1. Run 'take_recipe()' and store its return output (a dictionary) in a variable called 'recipe'.
  2. Run another 'for' loop inside this loop, which iterates through 'recipe'’s 'ingredients' list, where 
           it picks out elements one-by-one as 'ingredient'. It will run the following step inside: if the 
           chosen 'ingredient' isn’t present in 'ingredients_list', add it to this list. To check if an 
           element ele is present in a sequence 'seq', you can use the 'in' keyword in a conditional statement 
           as follows: 'if else in seq:'.Either 'True' or 'False' is returned (remember that you’re checking if 
           'ingredient' is not in the list, so use the 'not' operator accordingly).
  3. Once you’ve finished adding ingredients, append 'recipe' to 'recipes_list'.

  - Run another 'for' loop that iterates through 'recipes_list', picks out each element (a dictionary) as 'recipe', and performs the following steps:
 Determine the 'difficulty' of the recipe using the following logic:
  1. If 'cooking_time' is less than 10 minutes, and the number of 'ingredients' is less than 4, set a variable called 'difficulty' to the value of 'Easy'.
  2. If 'cooking_time' is less than 10 minutes, and the number of 'ingredients' is greater than or equal to 4, set a variable called 'difficulty' to the value of 'Medium'.
  3. If 'cooking_time' is greater than or equal to 10 minutes, and the number of 'ingredients' is less than 4, set a variable called 'difficulty' to the value of 'Intermediate'.
  4. If 'cooking_time' is greater than or equal to 10 minutes, and the number of 'ingredients' is greater than or equal to 4, set a variable called 'difficulty' to the value of 'Hard'.

  - Display the recipe in the following format, using values from each dictionary ('recipe') 
           obtained from 'recipes_list':

                    Recipe: <recipe[recipe_name]>
                    Cooking Time (min): <recipe[cooking_time]>
                    Ingredients: 
                    <recipe[ingredients][0]>
                    <recipe[ingredients][1]>
                    ...
                    <recipe[ingredients][n]>
                    Difficulty level: <difficulty>

              For example, it could look like this:

                    Recipe: Instant Noodles
                    Cooking Time (min): 5
                    Ingredients: 
                    Noodle Cakes
                    Flavoring
                    Water
                    Difficulty level: Easy

  - Next, you’ll have to display all the ingredients that you’ve come across so far in all of the recipes that you’ve just entered. In Step 5 you appended these ingredients into 'ingredient_list'. Now it’s time to print them all out. Print them in alphabetical order, in a format similar to this example:

                    Ingredients Available Across All Recipes
                    ----------------------------------------
                    Corn
                    Eggs
                    Ground Pepper
                    Potatoes
                    Salt
                    Sugar
                    Tea Leaves
                    Tomatoes
                    Water
 
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