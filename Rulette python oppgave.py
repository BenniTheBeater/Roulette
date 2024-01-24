import random

game = 1
penge = 100

while game:
    if penge > 0:
        nummer = int(input("Tast et lomme nummer fra (0-36): "))
        print(penge)
        bet = int(input("Hvor mye vil du bette? "))
        
        # Dette sjekker om nummeret er fra 0-36 eller ikke
        if 0 <= nummer <= 36:
            # Simulerer et hjulspinn fra 0-36
            wheel_result = random.randint(0, 36)

            color = ""
            if wheel_result == 0:
                color = "grønn"
            elif 1 <= wheel_result <= 10:
                color = "svart" if wheel_result % 2 == 0 else "rød"
            elif 11 <= wheel_result <= 18:
                color = "rød" if wheel_result % 2 == 0 else "svart"
            elif 19 <= wheel_result <= 28:
                color = "svart" if wheel_result % 2 == 0 else "rød"
            elif 29 <= wheel_result <= 36:
                color = "rød" if wheel_result % 2 == 0 else "svart"

            # Viser fargen på valgt nummer
            print("Fargen av lomme nummeret", nummer, " er ", color)

            # Viser resultatet av hjulspinn
            print("Hjulet har landet på nummer:", wheel_result, "som er fargen", color)

            # Sjekker om brukeren har vunnet eller tapt
            if nummer == wheel_result:
                penge += bet * 5 
                print("Gratulerer! Du har vunnet!")
            else:
                penge -= bet
                print("Beklager, du har tapt. Bedre lykke neste gang!")

            play_again = 0

            if nummer == 2:
                play_again = input("spill igjen? Tast Y eller N ").lower()
                if play_again in ("y", "n"):
                    break
                else:
                    print("Ugyldig inntasting, vennligst tast Y eller N")
            
            if play_again == "n":
                print("Hadet på badet din gamle sjokolade!")
                game = 0
        else:
            print("Error: Tallet du tastet er ikke mellom 0-36")
    else:
        print("Få en jobb din fattige person")
        game = 0
