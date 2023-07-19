class Recipe(object):

    all_ingredients = []

    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.cooking_time = 0
        self.difficulty = None

    def get_name(self):
        return self.name

    def get_cooking_time(self):
        return self.cooking_time

    def set_name(self, name):
        self.name = name

    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time

    def add_ingredients(self, *ingredients):
        for ingredient in ingredients:
            self.ingredients.append(ingredient)
        self.update_all_ingredients()

    def get_ingredients(self):
        return self.ingredients

    def calculate_difficulty(self):
        if self.cooking_time < 10 and len(self.ingredients) < 4:
          self.difficulty = "easy"
        elif self.cooking_time < 10 and len(self.ingredients) >= 4:
          self.difficulty = "medium"
        elif self.cooking_time >= 10 and len(self.ingredients) < 4:
          self.difficulty = "intermediate"
        elif self.cooking_time >= 10 and len(self.ingredients) >= 4:
          self.difficulty = "hard"
        return self.difficulty

    def get_difficulty(self):
        self.calculate_difficulty()
        return self.difficulty

    def search_ingredient(self, ingredient):
        if ingredient in self.ingredients:
            return True
        else:   
            return False
    
    def update_all_ingredients(self):
        if not self.ingredients == None:  
            for ingredient in self.ingredients:
                if ingredient not in self.all_ingredients:
                    self.all_ingredients.append(ingredient)

    def __str__(self):
        output = "\nRecipe Name: " + str(self.name) + \
        "\nCooking Time in minutes: " + str(self.cooking_time) + \
        "\nDifficulty: " + str(self.difficulty) + \
        "\nIngredients: "
        for ingredient in self.ingredients:
            output += " " + ingredient + "\n"
        return output

    def recipe_search(data, search_term):
        print("\nRecipes that include:", search_term)
        print("------------------------------------")
        for recipe in data:
            if recipe.search_ingredient(search_term):
                print(recipe.name)


           
tea = Recipe("Tea")
tea.add_ingredients("Tea Leaves", "Sugar", "Water")
tea.set_cooking_time(5)
tea.get_difficulty()
print(tea)

coffee = Recipe("Coffee")
coffee.add_ingredients("Coffee Powder", "Sugar", "Water")
coffee.set_cooking_time(5)
coffee.get_difficulty()
print(coffee)

cake = Recipe("Cake")
cake.add_ingredients("Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk")
cake.set_cooking_time(50)
cake.get_difficulty()
print(cake)

banana_smoothie = Recipe("Banana Smoothie")
banana_smoothie.add_ingredients("Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes")
banana_smoothie.set_cooking_time(5)
banana_smoothie.get_difficulty()
print(banana_smoothie)

recipes_list = [tea, coffee, cake, banana_smoothie]
(Recipe.recipe_search(recipes_list, "Water"))
(Recipe.recipe_search(recipes_list, "Sugar"))
(Recipe.recipe_search(recipes_list, "Bananas"))