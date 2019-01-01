import collections

class Library:
    def __init__(self):
        self.books = []

    def addbook(self, book):
        self.books.append(book)

    def based_on_isbn(self, isbn):
        b_o_isbn = []
        for book in self.books:
            if book.ISBN == isbn:
                b_o_isbn.append(book)
        return b_o_isbn

    def based_on_author(self, author):
        b_o_author = []
        for book in self.books:
            if book.author == author:
                b_o_author.append(book)
        return b_o_author


    def list_books(self):
        for book in self.books:
            print(book)


    def no_of_books(self):
        print("number of books: {}".format(len(self.books)))


    def cost_replace(self, cost):
        for i in range(len(self.books)):
            if (self.books[i].price) > 15:
                print(self.books[i].price)
                self.books[i]=self.books[i]._replace(price=15)
                print(self.books[i].price)

    def remove_book(self, book_name):
        for book in self.books:
            if book.name == book_name:
                self.books.remove(book)

def main():
    Book = collections.namedtuple('Book', 'name author ISBN price')
    library = Library()
    library.addbook(Book('Geometry', 'Jeff Potter', '0596805888', 22))
    library.addbook(Book('Math', 'George Harr', '0594805888', 15))
    library.addbook(Book('English', 'James Odd', '0596225888', 10))
    library.addbook(Book('Physics', 'Jeff Potter','0597884512', 18))
    #library.no_of_books()
    #library.list_books()
    #library.cost_replace(15)
    #library.list_books()
    library.remove_book('English')
    library.list_books()
    #print(library.based_on_isbn('0594805888'))
    #print(library.based_on_author('Jeff Potter'))


if __name__ == '__main__':
    main()






