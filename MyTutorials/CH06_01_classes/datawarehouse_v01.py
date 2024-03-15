class Article:

    def __init__(self, item_reference, item_name, item_pvp, item_description):
        self.item_reference = item_reference
        self.item_name = item_name
        self.item_pvp = item_pvp
        self.item_description = item_description

    def __str__(self):
        return f"REFERENCIA\t {self.item_reference}\n" \
               f"NOMBRE\t\t {self.item_name}\n" \
               f"PVP\t\t {self.item_pvp}\n" \
               f"DESCRIPCIÓN\t {self.item_description}\n"
        

class Book():

    def __init__(self, book_name, **kwargs):
        self.book_name = book_name
        book_attr = dict(kwargs.items())
        
        self.book_description = {
            "book_name" : book_name,
            "book_attr" : book_attr
                            }
        # print(self.book_description)
        # self.book_attr = book_attr


    def __str__(self):
        return f"REFERENCIA\t {self.referencia}\n" \
               f"NOMBRE\t\t {self.book_name}\n" \
               f"PVP\t\t {self.pvp}\n" \
               f"DESCRIPCIÓN\t {self.descripcion}\n"
    
    def __repr__(self):
        return f'A nested dictionary with {self.book_name} and the description and {self.book_description}'


class Library:

    def __init__(self):
        self.books_store = {}
        

    def add_book(self, books_store_new):
        self.books_store[books_store_new['book_name']] = books_store_new
        # return self.books_store

    def list_of_books(self):
        lista = []
        print(self.books_store.values())
        for value in self.books_store.values():
            lista.append([value])
        return lista

class Iterator:

    def __init__(self, objects_to_iteract):
        self.object_to_iteract = objects_to_iteract
        self.last_object = (len(self.object_to_iteract) - 1)
        
    def __iter__(self):
        self.n = 0
        return self

    def get_object_num(self, n):
        return self.object_to_iteract[n]
    
    def __next__(self):
        if self.n < self.last_object:
            output = self.get_object_num(self.n)
            self.n += 1
            return output
        elif self.n == self.last_object:
            output = self.get_object_num(self.n)
            self.n = 0
            return output

# cero_book = Article('aaaa',
#                     'nombre', 
#                     25.45, 
#                     "Fiesta"
#                     )
# print(cero_book)
# cero_book_book = Book(book_name = 'Fiesta',
#                       book_author = 'Ernest Hemingway',
#                       book_pages = "150",
#                       book_publisher = "Pan Books"
#                      )
# print(cero_book_book)


first_book = Book(book_name = 'Fiesta',
                  book_author = 'Ernest Hemingway',
                  book_pages = "150",
                  book_publisher = "Pan Books"
                )

# print(first_book.book_description)

second_book = Book(book_name = 'Romeo and Juliet',
                  book_author = 'William Shakespeare',
                  book_pages = "156",
                  book_publisher = "Letra Minúscula"
                )

third_book = Book(book_name = 'Damian',
                  book_author = 'Herman Hess',
                  book_pages = "136",
                  book_publisher = "Pan Books"
                )

fourth_book = Book(book_name = 'The Hobbit',
                  book_author = 'J.R.R. Tolkien',
                  book_pages = "269",
                  book_publisher = "Letra Minúscula"
                )
# print(second_book.book_description)

# print(str(first_book))
# print(repr(first_book))




libreria = Library()
libreria.add_book(first_book.book_description)
libreria.add_book(second_book.book_description)
libreria.add_book(third_book.book_description)
libreria.add_book(fourth_book.book_description)
# print('Contenido de libreria')
# print(libreria.books_store)
# libreria.books_store ={"nothing": "nothing to show"}

stock_libreria = libreria.list_of_books()
# print(stock_libreria)






        
list_of_books = stock_libreria
print(list_of_books)
it = Iterator(list_of_books)
process = iter(it)

print(next(process))
print(next(process))

# Si sobre escribo first_book
# first_book ={'book_name': 'aaaa', 'book_attr': {'book_author': 'bbb', 'book_pages': '150', 'book_publisher': 'ddd'}}
# print(first_book)
