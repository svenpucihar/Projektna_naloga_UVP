import sys
import os

from pridobivanje_strani import pridobi_vse_strani, mapa_strani
from izluscevanje_podatkov import preberi_shranjeno_stran, izlusci_oglase
from shranjevanje_podatkov import shrani_v_csv


osnovni_url = "https://www.nepremicnine.net/oglasi-prodaja/slovenija/stanovanje/"
stevilo_strani = 50

def main():
    ne_poberi = len(sys.argv) > 1 and sys.argv[1] == "ne_poberi"
    if not ne_poberi:
        pridobi_vse_strani(osnovni_url, stevilo_strani)

    vsi_oglasi = []
    for ime_datoteke in sorted(os.listdir(mapa_strani)):
        html = preberi_shranjeno_stran(ime_datoteke)
        vsi_oglasi.extend(izlusci_oglase(html))

    shrani_v_csv(vsi_oglasi)


if __name__ == "__main__":
    main()