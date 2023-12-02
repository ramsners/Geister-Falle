class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class World1:
    def __init__(self):
        self.rooms = {
            'start': Room('Start', 'Du befindest dich am Anfang des Abenteuers.'),
            'left_path': Room('Linker Pfad', 'Ein dunkler Pfad erstreckt sich nach links.'),
            'right_path': Room('Rechter Pfad', 'Ein heller Pfad führt nach rechts.'),
            'secret_room': Room('Geheimzimmer', 'Du entdeckst ein verborgenes Zimmer mit glänzenden Objekten.')
            # Füge hier weitere Räume hinzu, je nach Bedarf
        }
        self.current_room = self.rooms['start']

    def look_around(self):
        print(f'Du schaust dich um im Raum "{self.current_room.name}".')
        print(self.current_room.description)

    def move(self, direction):
        if direction == 'forward':
            self.move_forward()
        elif direction == 'left':
            self.move_left()
        elif direction == 'right':
            self.move_right()
        elif direction == 'back':
            self.go_back()
        else:
            print("Ungültige Eingabe. Bitte wähle erneut.")

    def move_forward(self):
        print("Du bewegst dich vorwärts.")
        # Implementiere hier die Logik für die Bewegung nach vorne
        # z.B., self.current_room = self.rooms['neuer_raum']

    def move_left(self):
        print("Du bewegst dich nach links.")
        # Implementiere hier die Logik für die Bewegung nach links
        # z.B., self.current_room = self.rooms['neuer_raum']

    def move_right(self):
        print("Du bewegst dich nach rechts.")
        # Implementiere hier die Logik für die Bewegung nach rechts
        # z.B., self.current_room = self.rooms['neuer_raum']

    def go_back(self):
        print("Du gehst zurück.")
        # Implementiere hier die Logik für die Rückkehr
        # z.B., self.current_room = self.rooms['neuer_raum']

    def choose_action(self):
        print("Welche Aktion möchtest du durchführen?")
        print("1. Bewegen")
        print("2. Umschauen")
        print("3. Interagieren")

        choice = input("Deine Wahl (1/2/3): ")

        if choice == "1":
            direction = input("In welche Richtung möchtest du dich bewegen? (forward/left/right/back): ")
            self.move(direction)
        elif choice == "2":
            self.look_around()
        elif choice == "3":
            self.interact()
        else:
            print("Ungültige Eingabe. Bitte wähle erneut.")

    def interact(self):
        print("Du interagierst mit der Umgebung.")
        # Implementiere hier die Logik für die Interaktion
        # z.B., self.current_room.interact()

# Hier kannst du dann den eigentlichen Ablauf starten, z.B.:
def start_afterlife():
    print("Willkommen zu 'Afterlife'!")
    print("Du öffnest die Augen und findest dich in einer mysteriösen Welt wieder, die zwischen Leben und Tod liegt.")
    print("Ein sanftes, diffuses Licht umgibt dich, während deine Umgebung langsam Form annimmt.")
    print("Du erkennst, dass du nicht mehr unter den Lebenden weilst, sondern im Afterlife gelandet bist – einer Welt jenseits der Grenzen des Bekannten.")
    print("Plötzlich taucht eine geisterhafte Figur vor dir auf, mit einem leuchtenden Schimmer um sich.")
    print("'Reisender,' spricht die Gestalt mit einer schwebenden Stimme, 'du bist in der Zwischenwelt gefangen. Doch es gibt einen Weg zurück ins Leben.'")
    print("Du erfährst, dass du vor eine Wahl gestellt wirst – eine Reise durch das Afterlife, um Antworten zu finden oder den Weg zurück ins Leben zu suchen.")
    print("'Möge deine Entscheidung das Gleichgewicht zwischen Leben und Tod beeinflussen.'")
    print("Die Figur verschwindet, und du stehst vor einem Pfad, der in die Dunkelheit führt.")
    print("Dein Abenteuer im Afterlife beginnt.")

start_afterlife()

world = World1()

while True:
    world.choose_action()
