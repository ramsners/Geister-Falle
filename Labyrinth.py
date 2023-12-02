import random

class Labyrinth:
    def __init__(self, breite, hoehe):
        self.breite = breite
        self.hoehe = hoehe
        self.spielfeld = [['W'] * breite for _ in range(hoehe)]
        self.start = (0, 0)
        self.ende = (hoehe - 1, breite - 1)
        self.position = self.start
        self._generiere_labyrinth()

    def _generiere_labyrinth(self):
        stack = [self.start]
        besucht = set()
        besucht.add(self.start)
        
        while stack:
            x, y = aktuell = stack[-1]
            nachbarn = [
                (x-2, y), (x+2, y),
                (x, y-2), (x, y+2)
            ]
            nachbarn = [(nx, ny) for nx, ny in nachbarn if 0 <= nx < self.hoehe and 0 <= ny < self.breite and (nx, ny) not in besucht]
            
            if nachbarn:
                nx, ny = ziel = random.choice(nachbarn)
                besucht.add(ziel)
                stack.append(ziel)
                
                # Wand entfernen
                self.spielfeld[(x + nx) // 2][(y + ny) // 2] = 'O'
                self.spielfeld[nx][ny] = 'O'
            else:
                stack.pop()

        self.spielfeld[self.start[0]][self.start[1]] = 'S'
        self.spielfeld[self.ende[0]][self.ende[1]] = 'E'

    def zeige_umgebung(self):
        x, y = self.position
        umgebung = {
            'n': self.spielfeld[x-1][y] if x > 0 else 'W',
            's': self.spielfeld[x+1][y] if x < self.hoehe-1 else 'W',
            'w': self.spielfeld[x][y-1] if y > 0 else 'W',
            'o': self.spielfeld[x][y+1] if y < self.breite-1 else 'W'
        }
        return umgebung

    def bewegen(self, richtung):
        dx, dy = 0, 0
        if richtung == 'n':
            dx = -1
        elif richtung == 's':
            dx = 1
        elif richtung == 'w':
            dy = -1
        elif richtung == 'o':
            dy = 1

        nx, ny = self.position[0] + dx, self.position[1] + dy
        if 0 <= nx < self.hoehe and 0 <= ny < self.breite and self.spielfeld[nx][ny] == 'O':
            self.position = (nx, ny)

def spiel_starten():
    lab = Labyrinth(11, 11)  # Ungrade Zahlen gewährleisten einen Weg durch das Labyrinth
    print("Du befindest dich in einem mysteriösen Labyrinth. Dein Ziel ist es, den Ausgang 'E' zu finden.")
    print("Du startest am Eingang 'S'.")
    while lab.position != lab.ende:
        umgebung = lab.zeige_umgebung()
        print(f"\nDu siehst um dich herum: Norden-{umgebung['n']}, Süden-{umgebung['s']}, Westen-{umgebung['w']}, Osten-{umgebung['o']}.")
        richtung = input("In welche Richtung möchtest du gehen? (n/s/w/o) ")
        lab.bewegen(richtung)
    print("\nGlückwunsch! Du hast das Labyrinth verlassen!")

spiel_starten()

