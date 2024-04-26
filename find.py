import os
import zipfile

# Funktion zum Finden von gelöschten Zip-Dateien
def finde_geloeschte_zip(dateipfad):
    geloeschte_zip_dateien = []

    # Durchsuche den Dateipfad nach gelöschten Zip-Dateien
    for root, dirs, files in os.walk(dateipfad):
        for file in files:
            if file.endswith(".zip"):
                geloeschte_zip_dateien.append(os.path.join(root, file))

    return geloeschte_zip_dateien

# Funktion zur Auswahl und Wiederherstellung von Zip-Dateien
def wiederherstellen_zip(dateien):
    for index, zip_datei in enumerate(dateien):
        print(f"{index+1}. {zip_datei}")

    auswahl = input("Gib die Nummern der Zip-Dateien ein, die du wiederherstellen möchtest (getrennt durch Leerzeichen): ")
    
    ausgewaehlte_dateien = [dateien[int(i)-1] for i in auswahl.split()]

    for zip_datei in ausgewaehlte_dateien:
        zielverzeichnis = "/zielverzeichnis/"  # Hier den gewünschten Zielordner angeben

        with zipfile.ZipFile(zip_datei, 'r') as zip_ref:
            zip_ref.extractall(zielverzeichnis)
        
        print(f"Die Zip-Datei {os.path.basename(zip_datei)} wurde erfolgreich wiederhergestellt unter {zielverzeichnis}")

# Aufruf der Funktion mit dem gewünschten Dateipfad
dateipfad = "/pfad/zur/festplatte"
gefundene_zip_dateien = finde_geloeschte_zip(dateipfad)

print("Gefundene gelöschte Zip-Dateien:")
wiederherstellen_zip(gefundene_zip_dateien)
