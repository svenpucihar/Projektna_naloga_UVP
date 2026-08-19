import os
import requests
import time

#Funkcije za prenos HTML strani iz spletne strani in shranjevanjedatotek v mapo 'strani/'

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )
}

mapa_strani = "strani"


#Funkcija, ki prenese HTML vsebino ene strani z oglasi in jo vrne kot niz

def pridobi_stran(url):
    try:
        odgovor = requests.get(url, headers=HEADERS, timeout=10)
        odgovor.raise_for_status()
        return odgovor.text
    except requests.RequestException as napaka:
        print("Napaka pri pridobivanju", url, ":", napaka)
        return None


#Shrani HTML niz v datoteko znotraj mape strani/

def shrani_stran(html, ime_datoteke):
    os.makedirs(mapa_strani, exist_ok=True)
    pot = os.path.join(mapa_strani, ime_datoteke)
    f = open(pot, "w", encoding="utf-8")
    f.write(html)
    f.close()


#Prenese stevilo podstrani z oglasi in jih shrani

def pridobi_vse_strani(osnovni_url, stevilo_strani):
    for i in range(1, stevilo_strani + 1):
        url = osnovni_url + str(i) + "/"
        print("Prenasam stran", i)
        html = pridobi_stran(url)
        if html:
            shrani_stran(html, "stran_" + str(i) + ".html")
        time.sleep(1)  #premor, pred obremenitvijo streznika