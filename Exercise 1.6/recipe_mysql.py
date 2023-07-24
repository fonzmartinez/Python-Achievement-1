import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='cf-python',
    passwd='password')

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")

cursor.execute("USE task_database")

cursor.execute('''CREATE TABLE IF NOT EXISTS recipes(
    id                  INT PRIMARY KEY AUTO_INCREMENT,
    name                VARCHAR(50),
    ingredients         VARCHAR(255),
    cooking_time        INT,  
    difficulty          VARCHAR(20)     
)''')


def main_menu(conn, cursor):
    choice = ""
    while (choice != "quit"):
        print("\nMAIN MENU")
        print("=========================")
        print("Pick a choice:")
        print("     1. Create a new recipe")
        print("     2. Search for a recipe by ingredient")
        print("     3. Update an existing recipe")
        print("     4. Delete a recipe")
        print("     Type 'quit' to exit the program.")
        choice = input("Your choice: ")

        if choice == "1":
            create_recipe(conn, cursor)
        elif choice == "2":
            search_recipe(conn, cursor)
        elif choice == "3":
            update_recipe(conn, cursor)
        elif choice == "4":
            delete_recipe(conn, cursor)

def create_recipe(conn, cursor):
    recipe_ingredients = []
    name = str(input("Enter name of the recipe: "))
    cooking_time = int(input("Enter the cooking time in minutes: "))
    ingredients = input("Enter the ingredients: ")
    recipe_ingredients.append(ingredients)
    difficulty = calculate_difficulty(cooking_time, recipe_ingredients)
    recipe_ingredients_str = ", ".join(recipe_ingredients)
    sql = 'INSERT INTO recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)'
    val = (name, recipe_ingredients_str, cooking_time, difficulty)

    cursor.execute(sql, val)
    conn.commit()
    print("\nRecipe Saved")


def calculate_difficulty(cooking_time, recipe_ingredients):
    if (cooking_time < 10) and (len(recipe_ingredients) < 4):
      difficulty = "easy"
    elif (cooking_time < 10) and (len(recipe_ingredients) >= 4):
      difficulty = "medium"
    elif (cooking_time >= 10) and (len(recipe_ingredients) < 4):
      difficulty = "intermediate"
    elif (cooking_time >= 10) and (len(recipe_ingredients) >= 4):
      difficulty = "hard"
    return difficulty


def search_recipe(conn, cursor):
    all_ingredients = []
    cursor.execute("SELECT ingredients FROM recipes")
    results = cursor.fetchall()

    print("\nList of all ingredients:")
    print("--------------------------")

    for row in results:
            row = row[0]
            row = row.split(", ")           
            for ingredients in row:
                if ingredients not in all_ingredients:
                    all_ingredients.append(ingredients)

    count = 1
    for ingredients in all_ingredients:
        print(count, "- ", ingredients)
        count = count + 1
    
    search_ingredient = int(input("Enter the number of the ingredient you want to search: "))
    index = search_ingredient - 1
    search_ingredient = all_ingredients[index]

    cursor.execute("SELECT ingredients FROM recipes WHERE ingredients LIKE '%" + search_ingredient + "%'")
    results_ingredients = cursor.fetchall()
    cursor.execute("SELECT name FROM recipes WHERE ingredients LIKE '%" + search_ingredient + "%'")
    results_name = cursor.fetchall()
    print("List of recipes with ingredient " + search_ingredient)
    print("----------------------------------------------------")
    for row in results_name:
        print(row[0])


def update_recipe(conn, cursor):
    cursor.execute("SELECT * FROM recipes")
    results = cursor.fetchall()

    print("\nChoose the recipe you wish to update:")
    print("---------------------------------------")

    for row in results:
        print(row[0], row[1])

    searched_recipe_id = str(input("Enter the number of the recipe you want to update: "))

    if not searched_recipe_id == None:
        searched_recipe_column = str(input("What column do you want to update? Type 'name', 'cooking_time' or 'ingredients': "))

        if searched_recipe_column == "name":
            new_name = str(input("Enter a new name for this recipe: "))
            cursor.execute("UPDATE recipes SET name = '" + new_name + "' WHERE id = " + searched_recipe_id)
            print("\nUpdated name to: " + new_name )

        elif searched_recipe_column == "cooking_time":
            new_cookingtime = str(input("Enter a new cooking time for this recipe: "))
            new_difficulty = calculate_difficulty (int(new_cookingtime), row[4])
            cursor.execute("UPDATE recipes SET cooking_time = " + new_cookingtime + " WHERE id = " + searched_recipe_id)
            cursor.execute("UPDATE recipes SET difficulty = '" + new_difficulty + "' WHERE id = " + searched_recipe_id)
            print("\nUpdated cooking time to: " + new_cookingtime + ", and difficulty to: " + new_difficulty)

        elif searched_recipe_column == "ingredients":
            new_ingredients = []
            n = int(input("Enter the number ingredients for this recipe: "))        
            for i in range(0, n):                                                        
                ingredient = input(" - ")
                new_ingredients.append(ingredient)
            new_ingredients_joined = ", ".join(new_ingredients)    
            new_difficulty = calculate_difficulty (row[3], new_ingredients)
            cursor.execute("UPDATE recipes SET ingredients = '" + new_ingredients_joined + "' WHERE id = " + searched_recipe_id)
            cursor.execute("UPDATE recipes SET difficulty = '" + new_difficulty + "' WHERE id = " + searched_recipe_id)
            print("\nUpdated Ingredients to: " + new_ingredients_joined + ", and difficulty to: " + new_difficulty)

        else: 
            print("\nYou didn't enter a column from the list. Try again.") 
            update_recipe(conn, cursor)   

        conn.commit()
        print("Recipe Updated")
            

def delete_recipe(conn, cursor): 
    cursor.execute("SELECT * FROM recipes")
    results = cursor.fetchall()

    print("\nChoose the recipe you wish to delete: ")
    print("----------------------------------------")

    for row in results:
        print(row[0], row[1])   

    searched_recipe_id = str(input("Enter the number of the recipe you want to delete: ")) 
    cursor.execute("DELETE FROM recipes WHERE id = " + searched_recipe_id)
    conn.commit()
    print("\nRecipe deleted!")     


main_menu(conn, cursor)
print('\nGoodbye!')                
