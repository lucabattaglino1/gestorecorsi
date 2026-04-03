from database.DB_connect import DBConnect
from model.corso import Corso
from model.studente import Studente


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

    #metodo che mi dice quali sono i corsi di un certo periodo didattico
    @staticmethod
    def getCorsiPD(pd):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        # con l'asterisco leggo tutto
        query = """select * 
                   FROM corso c
                    WHERE c.pd = %s""" #metto %s perchè sarà un parametro (1 o 2)

        cursor.execute(query, (pd,)) #tupla con periodo didattico che mi arriva dall'esterno

        res = []
        for row in cursor:
            # nel caso in cui il nome delle colonne nel database è uguale al nome delle proprietà
            # dell'oggetto dto posso fare l'unpack della riga
            res.append(Corso(**row))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getCorsiPDwIscritti(pd):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select c.codins, c.crediti, c.nome, c.pd, count(*) as n
                   FROM corso c, iscrizione i
                   WHERE c.codins = i.codins
                    and c.pd = %s
                    group by c.codins, c.crediti, c.nome, c.pd"""

        cursor.execute(query, (pd,))

        res = []
        for row in cursor:
            # appendo una tupla --> corso, intero
            res.append((Corso(codins = row["codins"],
                             crediti = row["crediti"],
                             nome = row["nome"],
                             pd = row["pd"]),
                       row["n"] ))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getStudentiCorso(codins):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select s.*
                   FROM studente s, iscrizione i
                   WHERE s.matricola = i.matricola
                    and i.codins = %s"""

        cursor.execute(query, (codins,))

        # qui riceverò i parametri di uno studente e non di un corso
        # perciò mi creo dto
        res = []
        for row in cursor:
            # unpack studente
            res.append(Studente(**row))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getCDSofCorso(codins):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select s.CDS, count(*) as n
                   FROM studente s, iscrizione i
                   WHERE s.matricola = i.matricola
                    and i.codins = %s
                    and s.CDS != ""
                    group by s.CDS"""

        cursor.execute(query, (codins,))

        # qui riceverò i parametri di uno studente e non di un corso
        # perciò mi creo dto
        res = []
        for row in cursor:
            # tupla
            res.append((row["CDS"], row["n"]))

        cursor.close()
        cnx.close()
        return res