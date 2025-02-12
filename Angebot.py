import jobSucheWebService
class Angebot:
    def __init__(self, title, arbeitgeber, ort, strasse, date, entfernung,description):
        self.title = title
        self.arbeitgeber = arbeitgeber
        self.ort = ort
        self.strasse = strasse
        self.date = date
        self.entfernung = entfernung
        self.description = description

    def to_string(self):
        if self.strasse:
            strasse_str = f'\nStrasse: {self.strasse}'
        else:
            strasse_str = ''

        self.description = f'\nBeschreibung: \n{self.description}' if self.description else ''



        return (f'''
Beruf: {self.title}Arbeitgeber: {self.arbeitgeber}
Ort:{self.ort}{strasse_str}
Veröffentlichungsdatum:{self.date}
Entfernung von der ausgewählten Stadt: {self.entfernung}KM
{self.description}''')

