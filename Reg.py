from kivy.uix.screenmanager import  Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import Connexion_to_Database


class RegPage(Screen):
    def btn2(self):
        email = self.ids.email.text
        sql = "SELECT email FROM testeur WHERE email = %s"
        Connexion_to_Database.Fetch.c.execute(sql, (email,))
        email_in_base = Connexion_to_Database.Fetch.c.fetchall()
        print(email_in_base) #'''Vérifier que le mail n'est pas n'existe dans la base de donnée'''
        # for em in email_in_base:
        if (email,) in email_in_base:
            popup = Popup(title='Nope bro', content=Label(text='Cette adress existe déja'),
                          size_hint=(None, None), size=(400, 200),
                          auto_dismiss=True)
            popup.open()

        else:
            val = (self.ids.user.text, self.ids.prenom.text, self.ids.email.text, self.ids.password.text)
            sql = "INSERT INTO testeur (user,prenom,email,password) VALUES (%s,%s,%s,%s)"
            Connexion_to_Database.Fetch.c.execute(sql, val)
            Connexion_to_Database.Fetch.mydb.commit()

            popup = Popup(title='Inscription validé', content=Label(text='Vous avez etais enrengistre'),
                          size_hint=(None, None), size=(400, 200),
                          auto_dismiss=True)
            popup.open()
