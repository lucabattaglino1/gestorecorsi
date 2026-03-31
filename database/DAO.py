from database.DB_connect import DBConnect
from model.corso import Corso

# lista di metodi che farà query al database

class DAO():

    # questa è la prima query al database per prendere tutti gli insegnamenti
    @staticmethod
    def getCodins():
        cnx = DBConnect.get_connection() #connessione
        cursor = cnx.cursor(dictionary=True) #creo cursore

        # query scritta su DBVEAR
        query = """select codins
                    FROM corso"""

        cursor.execute(query) #eseguo la query

        # ciclo su cursore per leggere i dati
        # li inserisco in una lista
        res = []
        for row in cursor:
            res.append(row["codins"]) #codins è il nome della colonna nel database


        cursor.close() # chiudo cursore
        cnx.close() # restituisco connessione
        return res # return della lista

    # qui leggo tutto l'intero corso per intero e non solo codins
    # riempo il dropdown non con le stringhe ma con gli oggetti
    @staticmethod
    def getAllCorsi():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        # con l'asterisco leggo tutto
        query = """select * FROM corso"""

        cursor.execute(query)

        # facendo un append di un oggetto corso
        # mi devo creare nel modello un DTO Corso
        # cosi appendo l'oggetto corso e avrò una lista di oggetti corso
        res = []
        for row in cursor:
            res.append(Corso(
                codins = row["codins"],
                crediti = row["crediti"],
                nome = row["nome"],
                pd = row["pd"]
            ))


        cursor.close()
        cnx.close()
        return res