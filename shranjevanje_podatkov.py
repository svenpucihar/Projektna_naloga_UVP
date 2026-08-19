import csv

ime_csv = "nepremicnine.csv"


def shrani_v_csv(oglasi, ime_datoteke=ime_csv): #spremenljivko oglasi bos uporabil kasneje
    if not oglasi:
        print("Pazi, CSV ni bil ustvarjen")
        return
    kljuci = oglasi[0].keys()

    f = open(ime_datoteke, "w", newline="", encoding="utf-8")
    pisec = csv.DictWriter(f, fieldnames=kljuci)
    pisec.writeheader()
    pisec.writerows(oglasi)
    f.close()

    print("Shranjenih", len(oglasi), "oglasov v", ime_datoteke)