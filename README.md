# Jobparser: Automatisierte Analyse von Ausbildungsstellen für Fachinformatiker/in – Anwendungsentwicklung

Dieses Python-Skript durchsucht automatisch die Stellenangebote der Bundesagentur für Arbeit nach Ausbildungsplätzen für Fachinformatiker/in in der Anwendungsentwicklung. Es extrahiert dabei wichtige Informationen wie:

- **Berufsbezeichnung**
- **Unternehmen**
- **Standort**
- **Straße**
- **Veröffentlichungsdatum**
- **Entfernung zum angegebenen Ort**
- **Stellenbeschreibung**

Die gesammelten Daten werden strukturiert in einer Excel-Datei gespeichert, um eine einfache Analyse zu ermöglichen.

## Hauptfunktionen

- **Datenextraktion**: Verwendung der `requests`- und `BeautifulSoup`-Bibliotheken zum Sammeln und Parsen von HTML-Daten von der Website der Arbeitsagentur.
- **Anpassbare Parameter**: Möglichkeit zur Festlegung der Anzahl der zu verarbeitenden Seiten, des Speicherpfads für die Datei und der HTTP-Header.
- **Export nach Excel**: Speicherung der Ergebnisse im XLSX-Format mit Hilfe der `pandas`-Bibliothek, was das Sortieren und Filtern der Daten erleichtert.
![image](https://github.com/user-attachments/assets/839d0667-8917-4391-b9a8-2050cdea42e4)
