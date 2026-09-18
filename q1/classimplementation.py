class Recipe:
    def __init__(self, recipe_name: str, prep_time_minutes: int, servings: int, is_gluten_free: bool):
        self.recipe_name = recipe_name
        self.prep_time_minutes = prep_time_minutes

        self.__servings = servings
        self.__is_favorite = False

        self.is_gluten_free = is_gluten_free
    
    def display_recipe_details(self) -> None:
        fav_status = "Yes" if self.__is_favorite else "No"
        gf_status = "Yes" if self.is_gluten_free else "No"
        print(f"Recipe Name: {self.recipe_name}")
        print(f"Preparation Time: {self.prep_time_minutes} minutes")
        print(f"Servings: {self.__servings}")
        print(f"Gluten-Free: {gf_status}")
        print(f"Favorited: {fav_status}")
    
    def adjust_servings(self, new_servings: int) -> None:
        if new_servings <= 0:
            print("Error: Servings must be greater than 0.")
            return
        old_servings = self.__servings
        self.__servings = new_servings
        print(f"Adjusted servings for '{self.recipe_name}' from {old_servings} to {self.__servings}.")
    
    def mark_as_favorite(self) -> None:
        self.__is_favorite = True
        print(f"'{self.recipe_name}' has been marked as a favorite.")

if __name__ == "__main__":
    recipe1 = Recipe("Sourdough Bread", 180, 4, True)
    recipe2 = Recipe("Matcha Cookies", 45, 12, False)

    print("--- BEFORE ACTION ---")
    print("Object 1 State:")
    recipe1.display_recipe_details()
    print()
    print("Object 2 State:")
    recipe2.display_recipe_details()
    print("\n" + "="*40 + "\n")

    print("Performing actions on Object 1 (Sourdough Bread)...")
    recipe1.adjust_servings(8)
    recipe1.mark_as_favorite()
    print("\n" + "="*40 + "\n")

    print("--- AFTER ACTION ---")
    print("Object 1 State (Updated):")
    recipe1.display_recipe_details()
    print()
    print("Object 2 State (Updated):")
    recipe2.display_recipe_details() 