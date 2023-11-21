import random
import os
os.system("cls")

# 30 verschiedene Gruselgeschichten
gruselgeschichten_liste = [
    "Du hörst leise Schritte hinter dir und fühlst einen eisigen Hauch auf deinem Nacken.",
    "Die Wände dieses Raums sind mit blutigen Handabdrücken bedeckt, die langsam zu verschwimmen scheinen.",
    "Eine unheimliche Puppe sitzt in einer Ecke des Raums und ihre Augen folgen dir, wenn du dich bewegst.",
    "Ein gruseliges Flüstern erfüllt die Luft, und du kannst die Worte nicht verstehen.",
    "Du siehst einen Schatten, der sich im Dunkeln bewegt, aber wenn du hinsiehst, ist nichts dort.",
    "Die Temperatur fällt schlagartig ab, und du siehst deinen Atem in der kalten Luft.",
    "Ein lautes Klopfen dringt aus einer geschlossenen Tür, und niemand ist auf der anderen Seite.",
    "Eine verrostete Schaukel bewegt sich von selbst, hin und her.",
    "Eine tiefe, klagende Stimme hallt in deinen Ohren wider, obwohl niemand in der Nähe ist.",
    "Die Wände des Raums scheinen zu atmen und sich zu bewegen, als ob sie lebendig wären.",
    "Du hörst leise Kinderlachen, obwohl du weißt, dass du alleine bist.",
    "Ein Spiegel zeigt dein verzerrtes Spiegelbild, das dich anstarrt.",
    "Schatten bewegen sich in den Ecken des Raums, aber du kannst nicht erkennen, was sie sind.",
    "Ein mysteriöses Gemälde an der Wand zeigt Szenen aus deinen Albträumen.",
    "Deine Taschenlampe flackert und geht aus, und du bist im Dunkeln gefangen.",
    "Der Boden unter dir scheint nachzugeben, als ob etwas versuchen würde, dich hinunterzuziehen.",
    "Ein seltsames Gefühl der Einsamkeit überkommt dich, als ob du beobachtet wirst.",
    "Die Decke des Raums ist mit zahllosen, glühenden Augen bedeckt, die dich fixieren.",
    "Ein fernes Stöhnen dringt an dein Ohr, und du weißt nicht, woher es kommt.",
    "Du spürst eine eiskalte Hand, die über deinen Arm streicht, obwohl niemand in der Nähe ist.",
    "Ein unheimliches Summen erfüllt den Raum, und du kannst die Ursache nicht erkennen.",
    "Ein merkwürdiges Flackern des Lichts lässt seltsame Schatten auf die Wände tanzen.",
    "Du fühlst, wie etwas unsichtbares durch dich hindurchgeht und dir eine Gänsehaut verpasst.",
    "Eine düstere Gestalt erscheint vor dir, aber sie verschwindet, wenn du blinzelst.",
    "Du hörst das Kratzen von Nägeln an der Tür, als ob etwas versucht, hereinzukommen.",
    "Ein Bild an der Wand zeigt ein verlassenes Kinderzimmer, und du hörst Kinderlachen.",
    "Die Luft wird schwer und drückend, und du hast Schwierigkeiten, zu atmen.",
    "Die Möbel im Raum bewegen sich von selbst, als ob sie ein Eigenleben hätten.",
    "Ein Buch auf dem Tisch öffnet sich von selbst und beginnt, leise vorzulesen.",
    "Eine kalte, unsichtbare Hand greift nach deinem Handgelenk und zieht dich weiter in den Raum.",
    "Ein mysteriöses Flüstern in einer unbekannten Sprache erfüllt den Raum, und du verstehst nichts.",
    
]

# Gruselgeschichten für 50 Räume generieren
gruselgeschichten = {raum: random.choice(
    gruselgeschichten_liste) for raum in range(1, 51)}

# Gruselgeschichte für den Ausgangsraum
ausgangs_raum = random.randint(1, 50)
gruselgeschichten[ausgangs_raum] = "Du hast den Ausgang aus dem Herrenhaus gefunden. Glückwunsch!"

# Zielraum generieren
zielraum = random.randint(1, 50)
gruselgeschichten[zielraum] = "Herzlichen Glückwunsch! Du hast das Ziel erreicht. You win!"

# Gruselgeschichte
print("Willkommen im gruseligen Text-Adventure!")
print("Du befindest dich in einem alten, verlassenen Herrenhaus. Es wird erzählt, dass dieses Herrenhaus von einem Geist heimgesucht wird.")
print("Deine Aufgabe ist es, das Herrenhaus zu erkunden und einen Weg nach draußen zu finden, ohne den Geist zu begegnen.")

# Startposition des Spielers
spieler_raum = 1

# Position des Geists (zufällige Raumnummer innerhalb eines Radius von 10 Räumen)
geist_radius = 10
geist_raum = random.randint(
    max(1, spieler_raum - geist_radius), min(50, spieler_raum + geist_radius))

# Spiel-Loop
while True:
    # Aktuelle Raum-Beschreibung anzeigen
    print(f"Du befindest dich in Raum {spieler_raum}.")

    # Anzeigen des Geiststandorts
    print(f"Der Geist befindet sich in Raum {geist_raum}.")

    # Gruselgeschichte für den aktuellen Raum anzeigen
    print(gruselgeschichten.get(spieler_raum,
          "Du befindest dich in einem dunklen Raum. Es ist unheimlich."))

    # Prüfen, ob der Geist den Spieler erreicht hat
    if spieler_raum == geist_raum:
        print("Der Geist hat dich gefunden! Du bist tot.")
        break

    # Prüfen, ob der Spieler den Ausgangsraum erreicht hat
    if spieler_raum == ausgangs_raum:
        print("Du hast den Ausgang aus dem Herrenhaus gefunden. Glückwunsch! Du hast überlebt.")
        break

    # Prüfen, ob der Spieler den Zielraum erreicht hat
    if spieler_raum == zielraum:
        print("Herzlichen Glückwunsch! Du hast das Ziel erreicht. You win!")
        break

    # Benutzereingabe einlesen
    eingabe = input(
        "Wohin möchtest du gehen? (Norden/Süden/Osten/Westen/beenden): ").lower()

    # Bewegungsrichtungen definieren
    bewegungen = {
        "norden": -10,
        "süden": 10,
        "osten": 1,
        "westen": -1
    }

    # Prüfen, ob die Eingabe gültig ist
    if eingabe in bewegungen:
        bewegung = bewegungen[eingabe]
        neue_raum = spieler_raum + bewegung

        # Stelle sicher, dass der Spieler sich im Bereich 1-50 bewegt
        neue_raum = max(1, min(50, neue_raum))

        # Anzeigen des Bewegungsvorgangs und Zielraums
        print(
            f"Du gehst nach {eingabe.capitalize()} und betrittst Raum {neue_raum}.")

        spieler_raum = neue_raum

        # Aktualisiere die Geistposition (zufällige Bewegung des Geists innerhalb des Radius)
        geist_raum = random.randint(
            max(1, spieler_raum - geist_radius), min(50, spieler_raum + geist_radius))
    elif eingabe == "beenden":
        print("Spiel beendet.")
        break
    else:
        print("Ungültige Eingabe. Bitte wähle eine Richtung oder 'beenden'.")
        
        
        
        
        
     
