from kivy.uix.screenmanager import ScreenManager, Screen
import mysql.connector
import Connexion_to_Database as cb


class LogPage(Screen):
    def btn1(self):
        user = self.ids.user.text
        password = self.ids.password.text
        etat = self.ids.etat
        if user == '' or password == '':
            etat.text = "[color=#FF0000] Entrer votre Nom d'utilisateur / mot de passe"
        else:
            if user == 'admin' and password == 'admin':
                self.manager.current = 'AdminDash'
            elif user == 'admin' and not(password == 'admin'):
                etat.text = '[color=#FF0000] Mot de passe inccorect '
            else:

                sql = "SELECT user,password,email FROM testeur WHERE user = %s "
                adr = (user,)
                cb.Fetch.c.execute(sql, adr)
                myresult = cb.Fetch.c.fetchall()

                if myresult == []:
                    etat.text = '[color=#FF0000] Utilisateur / mot de passe incorrect '
                else:
                    if password == myresult[0][1]:
                        self.manager.current = "Account"
                    else:
                        etat.text = '[color=#FF0000] mot de passe incorrect '
