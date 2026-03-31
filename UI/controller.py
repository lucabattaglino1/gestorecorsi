import flet as ft

from model.model import Model

# lista di metodi che regolano come si comporta l'interfaccia

class Controller:
    def __init__(self, view):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = Model()

    # oltre al self metto sempre e(evento del pulsante)
    def handlePrintCorsiPD(self, e):
        pass

    def handlePrintIscrittiCorsiPD(self, e):
        pass

    def handlePrintIscrittiCodins(self, e):
        pass

    def handlePrintCDSCodins(self, e):
        pass

    # metodo per andare a prendere i corsi nel database e caricarli nel view
    def fillddCodins(self):
        # for cod in self._model.getCodins():
        #     self._view.ddCodins.options.append(
        #         ft.dropdown.Option(cod)
        #     )

        # chiede al modello la lista di tutti i codici di insegnamento
        # cicla sulla lista e aggiungi tutti i corsi al dropdown
        for c in self._model.getAllCorsi():
            self._view.ddCodins.options.append(ft.dropdown.Option(
                key = c.codins, # stringa che viene visualizzata nel menu
                data = c, # oggetto vero e proprio che stiamo inserendo nel dropdown
                on_click = self._choiceDDCodins # serve per salvare nel controller la voce selezionata
            ))
            pass

    # leggo la selezione dell'utente e la salvo in una variabile locale
    def _choiceDDCodins(self, e):
        self._ddCodinsValue = e.control.data
        print(self._ddCodinsValue)