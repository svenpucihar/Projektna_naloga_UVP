import os
import re
from bs4 import BeautifulSoup

mapa_strani = "strani"

#Regex vzorci, ki se ponavljajo v oglasih

test_kvadratura = re.compile(r"([\d,]+)\s?m2")
test_sobe = re.compile(r"(\d(?:,\d)?)-sobno")
test_leto = re.compile(r"zgrajen[oa]?\s?l\.\s?(\d{4})")
test_cena = re.compile(r"Cena:\s?([\d\.]+,\d{2})\s?EUR")


#Prebere shranjeno HTML datoteko iz mape strani/

def preberi_shranjeno_stran(ime_datoteke):
    pot = os.path.join(mapa_strani, ime_datoteke)
    f = open(pot, "r", encoding="utf-8")
    vsebina = f.read()
    f.close()
    return vsebina


def izlusci_oglase(html):
    soup = BeautifulSoup(html, "html.parser")
    oglasi = []
    elementi = soup.find_all("div", class_="property-box")

    for element in elementi:
        besedilo = element.get_text(separator=" ", strip=True)
        kvadratura = poisci_prvo(test_kvadratura, besedilo)
        sobe = poisci_prvo(test_sobe, besedilo)
        leto = poisci_prvo(test_leto, besedilo)
        cena = poisci_prvo(test_cena, besedilo)
        lokacija = None
        
        oglasi.append({
            "kvadratura_m2": v_stevilo(kvadratura),
            "sobe": sobe,
            "leto gradnje": leto,
            "cena_eur": cena_v_stevilo(cena),
            "lokacija": lokacija,
        })
    return oglasi


def poisci_prvo(vzorec, besedilo):
    zadetek = vzorec.search(besedilo)
    if zadetek:
        return zadetek.group(1)
    return None


def v_stevilo(vrednost):
    if vrednost is None:
        return None
    return float(vrednost.replace(",", "."))

def cena_v_stevilo(vrednost):
    if vrednost is None:
        return None
    return float(vrednost.replace(".", "").replace(",", "."))

