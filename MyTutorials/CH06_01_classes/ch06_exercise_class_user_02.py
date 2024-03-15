
class UserAdmin():

    def __init__(self, user_name, user_login):
        self.user_name = user_name
        self.__user_login = user_login

        self.__user_data = {
                          "user_name" : self.user_name,
                          "user_login" : self.__user_login,
                          "user_id_type": "1" ,
                          "user_type": "Administrator",
                          "user_permissions": ['Management', "Updater", "Seller"],
                          "user_secure_word": "help --admin" 
                         }
        
    def get_user_data(self, user_name, user_login):
        if user_name == self.user_name and user_login == self.__user_login:
            return self.__user_data
        else:
            return 'You are not allowed.'

    def set_user_login(self, user_name, user_login):
        if user_name == self.user_name and user_login == self.__user_login:
            self.__user_login =input("What is your new password?")
            self.__user_data['user_login']= self.__user_login
            return f"{self.user_name}: Tu contraseña ha sido cambiada por {self.__user_login}"
        else:
            return 'You are not allowed.'
               
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

        self._user_data = {
                          "user_name" : self.user_name,
                          "user_login": self.user_login,
                          "user_id_type": "3" ,
                          "user_type": "Invoicer",
                          "user_permissions": ["Seller"]
                         }    
        
    @property
    def user_data(self):
        return self._user_data

    @user_data.setter
    def user_data(self, value):
        self._user_data = value

    @user_data.deleter
    def user_data(self):
        del self._user_data 

usuario_1 = UserAdmin(user_name= 'Alba',user_login= 'Gxwmm55')   
print(usuario_1.get_user_data(user_name= 'Alba',user_login= 'Gxwmm55'))
print(usuario_1.get_user_data(user_name= 'Rocio',user_login= 'Gxwmm55'))
new_login = usuario_1.set_user_login(user_name= 'Alba',user_login= 'Gxwmm55')
print(new_login)
print(usuario_1.get_user_data(user_name= 'Alba',user_login= 'newpass'))

usuario_2 = UserUpdaters(user_name= 'Rocio',user_login= 'Sllxxxbb5')   
print(usuario_2.user_data)

usuario_3 = UserInvoicers(user_name= 'Estibaliz',user_login= 'Ysfma77dk')   
print(usuario_3.user_data)

usuario_3.user_data = 3
print(usuario_3.user_data)
# del usuario_3.user_data
# print(usuario_3.user_data)