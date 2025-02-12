import angebotsFactory


print("Willkommen beim Jobparser als Azubi Fachinformatiker/in - Anwendungsentwicklung.")
ort_angebot = input("Stadt? : ")
umkreis_angebot = input("Umkreis?(km) : ")
result = angebotsFactory.build_angebots(ort_angebot, umkreis_angebot)

for item in result:
    print(item.to_string())













