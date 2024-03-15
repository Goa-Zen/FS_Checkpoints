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
        

