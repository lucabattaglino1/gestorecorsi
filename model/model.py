from database.DAO import DAO


class Model:
    def __init__(self):
        pass

    # metodo per sapere tutti i codici dei corsi
    # ma anche lui non li sa
    # lo chiede perciò al DAO

    # qui ho la lista di stringhe con tutti gli insegnamenti
    def getCodins(self):
        return DAO.getCodins()

    def getAllCorsi(self):
        return DAO.getAllCorsi()