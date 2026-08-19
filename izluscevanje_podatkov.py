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

    