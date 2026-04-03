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

    def getCorsiPD(self, pd):
        return DAO.getCorsiPD(pd)

    def getCorsiPDwiscritti(self, pd):
        # do un'ordinazione per iscritti decrescente
        result = DAO.getCorsiPDwIscritti(pd)
        result.sort(key = lambda s:s[1], reverse=True)
        return result

    def getStudentiCorso(self,codins):
        studenti = DAO.getStudentiCorso(codins)
        studenti.sort(key=lambda s:s.cognome)
        return studenti

    def getCDSofCorso(self,codins):
        cds = DAO.getCDSofCorso(codins)
        cds.sort(key=lambda c:c[1], reverse=True)
        return cds