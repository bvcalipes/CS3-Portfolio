class Recipe:
    """
    Represents a specific baking or cooking recipe in a digital cookbook application.
    """
    def __init__(self, recipe_name: str, prep_time_minutes: int, servings: int, is_gluten_free: bool):
        #Public attributes
        self.recipe_name = recipe_name
        self.prep_time_minutes = prep_time_minutes

        #Private attributes
        self.__servings = servings
        self.__is_favorite = False

        self.is_gluten_free = is_gluten_free
    
    def display_recipe_details(self) -> None:
        """
        Displays the details of the recipe, including name, preparation time, servings, and gluten-free status.
        """
        fav_status = "Yes" if self.__is_favorite else "No"
        gf_status = "Yes" if self.is_gluten_free else "No"
        print(f"Recipe Name: {self.recipe_name}")
        print(f"Preparation Time: {self.prep_time_minutes} minutes")
        print(f"Servings: {self.__servings}")
        print(f"Gluten-Free: {gf_status}")
        print(f"Favorited: {fav_status}")

    
