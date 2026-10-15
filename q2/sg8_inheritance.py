class Publication: #creating parent class
    
    def __init__(self, title: str, author: str): 
        self.__title = title
        self.__author = author
    
    def set_title(self, title: str):
        self.__title = title
        self.set_title(title)
    
    def set_author(self, author: str):
        self.__author = author
        self.set_author(author)
    
    def get_title(self):
        return f"Title: {self.title}"
    
    def get_author(self):
        return f"Author: {self.author}"
    
    def display_info(self): #display information about the publication
        print(f"Title: {self.__title}")
        print (f"Author: {self.__author}")

class Book(Publication): #creating child class called Book that inherits from Publication
    
    def __init__(self, title: str, author: str, number_of_pages: int):
        super().__init__(title, author)
        self.__number_of_pages = number_of_pages
        if number_of_pages < 0:
            print("Number of pages must be a positive number.")
    def get_number_of_pages(self):
        return f"Number of Pages: {self.__number_of_pages}"
    
    def set_number_of_pages(self, number_of_pages: int):
        if number_of_pages > 0:
            self.__number_of_pages = number_of_pages
        else:
            print("Number of pages must be a positive number.")
    
    def display_info(self): #display information about the book
        super().display_info()
        print(f"Number of Pages: {self.__number_of_pages}")


class Magazine(Publication): #creating child class called Magazine that inherits from Publication
    
    def __init__(self, title: str, author: str, issue_number: int):
        super().__init__(title, author)
        self.__issue_number = issue_number

    def get_issue_number(self):
        return f"Issue Number: {self.__issue_number}"
    
    def set_issue_number(self, issue_number: int):
        self.__issue_number = issue_number
        self.set_issue_number(issue_number)
    
    def display_info(self): #display information about the magazine
        super().display_info()
        print(f"Issue Number: {self.__issue_number}")
    

#Creating objects
pub1 = Publication("Journal of experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)

#Displaying information
print("Publication Information:")
pub1.display_info()

print("\nBook Information:")
book1.set_number_of_pages(-310)
book1.display_info()

print("\nMagazine Information:")
mag1.display_info()

