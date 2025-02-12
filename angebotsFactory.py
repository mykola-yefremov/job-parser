from Angebot import *
import jobSucheWebService
def build_angebots(ort_angebot,umkreis_angebot):

    angebots = jobSucheWebService.gets_angebots(ort_angebot, umkreis_angebot)
    jobs = []

    for angebot in angebots["stellenangebote"]:

        title = angebot["beruf"]
        arbeitgeber = angebot["arbeitgeber"]
        ort = angebot["arbeitsort"]["ort"]

        try:
            strasse = angebot["arbeitsort"]["strasse"]
        except:
            strasse = ""

        date = angebot["aktuelleVeroeffentlichungsdatum"]
        entfernung = angebot["arbeitsort"]["entfernung"]

        if 'kundennummerHash' in angebot:
            kundennummerhash = angebot['kundennummerHash']
            description = jobSucheWebService.gets_beschreibungs(kundennummerhash)
            try:
                description_str = description['beschreibung']
            except:
                description_str = ""


            angebot_object = Angebot(title, arbeitgeber, ort, strasse, date,entfernung,description_str)
            jobs.append(angebot_object)

    return jobs

