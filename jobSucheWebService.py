import requests

headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "ru,de-DE;q=0.9,de;q=0.8,ru-US;q=0.7,en-US;q=0.6,en;q=0.5",
        "Connection": "keep-alive",
        "Origin": "https://www.arbeitsagentur.de",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "X-API-Key": "jobboerse-jobsuche",
    }
def gets_angebots(ort, umkreis):
    url_title = "https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/jobs"
    params = {
        "angebotsart": 4,
        "ausbildungsart": 0,
        "was": "Anwendungsentwicklung",
        "wo": str(ort),
        "umkreis": int(umkreis),
        "page": 1,
        "size": 25,
        "pav": "false",
        "facetten": "false"
    }

    response_title = requests.get(url_title, headers=headers, params=params)
    return response_title.json()


def gets_beschreibungs(kundennummerhash):
    url = "https://rest.arbeitsagentur.de/vermittlung/ag-darstellung-service/pc/v1/arbeitgeberdarstellung/" + kundennummerhash
    response_description = requests.get(url, headers=headers)
    return response_description.json()




