class Book:
   def __init__(self, title , author , pages):
        self.title = title
        self.author =  author
        self.pages = pages

   def description(self):
        print(f"title = {self.title}\n author = {self.author}\n pages = {self.pages}")

        

book1 = Book("things fall apart","chinua achebe", 600)
book1.description()

print()

book2 = Book("my sweetest mother", "monday gift", 350,)
book2.description() 