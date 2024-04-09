class Book:
    def __init__(self, title, author, category, quantity = 5):
        self.title = title
        self.author = author
        self.category = category
        self.quantity = quantity #5 by default
        self.availability = True

    #print out the info
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Category: {self.category}, Quantity: {self.quantity}, Availability: {self.availability}"

    def rent_book(self):
        if self.availability and self.quantity > 0: #checks if there is any available and if the quanitiy is over 0
            self.quantity = self.quantity - 1 #if so then remove a book from the quantity
            if self.quantity == 0: #if there is no books
                self.availability = False #set to false and then unable to be rented
                return "There are no more books available"
            #this prints weird
            #return self.title, " has been rented."

            return f"{self.title}, has been rented"
        else:
            #return "Book cannot be rented."
            return None

class Library:
    def __init__(self):
        self.books = [] #array of books

    #appends books into array
    def add_book(self, title, author, category, quantity):
        new_book = Book(title, author, category, quantity)
        self.books.append(new_book)

    #search by input
    def search_book(self, input):
        for book in self.books:
            #check if the book user input is in the array through the author, title, or category
            if input.lower() in [book.author.lower(), book.title.lower(), book.category.lower()]:
                return book
        #return "Book not found"
        return None #have to have None because a message will still ask to rent even if the book doesnt exist then crash


def main():
    library = Library() #calling library class
    library.add_book("The greatest book of all time", "Leonardo Pereira", "Comedy", 5)
    library.add_book("Book the second", "Steve", "Fantasy", 5)

    print("Library")
    for book in library.books:
        print(book)

    print()

    while True:
        book_input = input("(e to exit), Enter author of book, title of book, or category of book: ")
        user_book_search = library.search_book(book_input)

        if book_input.lower() == "e":
            print("Thank you for using the library")
            break

        if user_book_search:
            print("Book found:")
            print(user_book_search)
            choice = input("Rent the book? (y/n): ")
            if choice.lower() == "y":
                print(user_book_search.rent_book()) #rents book user asked to rent if they say yes
            else:
                print("Book not rented")
        else:
            print("No book found")
#this calls the main so the program can run, without this program doesnt work
if __name__ == "__main__":
    main()
