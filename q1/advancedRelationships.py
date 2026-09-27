class Ingredient:
    def __init__(self, ingredient_name, ingredient_amount, unit, ingredient_price, effects=None):
        self.ingredient_name = ingredient_name
        self.ingredient_amount = ingredient_amount
        self.unit = unit
        self.ingredient_price = ingredient_price
        self.effects = effects if effects is not None else []

    def display_info(self, index):
        print(f"   {index}. {self.ingredient_name}")
        print(f"      - Quantity: {self.ingredient_amount} {self.unit}")
        print(f"      - Price: ${self.ingredient_price}")
        for effect in self.effects:
            print(f"      - Effect: {effect}")

    def addColor(self, color_effect):
        self.effects.append(color_effect)

    def addFlavor(self, flavor_effect):
        self.effects.append(flavor_effect)

    def odorize(self, scent_effect):
        self.effects.append(scent_effect)

class NutritionProfile:
    def __init__(self, calories=250, protein_g=6, carbs_g=30):
        self.calories = calories
        self.protein_g = protein_g
        self.carbs_g = carbs_g

    def display_nutrition(self):
        return f"{self.calories} kcal | Protein: {self.protein_g}g | Carbs: {self.carbs_g}g"
class Recipe:
    def __init__(self, recipe_name, prep_time_minutes, is_gluten_free, servings=2):
        self.recipe_name = recipe_name
        self.prep_time_minutes = prep_time_minutes
        self.is_gluten_free = is_gluten_free
        self.__servings = servings
        self.__is_favorite = False
        
        self.ingredients = []
        
        self.nutrition_profile = NutritionProfile(calories=220, protein_g=5, carbs_g=28)

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)
        print(f"[+] Associated {ingredient.ingredient_name} with {self.recipe_name}")

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
        print("Nutrition Profile (Composition): " + self.nutrition_profile.display_nutrition())
        print("Ingredients (Aggregation):")
        
        if len(self.ingredients) == 0:
            print("  (No ingredients added yet)")
            return
        
        count = 1
        for item in self.ingredients:
            item.display_info(count)
            count += 1


class BakingRecipe(Recipe):
    def __init__(self, recipe_name, prep_time_minutes, is_gluten_free, baking_temp, bake_time_minutes, servings=2):
        super().__init__(recipe_name, prep_time_minutes, is_gluten_free, servings)
        self.baking_temp = baking_temp
        self.bake_time_minutes = bake_time_minutes

    def displayRecipeDetails(self):
        super().displayRecipeDetails()
        print(f"Baking Temperature: {self.baking_temp}°F")
        print(f"Bake Time: {self.bake_time_minutes} mins")


class KitchenScale:
    def weigh(self, ingredient):
        print(f"[Kitchen Scale] Accurate weight check: {ingredient.ingredient_amount} {ingredient.unit} of {ingredient.ingredient_name}.")


class Chef:
    def __init__(self, chef_name):
        self.chef_name = chef_name

    def weigh_ingredient(self, ingredient, scale):
        print(f"\nChef {self.chef_name} is weighing ingredient...")
        scale.weigh(ingredient)


if __name__ == "__main__":
    print("=== TEST 1: INHERITANCE ===")
    ing1 = Ingredient("Cocoa Powder", 1, "cup", 4)
    ing1.addColor("makes the cookies go brown")
    ing1.addFlavor("makes the cookies taste chocolate")

    ing2 = Ingredient("Vanilla Extract", 1, "tsp", 5)
    ing2.odorize("makes the cookies smell sweet")

    ing3 = Ingredient("Sugar", 0.5, "cup", 2)
    ing3.addFlavor("makes the cookies sweet")

    baking_recipe = BakingRecipe(
        recipe_name="Chocolate Cookies", 
        prep_time_minutes=20, 
        is_gluten_free=False, 
        baking_temp=350, 
        bake_time_minutes=12,
        servings=2
    )

    baking_recipe.adjustServings(4)
    baking_recipe.markAsFavorite()

    print("\n=== TEST 2: AGGREGATION & COMPOSITION ===")
    baking_recipe.add_ingredient(ing1)
    baking_recipe.add_ingredient(ing2)
    baking_recipe.add_ingredient(ing3)

    baking_recipe.displayRecipeDetails()

    print("\n=== TEST 3: DEPENDENCY ===")
    head_chef = Chef("Auguste")
    scale_tool = KitchenScale()

    head_chef.weigh_ingredient(ing1, scale_tool)

