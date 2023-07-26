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
  3. To repeat a set of characters multiple times, simply type your desired characters in double quotes, followed by *('number of times to be repeated'). For example, typing in print("-"*5) would give you -----.
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

  - Check if your table has any entries. Use the "count()" method like below to get the number of entries in the given table: "session.query('model name').count()". If there aren’t any entries, notify the user, and exit the function.

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
  2. Append the search condition containing "like_term" to the "conditions" list (e.g., 'Model name'.'column to search in'.like(like_term)).

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
