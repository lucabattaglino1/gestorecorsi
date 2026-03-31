from dataclasses import dataclass

# DTO associato alla tabella Corso
# mi serivirà nel DAO per appendere un oggetto corso e non codins

# inserisco tutti i campi del corso

# metodi eq e hash devono sempre esserci

@dataclass
class Corso:
    codins: str
    crediti: int
    nome: str
    pd: int

    # comparazione tra le chiavi
    def __eq__(self, other):
        return self.codins == other.codins

    def __hash__(self):
        return hash(self.codins)

    # qui ritorno una stringa dell'insegnamento
    def __str__(self):
        return f"{self.nome} ({self.codins}) - {self.crediti} CFU"