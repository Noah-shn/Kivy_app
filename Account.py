from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
import Connexion_to_Database as cb


class Account(Screen):

    # Affichage des catégories par image dans Account aprés afficher et selectionner les préstations
    # pas sur que RV soit la meilleur solution a revoir rapidement

    def add_icon_item(self):
        My_list = []
        List_to_dict = []
        for x in cb.Fetch.categories:
            for item in x:
                dict = {'key': item, 'text': item}
                List_to_dict.append(dict)

                My_list = List_to_dict

        self.rv.data = [l for l in My_list]
        print(My_list)


class MyButton(Button):
    def get_to(self):

        pass

        #  def print_data(self, text):
        #  print(text)
        # print(categorie)
