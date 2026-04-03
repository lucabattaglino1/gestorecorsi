import flet as ft

from model.model import Model

# lista di metodi che regolano come si comporta l'interfaccia

class Controller:
    def __init__(self, view):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = Model()
        self._ddCodinsValue = None # è nullo fin che quacuno non lo riempie

    # oltre al self metto sempre e(evento del pulsante)
    # recupera dall'interfaccia qual'è il periodo idadattico
    # faccio la query al database e stampa i dati
    def handlePrintCorsiPD(self, e):
        self._view.txt_result.controls.clear()
        pd = self._view.ddPD.value #recupero il periodo didattico ( I o II)
        # devo convertirlo in numeri però cioè 1 o 2

        #controllo che ci sia un numero
        if pd is None:
            self._view.create_alert("Attenzione, selezionare un periodo didattico")
            self._view.update_page()
            return

        #se super il controllo so che pd = 1 o 2
        if pd == "I":
            pdInt = 1
        else:
            pdInt = 2

        # a questo punto ho tutto per fare la query

        # getCorsiPD è un metodo del model che prende il periodo didattico
        # questo metodo chiederà poi al dao di fare la query
        corsiPD = self._model.getCorsiPD(pdInt)

        # controllo che la lista non sia vuota
        if not len(corsiPD):
            self._view.txt_result.controls.append(ft.Text(f"Nessun corso trovato per il {pd} periodo didattico"))
            self._view.update_page()
            return

        # se arrivo qui vuol dire che ci sono corsi nella lista
        self._view.txt_result.controls.append(ft.Text(f"Di seguito i corsi del {pd} periodo didattico"))
        for c in corsiPD:
            self._view.txt_result.controls.append(ft.Text(c))

        self._view.update_page()



    def handlePrintIscrittiCorsiPD(self, e):
        self._view.txt_result.controls.clear()
        pd = self._view.ddPD.value  # recupero il periodo didattico ( I o II)
        # devo convertirlo in numeri però cioè 1 o 2

        # controllo che ci sia un numero
        if pd is None:
            self._view.create_alert("Attenzione, selezionare un periodo didattico")
            self._view.update_page()
            return

        # se super il controllo so che pd = 1 o 2
        if pd == "I":
            pdInt = 1
        else:
            pdInt = 2

        # a questo punto ho tutto per fare la query

        # getCorsiPD è un metodo del model che prende il periodo didattico
        # questo metodo chiederà poi al dao di fare la query
        corsi = self._model.getCorsiPDwiscritti(pdInt)

        # controllo che la lista non sia vuota
        if not len(corsi):
            self._view.txt_result.controls.append(ft.Text(f"Nessun corso trovato per il {pd} periodo didattico con dettaglio iscritti:"))
            self._view.update_page()
            return

        # se arrivo qui vuol dire che ci sono corsi nella lista
        self._view.txt_result.controls.append(ft.Text(f"Di seguito i corsi del {pd} periodo didattico con dettaglio iscritti:"))
        for c in corsi:
            self._view.txt_result.controls.append(
                ft.Text(f"{c[0]} -- N Iscritti: {c[1]}"))

        self._view.update_page()

    def handlePrintIscrittiCodins(self, e):
        self._view.txt_result.controls.clear()
        if self._ddCodinsValue is None:
            self._create_alert("Perfavore selezionare un insegnamento")
            self._view.update_page()
            return

        # se arrivo qui posso recuperare gli studenti
        studenti = self._model.getSTudentiCorso(self._ddCodinsValue.codins)

        if not len(studenti):
            self._view.txt_result.controls.append(
                ft.Text("Nessuno studente iscritto al corso}"))
            self._view.update_page()
            return

        self._view.txt_result.controls.append(
            ft.Text(f"Di seguito gli studenti iscritti sl corso {self._ddCodinsValue}"))

        for s in studenti:
            self._view.txt_result.controls.append(ft.Text(s))

        self._view.update_page()

    def handlePrintCDSCodins(self, e):
        self._view.txt_result.controls.clear()
        if self._ddCodinsValue is None:
            self._create_alert("Perfavore selezionare un insegnamento")
            self._view.update_page()
            return

        cds = self._model.getCDSofCorso(self._ddCodinsValue.codins)

        if not len(cds):
            self._view.txt_result.controls.append(
                ft.Text(f"Nessun CDS afferente al corso {self._ddCodinsValue}"))
            self._view.update_page()
            return

        self._view.txt_result.controls.append(
            ft.Text(f"Di seguito i CDS che frequentano il corso {self._ddCodinsValue}"))

        for c in cds:
            self._view.txt_result.controls.append(ft.Text(f"{c[0]} -- N Iscritti {c[1]}"))

        self._view.update_page()

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