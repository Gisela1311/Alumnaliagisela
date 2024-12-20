import csv
estudis = {}
with open("Notes_de_tall_d_acc_s_als_estudis_universitaris__convocat_ries_de_juny_2023-actualitat__i_nombre_de_places_20241209.csv", "r", encoding="utf-8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',',)
    for row in spamreader:
        print(row)
        if row[3] not in estudis:
            estudis.setdefault(row[3].replace(",",""), 1) 
        else:
            estudis[row[3]] +=1
lista = list(sorted(estudis.keys()))
with open("estudis.csv", "w", encoding="utf-8") as resultado:
    for i, e in enumerate(lista):
        resultado.write(f"{i},{e}\n")
