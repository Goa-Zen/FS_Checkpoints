class Article:

    def __init__(self, item_reference, item_name, item_pvp, item_description):
        self.item_reference = item_reference
        self.item_name = item_name
        self.item_pvp = item_pvp
        self.item_description = item_description

        self.item_main = {
            "item_reference" : item_reference,
            "item_name" : item_name,
            "item_pvp" : item_pvp,
            "item_description" : item_description
        }

    def __str__(self):
        return f"REFERENCIA\t {self.item_reference}\n" \
               f"NOMBRE\t\t {self.item_name}\n" \
               f"PVP\t\t {self.item_pvp}\n" \
               f"DESCRIPCIÓN\t {self.item_description}\n"
        

class Book(Article):

    def insert_book_details(self, **kwargs):
        book_attr = dict(kwargs.items())
        self.book_attr = book_attr
        self.item_main['item_atributtes'] = self.book_attr
        # print(self.item_main)



class Library:

    def __init__(self):
        self.books_store = {}
        

    def add_book(self, books_store_new):
        self.books_store[books_store_new['item_reference']] = books_store_new
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

#-------------------------------------------------------
        
class Users:

    def __init__(self, user_name, user_login):
        self.user_name = user_name
        self._user_login = user_login


    def register(self):
        if self.user_name != '' and self._user_login != '':
            raise NotImplementedError("Subclass must implement register method")
    
    @property
    def user_login(self):
          raise NotImplementedError("Subclass must implement register method")

        
class UserAdmin(Users):

    def register(self):
        self.user_data = {
                          "user_name" : self.user_name,
                          "user_login": self._user_login,
                          "user_id_type": "1" ,
                          "user_type": "Administrator",
                          "user_permissions": ['Management', "Updater", "Seller"],
                          "user_secure_word": "help --admin" 
                         }

    @property
    def user_login(self):
        return self._user_login

        


class UserUpdaters(Users):

    def register(self):
        self.user_data = {
                          "user_name" : self.user_name,
                          "user_login": self._user_login,
                          "user_id_type": "2" ,
                          "user_type": "Updater",
                          "user_permissions": [ "Updater", "Seller"]
                         }    
        
    @property
    def user_login(self):
        return self._user_login

class UserInvoicers(Users):

    def register(self):
        self.user_data = {
                          "user_name" : self.user_name,
                          "user_login": self._user_login,
                          "user_id_type": "3" ,
                          "user_type": "Invoicer",
                          "user_permissions": ["Seller"]
                         }    

    @property
    def user_login(self):
        return self._user_login


#-------------------------------------------------------
    
class DictionaryFormatter:

    def __init__(self, dictionary):
        lista =[]
        for key, value in dictionary.items():
            lista.append(f'{key.upper()}\t {value}\n ')
            print(f'{key.upper()}\t {value}\n ')


        self.str_dictionary = "  ".join(lista)
        

#-------------------------------------------------------

usuario_1 = UserAdmin(user_name= 'Alba',user_login= 'Gxwmm55')   
usuario_1.register()
# print(usuario_1.user_data(user_name= 'Alba',user_login= 'Gxwmm55'))
print(usuario_1.user_login )

usuario_2 = UserUpdaters(user_name= 'Rocio',user_login= 'Sllxxxbb5')   
usuario_2.register()
print(usuario_2.user_data)

usuario_3 = UserInvoicers(user_name= 'Estibaliz',user_login= 'Ysfma77dk')   
usuario_3.register()
print(usuario_3.user_data)



texto = DictionaryFormatter(usuario_1.user_data)
print(texto.str_dictionary)


first_book = Book(item_reference = 'A/B/2024-2000',
                  item_name = 'Fiesta',
                  item_pvp = 17.5,
                  item_description = "Libro de Ernest Hemingway"
                )
# print(first_book.item_main)
first_book.insert_book_details(book_name = 'Fiesta',
                               book_author = 'Ernest Hemingway',
                               book_pages = "150",
                               book_publisher = "Pan Books"
                               )




second_book = Book(item_reference = 'A/B/2024-2001',
                  item_name = 'Romeo and Juliet',
                  item_pvp = 27.5,
                  item_description = "Libro de W. Shakespeare"
                )
# print(second_book.item_main)
second_book.insert_book_details(book_name = 'Romeo and Juliet',
                               book_author = 'William Shakespeare',
                               book_pages = "156",
                               book_publisher = "Letra Minúscula"
                              )

# print(first_book.item_main)
# print(second_book.item_main)


third_book = Book(item_reference = 'A/B/2024-2002',
                  item_name = 'Damian',
                  item_pvp = 22,
                  item_description = "Libro de Herman Hess"
                )

third_book.insert_book_details(book_name = 'Damian',
                               book_author = 'Herman Hess',
                               book_pages = "136",
                               book_publisher = "Pan Books"
                              )

fourth_book = Book(item_reference = 'A/B/2024-2003',
                   item_name = 'The Hobbit',
                   item_pvp = 29,
                   item_description = "Libro de J.R.R. Tolkien"
                  )

fourth_book.insert_book_details(book_name = 'The Hobbit',
                                book_author = 'J.R.R. Tolkien',
                                book_pages = "269",
                                book_publisher = "Letra Minúscula"
                               )
# print(second_book.book_description)

# print(str(first_book))
# print(repr(first_book))




libreria = Library()
libreria.add_book(first_book.item_main)
libreria.add_book(second_book.item_main)
libreria.add_book(third_book.item_main)
libreria.add_book(fourth_book.item_main)

print('Contenido de libreria')
print(libreria.books_store)
# Si sobre escribo first_book
# libreria.books_store ={"nothing": "nothing to show"}

stock_libreria = libreria.list_of_books()
print(stock_libreria)






        
list_of_books = stock_libreria
print(list_of_books)
it = Iterator(list_of_books)
process = iter(it)

print(next(process))
print(next(process))



