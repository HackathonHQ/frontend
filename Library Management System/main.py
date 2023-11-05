class Library:
    def __init__(self,BooksList):
        self.books=BooksList
    
    def displayBooks(self):
        print('We have the following books:')
        for book in self.books:
            print(" • "+ book)
    pass

class Student:
    pass

if __name__ == "__main__":
    book_titles = ["The Great Gatsby", "To Kill a Mockingbird", "Pride and Prejudice", "The Catcher in the Rye", "Animal Farm", "Lord of the Flies", "One Hundred Years of Solitude", "Crime and Punishment", "The Hobbit"]
    mainLibrary = Library(book_titles)
    mainLibrary.displayBooks()