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

## Exercise 1.6 - Databases in Python

Task Requirement:
  - In this task, you’ll explore how you can use MySQL to store data for your command-line Recipe app. You’ll be able to add a few more methods into your Recipe class that perform operations on your MySQL database.

Also, note that MySQL doesn’t fully support array data types for columns. This affects your field for ingredients within each recipe. To work around this limitation, you’ll store ingredients into comma-separated strings (e.g., Milk, Sugar, Chocolate instead of ["Milk", "Sugar", "Chocolate"]). These strings can easily be converted back and forth between lists and strings using the split() and join() methods. You’ll explore this technique as part of the task.

Your “recipe_mysql.py” script will perform four basic operations through a main menu:

  1. Creating recipes and adding them to the database
  2. Searching for recipes on the database by ingredient
  3. Modifying entries in the database
  4. Deleting recipes from the database


Task Directions: 

Part 1: Create and connect database

  - First, import the "mysql.connector" module.

  - Next, initialize a connection object called "conn", which connects with the following parameters, based on the user that you set up earlier:
  1. Hostname is 'localhost'
  2. Username is 'cf-python'
  3. Password is 'password'

  - Next, initialize a 'cursor' object from "conn".

  - Create a database called "task_database". To ensure you don’t get errors from accidentally using multiple databases with the same name, make sure it’s the only database with this name on the server by using the EXISTS statement: CREATE DATABASE IF NOT EXISTS 'database name'

  - Have your script access your database with the "USE" statement.

  - Create a table called "Recipes" with the following columns:
  1. "id": integer type; increments automatically; the primary key for this table.
  2. "name": string type; character limit of '50'; stores the name of the recipe.
  3. "ingredients": string type; character limit of '255'; stores the ingredients of the recipe in the form of a string.
  4. "cooking_time": integer type; stores the cooking time in minutes.
  5. "difficulty": string type; character limit of '20'; stores the difficulty level as "Easy", "Medium", "Intermediate", or "Hard".

  As you did with the database, use the EXISTS statement to make 
  sure there isn’t already a table with the same name: CREATE TABLE
  IF NOT EXISTS 'table name'

Part 2: The Main Menu

                    Main Menu
                    ==============================
                    Pick a choice:
                            1. Create a new recipe
                            2. Search for a recipe by ingredient
                            3. Update an existing recipe
                            4. Delete a recipe
                            Type 'quit' to exit the program.
                    Your choice:

  - To implement a main menu, let's first understand how the user would flow through it:
  1. First, the user gets to choose from four options: adding recipes, Searching for recipes, modifying recipes, and deleting recipes. Once the user selects an option, it should be launched through its own function call. When the function is over, the user needs to be taken back to the main menu so they can perform other operations.
  2. The process of user selection, function calling, and returning to the main menu requires a loop so that after the process has been completed once it can loop and happen again. A while loop would be perfect for this, because in this case you don’t know exactly how many times the loop will run.
  3. The condition for running the loop can be based on the user’s choice between the 4 options (adding recipes, searching for recipes, etc.). However, if the user were to enter a designated choice to exit the program, the loop would stop.

  Here's an idea of what your loop could look like:

                    # Definition for operation A
                    def operation_A():
                        . . .
                        return value

                    # Definition for operation B
                    def operation_B():
                        . . .
                        return value

                    # Definition for operation C
                    def operation_C():
                        . . .
                        return value

                    # This is our loop running the main memu.
                    # It continues to loop as long as the user
                    # doesn't choose to quit.
                    While(choice != 'quit'):
                        print("What would you like to do? Pick a choice!")
                        print("1. Perform Operation A")
                        print("1. Perform Operation B")
                        print("1. Perform Operation C")
                        print("Type 'quit' to exit the program.")
                        choice = input("Your choice: ")

                        if choice == '1':
                            operation_A()
                        elif choice == '2':
                            operation_B()
                        elif choice == '3':
                            operation_C()

  - Therefore, your "main_menu()" functions requires the following options:
  1. "Creating a new recipe": Calls a function called "create_recipe()" which accepts "conn" and "cursor" as its arguments.
  2. "Searching for a recipe by ingredient": Calls a function called "search_recipe()" which accepts "conn" and "cursor" as its arguments.
  3. "Updating an existing recipe": Calls a function called update_recipe() which accepts "conn" and "cursor" as its arguments.
  4. "Deleting a recipe": Calls a function called delete_recipe() which accepts "conn" and "cursor" as its arguments.

If the user exits this loop, any changes to the database would be committed and the connection created would be closed.

Once you've defined the "main_menu()" function, call it in the main code. Pass "conn" and "cursor" as arguments so that the code inside the "main_menu()" function can use the database.

Part 3: Creating a Recipe with "create_recipe()"

  -  First, collect the following details for a recipe entry:
  1. "name": Name of the recipe, string type.
  2. "cooking_time": Cooking time of the recipe in minutes, integer type.
  3. "ingredients": Ingredients of the recipe, each ingredient stored as a string in this list.

  - Next, call a function called "calculate_difficulty()". It calculates the difficulty of the recipe by taking in "cooking_time" and "ingredients" as its arguments, and returning one of the following strings: 'Easy', 'Medium', 'Intermediate', or 'Hard'. Store the output in a variable called "difficulty". Here’s how you can define this function:
  1. Set "cooking_time" and "ingredients" as the input parameters.
  2. These parameters will be used to return one of four strings that define the recipe’s difficulty: 'Easy', 'Medium', 'Intermediate', or 'Hard'.
  3. Follow the logic below using if-elif statements to return the appropriate difficulty:

      a. If "cooking_time" is less than 10 minutes and the number of "ingredients" is less than 4, set a variable called "difficulty" to the value of 'Easy'.

      b. If "cooking_time" is less than 10 minutes and the number of "ingredients" is greater than or equal to 4, set a variable called "difficulty" to the value of 'Medium'.

      c. If "cooking_time" is greater than or equal to 10 minutes and the number of "ingredients" is less than 4, set a variable called "difficulty" to the value of 'Intermediate'.

      d. If "cooking_time" is greater than or equal to 10 minutes and the number of "ingredients" is greater than or equal to 4, set a variable called "difficulty" to the value of 'Hard'.

      e. Return "difficulty" once the function’s done.

  - Now, you have to prepare to wrap this information up in an SQL query so that you can enter it into the Recipes table on your database. Since MySQL doesn’t fully support arrays, your "ingredients" list needs to be converted into a comma-separated string. This can be done through the "join()" method, which is used with the syntax: <returned_string> = "'separator characters'".join('sequence from which items are to be joined'). Here, you need to join the elements of the list "ingredients", the separator being a comma followed by a space (", "). Finally, build the query string in the following format: INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES ('respective values for each column').

  - Execute the query, then commit your changes.

Part 4: Searching for a Recipe with "search_recipe()"

  - You need to begin with an entire list of ingredients that is available in the "Recipes" table for the user to choose from. Obtain this list by SELECT-ing only the "ingredients" column from your table. Store the output into a variable called "results".

  - "results" is made up of a list of rows, each row being a tuple containing column values. Since you’re only retrieving the "ingredients" column, each row contains a single-element tuple, the element being a string containing the ingredients for each recipe. Add each ingredient that you come across into a new list called "all_ingredients", and make sure that there are no duplicates.

  - Display all the ingredients that you’ve found so far to the user, and allow them to pick a number corresponding to the ingredient in order to begin a search. Store the ingredient to be searched for into a variable called "search_ingredient".

  - To search for rows in the table that contain "search_ingredient" within the "ingredients" column, use the WHERE statement with the LIKE operator: SELECT ('columns to be displayed') FROM ('table') WHERE ('search column') LIKE ('search pattern').

In your case, an ingredient that you search for can either be in the middle, at the beginning, or at the end of the "ingredients" string. SQL Server supports the wildcard "%", which represents zero or more characters in its position. Hence, if you’re searching for "beans" within a string, your search pattern should be "%beans%".

  - Use this logic to build your query, fetch the results that satisfy this condition, and display them to the user.

Part 5: Updating a Recipe with update_recipe()

  - In this function, you’ll first fetch all the recipes that are present on the database and list them to the user. The user will then pick a recipe to be updated by specifying its corresponding "id", after which the script will ask for the column to be updated for that recipe. The columns available for modification are "name", "cooking_time" and "ingredients".

  - Once the user selects the column that needs an update, collect the new value from the user.

  - Build your query in the form of a string, to update an entry on the table for the given "id", column, and updated value. Note that if the user is updating either "cooking_time" or "ingredients", the script will have to recalculate the "difficulty" of the recipe, then update that column as well (make a separate query for this).

  - Execute your queries on the table and commit your changes.

Part 6: Deleting a Recipe with delete_recipe()

  - This function will display every recipe in your table to the user, where they can pick one by its "id" for deletion.

  - Build a query using the DELETE statement, where the row to be deleted is identified by the "id" that the user had specified.

  - Execute this query and commit your changes to the table.

Part 7: Final Steps

  - Save your Python script and ensure that your MySQL server is running on your system. Then, run your script.

  - Create about 3 to 4 simple recipes of your choice using the first option in your menu: "Create a Recipe".

  - Run a search by selecting the ingredient to search for, this time using the second option in your script: "Search for a Recipe".

  - Change a few values in some of your recipes using the third option in your script’s menu: "Update a Recipe". 2 or 3 updates should be enough.

  - Delete any one of your recipes using the final option: "Delete a Recipe".

  - Exit the script using the exit keyword that you defined before (e.g. 'quit').

## Exercise 1.7 - Object-Relational Mapping in Python

Task Requirement: 
  - You’ll be making your final application for your command line Recipe app here. You’ll make use of most of the concepts that you’ve learned so far to build a robust, functional, and user-friendly application. Let’s work towards finalizing your Recipe app, step by step.


Task Directions: 

Part 1: Set Up Your Script & SQLAlchemy

  - Open a script file called "recipe_app.py".

  - As you saw earlier, your application requires a number of packages and functions for each part to operate, such as model definitions and session creation. Make sure you import all the packages and methods necessary to build your application.

  - Set up SQLAlchemy if you haven’t already. Make sure that your MySQL server is up and running. Take note of your username, password, hostname, and database name.

  - Use the credentials and details above to create an engine object called "engine" that connects to your desired database. (Note: You can use the database "task_database" that you created in the previous Exercise.)

  - Make the session object that you’ll use to make changes to your database. To do this, generate the "Session" class, "bind" it to the "engine", and initialize the "session" object.

Part 2: Create Your Model and Table

Store your declarative base class into a variable called Base. Then, begin your definition for the Recipe model.

  - The Recipe class should inherit the Base class that you created earlier.
  
  - Define an attribute to set the table’s name as final_recipes.

  - Define these attributes to create columns in your table:
  1. "id": integer; primary key; increments itself automatically.
  2. "name": string with 50-character limit; stores the recipe’s name.
  3. "ingredients": string type; character limit of 255; stores the ingredients of the recipe in the form of a string.
  4. "cooking_time": integer; stores the recipe’s cooking time in minutes
  5. "difficulty": string with 20-character limit; stores one of four strings that describe the difficulty of the recipe ('Easy', 'Medium', 'Intermediate', and 'Hard').

  - Define a __repr__ method that shows a quick representation of the recipe, including the "id", "name", and "difficulty".

  - Define a __str__ method that prints a well-formatted version of the recipe. Get creative with your print statements! Some quick tips:
  1. The '\t' characters create a tab space, which is equivalent to 4 spaces.
  2. The '\n' characters string creates a new line. (Remember: these characters are strings, so they’ll always go inside quotation marks.)
  3. To repeat a set of characters multiple times, simply type your desired characters in double quotes, followed by *({number of times to be repeated}). For example, typing in print("-"*5) would give you -----.
  4. Use the 'end' keyword argument in the "print()" function to explicitly define what comes after its output. By default, every "print()" statement creates a new line. Have a look at the following example:

                      print("Hello", end="=")
                      print("World")

This would give an output of:

                      Hello-World

  - Define a method called "calculate_difficulty()" to calculate the difficulty of a recipe based on the number of ingredients and cooking time. You may copy the same code from the task in the previous Exercise here, with the exception of the last step (where instead of returning the calculated "difficulty", the difficulty level is instead assigned to the instance variable "self.difficulty").

  - Define a method that retrieves the "ingredients" string inside your "Recipe" object as a list, called "return_ingredients_as_list()". It will follow these steps:
  1. If the instance variable "self.ingredients" is an empty string, return an empty list.
  2. Otherwise, use the "split()" method available to strings to split the string into a list wherever there’s a comma followed by a space (,). Return this list.

  - Once you’re done defining your model, create the corresponding table on the database using the "create_all()" method from "Base.metadata".

Part 3: Define your Main Operations as Functions

Before you create the main menu, you need to establish the functions that get executed when an option on the main menu is picked. Let’s go through the five functions, one by one.

  Function 1: create_recipe()

  - Collect the details of the recipe ("name", "ingredients", "cooking_time") from the user.

  - Ensure all the inputs are appropriate (e.g., "name" doesn’t extend past 50 characters, or "cooking_time" isn’t a letter of the alphabet). Use the following methods to perform these checks for a given string called "line":
  1. "len()" - use "len(line)" to get the length of "line" as an integer.
  2. "isalnum()" - "line.isalnum()" gives you 'True' or 'False' based on whether "line" contains alphanumeric characters.
  3. "isnumeric()" - "line.isnumeric()" returns 'True' or 'False' based on whether line contains only numbers.
  4. "isalpha()" - "line.isalpha()" returns 'True' or 'False' based on whether line contains only alphabetical characters.

  - Collect the ingredients from the user in the following manner:
  1. Define a temporary empty list called "ingredients".
  2. Ask the user how many ingredients they’d like to enter.
  3. Based on this number, run a 'for' loop that collects each ingredient and then adds it to your temporary list, "ingredients".

  - Convert the list "ingredients" into a string using the "join()" method, where each ingredient is joined to the other with a comma followed by a space (,).

  - Create a new object from the "Recipe" model called "recipe_entry" using the details above.

  - Generate the "difficulty" attribute for this recipe by calling its "calculate_difficulty()" method.

  - Add this to your database through the "session" object, and commit this change.

  Function 2: view_all_recipes()

  - Retrieve all recipes from the database as a list.

  - If there aren’t any entries, inform the user that there aren’t any entries in your database, and exit the function to return to the main menu. (Tip: to exit the function, simply use the return None statement.)

  - Loop through this list of recipes, and call each of their __str__ methods to display each recipe.

  Function 3: search_by_ingredients()

  - Check if your table has any entries. Use the "count()" method like below to get the number of entries in the given table: "session.query({model name}).count()". If there aren’t any entries, notify the user, and exit the function.

  - Retrieve only the values from the "ingredients" column of your table, and store this into a variable called "results".

  - Initialize an empty list called "all_ingredients".

  - Go through each entry in "results", split up the ingredients into a temporary list, and add each ingredient from this list to "all_ingredients". Check each ingredient isn’t already on the list before adding.

  - Display these ingredients to the user, where each ingredient has a number displayed next to it. Ask them by which ingredients they’d like to search for recipes.

  - The user is allowed to pick these ingredients by typing the numbers corresponding to the ingredients, separated by spaces.

  - Check that the user’s inputs match the options available. Otherwise, inform the user and exit the function.

  - Based on the user’s selection as numbers, make a list of ingredients to be searched for, called "search_ingredients", which contains these ingredients as strings.

  - Initialize an empty list called "conditions". This list will contain "like()" conditions for every ingredient to be searched for.

  - Run a loop that runs through "search_ingredients", and performs the following steps:
  1. Make a search string called "like_term", which is essentially the ingredient, surrounded by a “%” on either side (e.g., “%Milk%”).
  2. Append the search condition containing "like_term" to the "conditions" list (e.g., {Model name}.{column to search in}.like(like_term)).

  - Retrieve all recipes from the database using the "filter()" query, containing the list "conditions". Display these recipes using the __str__ method.

  Function 4: edit_recipe()

  - Check if any recipes exist on your database, and continue only if there are any. Otherwise, exit this function.

  - Retrieve the "id" and "name" for each recipe from the database, and store them into "results".

  - From each item in "results", display the recipes available to the user.

  - The user gets to pick a recipe by its "id". If the chosen "id" doesn’t exist, exit the function.

  - Retrieve the entire recipe that corresponds to this "id" from the database into a variable called "recipe_to_edit".

  - Display the recipe, including only "name", "ingredients" and "cooking_time". "difficulty" isn’t editable since it is a calculated value. Display a number next to each attribute so that the user gets to pick one.

  - Ask the user which attribute they’d like to edit by entering the corresponding number. Remember to check the user’s input here.

  - Based on the input, use "if-else" statements to edit the respective attribute inside the "recipe_to_edit" object. Recalculate the difficulty using the object’s "calculate_difficulty()" method.

  - Commit these changes to the database.

  Function 5: delete_recipe()

  - Check if any recipes exist on our database, and continue only if there are any. Otherwise, exit this function.

  - Retrieve the "id" and "name" of every recipe in the database. List these out to the user to choose from.

  - Ask the user which recipe they’d like to delete by entering the corresponding "id". Verify inputs here.

  - Based on the selected "id", retrieve the corresponding object that exists on the database.

  - Ask the user if they’re sure that they’d like to delete this entry. If it’s a ‘yes’, perform the delete operation and commit this change. Otherwise, exit the function.

Part 4: Design Your Main Menu

Your main menu will be contained in a "while" loop, where the condition to exit the loop will be based on the user’s choice. The condition can be such that the loop only continues if the user’s choice at any point is not "quit". This main menu is similar to that of the previous Exercise, with the difference being that the function call for each option doesn’t pass through arguments like "conn" and "cursor".

  Directions

  - Inside this loop, lay out print statements that display six options:
  1. Create a new recipe
  2. View all recipes
  3. Search for recipes by ingredients
  4. Edit a recipe
  5. Delete a recipe
  6. Additionally, tell the user to type "quit" to quit the application.

  - Using "if-elif" statements, launch the corresponding function based on the user’s input. Use an "else" statement at the end to handle any malformed input by informing the users of this error and having the loop simply continue to its next iteration to display the main menu again.

  - Once the user chooses to quit, close "session" and "engine" with their respective "close()" methods, and the script ends there.

Part 5: Final Steps

  Directions

  - Create a few recipes of your own through your application.

  - Run through each option on the menu, testing the app’s functionality by reading, updating, and deleting entries in your database and taking screenshots of your terminal during these operations.
