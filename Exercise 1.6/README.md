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

  - Create a database called "task_database". To ensure you don’t get errors from accidentally using multiple databases with the same name, make sure it’s the only database with this name on the server by using the EXISTS statement: CREATE DATABASE IF NOT EXISTS <database name>

  - Have your script access your database with the "USE" statement.

  - Create a table called "Recipes" with the following columns:
  1. "id": integer type; increments automatically; the primary key for this table.
  2. "name": string type; character limit of '50'; stores the name of the recipe.
  3. "ingredients": string type; character limit of '255'; stores the ingredients of the recipe in the form of a string.
  4. "cooking_time": integer type; stores the cooking time in minutes.
  5. "difficulty": string type; character limit of '20'; stores the difficulty level as "Easy", "Medium", "Intermediate", or "Hard".

  As you did with the database, use the EXISTS statement to make 
  sure there isn’t already a table with the same name: CREATE TABLE
  IF NOT EXISTS <table name>

Part 2: The Main Nenu

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

  - Now, you have to prepare to wrap this information up in an SQL query so that you can enter it into the Recipes table on your database. Since MySQL doesn’t fully support arrays, your "ingredients" list needs to be converted into a comma-separated string. This can be done through the "join()" method, which is used with the syntax: <returned_string> = "<separator characters>".join(<sequence from which items are to be joined>). Here, you need to join the elements of the list "ingredients", the separator being a comma followed by a space (", "). Finally, build the query string in the following format: INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (<respective values for each column>).

  - Execute the query, then commit your changes.

Part 4: Searching for a Recipe with "search_recipe()"

  - You need to begin with an entire list of ingredients that is available in the "Recipes" table for the user to choose from. Obtain this list by SELECT-ing only the "ingredients" column from your table. Store the output into a variable called "results".

  - "results" is made up of a list of rows, each row being a tuple containing column values. Since you’re only retrieving the "ingredients" column, each row contains a single-element tuple, the element being a string containing the ingredients for each recipe. Add each ingredient that you come across into a new list called "all_ingredients", and make sure that there are no duplicates.

  - Display all the ingredients that you’ve found so far to the user, and allow them to pick a number corresponding to the ingredient in order to begin a search. Store the ingredient to be searched for into a variable called "search_ingredient".

  - To search for rows in the table that contain "search_ingredient" within the "ingredients" column, use the WHERE statement with the LIKE operator: SELECT <columns to be displayed> FROM <table> WHERE <search column> LIKE <search pattern>.

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
