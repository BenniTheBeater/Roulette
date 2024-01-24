import random
import numpy as np

# Lager arrays som inneholder tall.
red = np.array([1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36])
black = np.array([2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35])
odd = np.array([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35])
even = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36])

class Roulettegame:
    def __init__(self):
        self.valg = 0

    def meny(self):
        self.valg = input("Hva vil du gamble på, Jørn? Velg en av disse alternativene: ")
        if self.valg.lower() in ["red", "black", "odd", "even"]:
            self.choose_number(self.valg.lower())
        else:
            print("Neiånei, du må da kunne følge enkle instrukser? Du er jo tross alt en lærer.")

    def choose_number(self, color):
        numbers = red if color == "red" else black if color == "black" else odd if color == "odd" else even
        print(f"Okei, nå velg en av disse tallene: {numbers}")
        chosen_number = int(input("Skriv ditt valgte nummer: "))

colors = {"red": red, "black": black, "odd": odd, "even": even}

game = Roulettegame()
game.meny()

numbers = colors.get(game.valg)
if numbers is not None:
    print(f"Okei, nå kan du velge en av disse tallene: {numbers}")
else:
    print("Bruh, feil igjen?")
