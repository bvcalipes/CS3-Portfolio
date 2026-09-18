class Ingredient:
    def __init__(self, ingredient_name, ingredient_amount, unit, ingredient_price, effects=None):
        self.ingredient_name = ingredient_name
        self.ingredient_amount = ingredient_amount
        self.unit = unit
        self.ingredient_price = ingredient_price
        self.effects = effects if effects is not None else []

    def display_info(self, index):
        print(str(index) + ". " + self.ingredient_name)
        print("   - " + str(self.ingredient_amount) + " " + self.unit)
        for effect in self.effects:
            print("   - " + effect)

    def addColor(self, color_effect):
        self.effects.append(color_effect)

    def addFlavor(self, flavor_effect):
        self.effects.append(flavor_effect)

    def odorize(self, scent_effect):
        self.effects.append(scent_effect)


class Recipe:
    def __init__(self, recipe_name, prep_time_minutes, is_gluten_free, servings=2):
        self.recipe_name = recipe_name
        self.prep_time_minutes = prep_time_minutes
        self.is_gluten_free = is_gluten_free
        self.__servings = servings
        self.__is_favorite = False
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)
        print("[+] Associated " + ingredients.ingredient_name + "with" + self.recipe_name)

    def adjustServings(self, new_servings):
        self.__servings = new_servings

    def markAsFavorite(self):
        self.__is_favorite = True

    def displayRecipeDetails(self):
        favorite_status = "Yes" if self.__is_favorite else "No"
        gluten_status = "Yes" if self.is_gluten_free else "No"
        
        print("\n--- RECIPE: " + self.recipe_name + " ---")
        print("Prep Time: " + str(self.prep_time_minutes) + " mins")
        print("Gluten Free: " + gluten_status)
        print("Servings: " + str(self.__servings))
        print("Favorite: " + favorite_status)
        print("\nIngredients:")
        
        if len(self.ingredients) == 0:
            print("  (No ingredients added yet)")
            return
        
        count = 1
        for item in self.ingredients:
            item.display_info(count)
            count += 1


print("=== STEP A: OBJECTS BEFORE ASSOCIATION ===")

ing1 = Ingredient("Cocoa Powder", 1, "cup", 4)
ing1.addColor("makes the cookies go brown")
ing1.addFlavor("makes the cookies taste chocolate")

ing2 = Ingredient("Vanilla Extract", 1, "tsp", 5)
ing2.odorize("makes the cookies smell sweet")

ing3 = Ingredient("Sugar", 0.5, "cup", 2)
ing3.addFlavor("makes the cookies sweet")

my_recipe = Recipe("Chocolate Cookies", 20, False)

my_recipe.displayRecipeDetails()

print("\n=== STEP B: BUILDING RELATIONSHIP ===")

my_recipe.add_ingredient(ing1)
my_recipe.add_ingredient(ing2)
my_recipe.add_ingredient(ing3)

print("\n=== STEP C: RELATIONSHIP AFTER ASSOCIATION ===")

my_recipe.adjustServings(4)
my_recipe.markAsFavorite()
my_recipe.displayRecipeDetails()

print("\n--- Direct Data Access via Relationship ---")
if len(my_recipe.ingredients) > 0:
    first_item = my_recipe.ingredients[0]
    print("First ingredient directly accessed:", first_item.ingredient_name, "-", str(first_item.ingredient_amount), first_item.unit)