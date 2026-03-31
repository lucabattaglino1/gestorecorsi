
import flet as ft

from UI.controller import Controller
from UI.view import View

# solitamente non si tocca

def main(page: ft.Page):
    v = View(page) #creo view a cui passo una pagina
    c = Controller(v) #creo un controller a cui passo il view
    v.set_controller(c) #dico al view chi è il controller
    v.load_interface() #carico l'interfaccia


ft.app(target = main)
