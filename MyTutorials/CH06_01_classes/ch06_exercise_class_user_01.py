class Users:

    def __init__(self, user_name, user_login):
        self.user_name = user_name
        self.user_login = user_login


    def register(self):
        if self.user_name != '' and self.user_login != '':
            raise NotImplementedError("Subclass must implement register method")


class UserAdmin():

    def __init__(self, user_name, user_login):
        self.user_name = user_name
        self.user_login = user_login

        self.user_data = {
                          "user_name" : self.user_name,
                          "user_login": self.user_login,
                          "user_id_type": "1" ,
                          "user_type": "Administrator",
                          "user_permissions": ['Management', "Updater", "Seller"],
                          "user_secure_word": "help --admin" 
                         }
        
class UserUpdaters():

    def __init__(self, user_name, user_login):
        self.user_name = user_name
        self.user_login = user_login

        self.user_data = {
                          "user_name" : self.user_name,
                          "user_login": self.user_login,
                          "user_id_type": "2" ,
                          "user_type": "Updater",
                          "user_permissions": [ "Updater", "Seller"]
                         }    

class UserInvoicers():

    def __init__(self, user_name, user_login):
        self.user_name = user_name
        self.user_login = user_login

        self.user_data = {
                          "user_name" : self.user_name,
                          "user_login": self.user_login,
                          "user_id_type": "3" ,
                          "user_type": "Invoicer",
                          "user_permissions": ["Seller"]
                         }    


usuario_1 = UserAdmin(user_name= 'Alba',user_login= 'Gxwmm55')   
print(usuario_1.user_data)

usuario_2 = UserUpdaters(user_name= 'Rocio',user_login= 'Sllxxxbb5')   
print(usuario_2.user_data)

usuario_3 = UserInvoicers(user_name= 'Estibaliz',user_login= 'Ysfma77dk')   
print(usuario_3.user_data)