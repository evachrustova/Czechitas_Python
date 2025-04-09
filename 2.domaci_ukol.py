import requests
import json

# Vyhledání podle IČO
def hledat_podle_ico():
    ico = input("Zadej IČO subjektu: ").strip()
    url = f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        obchodni_jmeno = data.get("obchodniJmeno", "Neznámé jméno")
        adresa = data.get("sidlo", {}).get("textovaAdresa", "Adresa není k dispozici")
        print(f"\n{obchodni_jmeno}\n{adresa}")
    else:
        print("Zadané informace nelze načíst. Zkontroluj IČO.")

# Vyhledání podle názvu
def hledat_podle_nazvu():
    nazev = input("\nZadej název subjektu: ").strip()

    url = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }
    data = json.dumps({
        "obchodniJmeno": nazev
    })

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        vysledky = response.json()
        subjekty = vysledky.get("ekonomickeSubjekty", [])
        print(f"\nNalezeno subjektů: {vysledky.get('pocetCelkem', 0)}")
        for subjekt in subjekty:
            jmeno = subjekt.get("obchodniJmeno", "Neznámé jméno")
            ico = subjekt.get("ico", "Neznámé IČO")
            print(f"{jmeno}, {ico}")
    else:
        print("Chyba při vyhledávání subjektu podle názvu.")

def main():
    print("Vyber možnost:")
    print("1 - Vyhledat podle IČO")
    print("2 - Vyhledat podle názvu")
    volba = input("Tvoje volba: ")

    if volba == "1":
        hledat_podle_ico()
    elif volba == "2":
        hledat_podle_nazvu()
    else:
        print("Neplatná volba.")


if __name__ == "__main__":
    main()
