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
        4. 'recipe'(dictionary): Stores the 'name', 'cooking_time', and 'ingredients' variables (e.g.,    
           'recipe' = {'name': name, 'cooking_time': cooking_time, 'ingredients': ingredients}).

  - In the main section of your code, ask the user how many recipes they would like to enter. Their response will be linked to a variable 'n'. 

  - Run a 'for' loop, which runs 'n' times to perform the following steps:
        1. Run 'take_recipe()' and store its return output (a dictionary) in a variable called 'recipe'.
        2. Run another 'for' loop inside this loop, which iterates through 'recipe'’s 'ingredients' list, where 
           it picks out elements one-by-one as 'ingredient'. It will run the following step inside: if the 
           chosen 'ingredient' isn’t present in 'ingredients_list', add it to this list. To check if an 
           element ele is present in a sequence 'seq', you can use the 'in' keyword in a conditional statement 
           as follows: 'if ele in seq:'.Either 'True' or 'False' is returned (remember that you’re checking if 
           'ingredient' is not in the list, so use the 'not' operator accordingly).
        3. Once you’ve finished adding ingredients, append 'recipe' to 'recipes_list'.

  - Run another 'for' loop that iterates through 'recipes_list', picks out each element (a dictionary) as 'recipe', and performs the following steps:
        1. Determine the 'difficulty' of the recipe using the following logic: 
              - If 'cooking_time' is less than 10 minutes, and the number of 'ingredients' is less than 4, 
                set a variable called 'difficulty' to the value of 'Easy'.
              - If 'cooking_time' is less than 10 minutes, and the number of 'ingredients' is greater than 
                or equal to 4, set a variable called 'difficulty' to the value of 'Medium'.
              - If 'cooking_time' is greater than or equal to 10 minutes, and the number of 'ingredients' 
                is less than 4, set a variable called 'difficulty' to the value of 'Intermediate'.
              - If 'cooking_time' is greater than or equal to 10 minutes, and the number of 'ingredients' 
                is greater than or equal to 4, set a variable called 'difficulty' to the value of 'Hard'.
        2. Display the recipe in the following format, using values from each dictionary ('recipe') 
           obtained from 'recipes_list':

                    Recipe: <recipe[recipe_name]>
                    Cooking Time (min): <recipe[cooking_time]>
                    Ingredients: 
                    <recipe[ingredients][0]>
                    <recipe[ingredients][1]>
                    ...
                    <recipe[ingredients][n]>
                    Difficulty level: <difficulty>

        3. For example, it could look like this:

                    Recipe: Instant Noodles
                    Cooking Time (min): 5
                    Ingredients: 
                    Noodle Cakes
                    Flavoring
                    Water
                    Difficulty level: Easy

  - Next, you’ll have to display all the ingredients that you’ve come across so far in all of the recipes that you’ve just entered. In Step 5 you appended these ingredients into 'ingredient_list'. Now it’s time to print them all out. Print them in alphabetical order, in a format similar to this example: