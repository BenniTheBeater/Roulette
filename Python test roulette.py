import random

def print_board(board):
    for row in board:
        print(" ".join(row))

def spin_wheel():
    return random.choice(range(0, 37))

def determine_color(number):
    if number == 0:
        return "green"
    elif 1 <= number <= 10 or 19 <= number <= 28:
        return "red"
    else:
        return "black"

def main():
    board = [["0" for _ in range(12)] for _ in range(3)]
    for i in range(1, 37):
        color = determine_color(i)
        row = (i - 1) // 12
        col = (i - 1) % 12
        board[row][col] = f"{i} ({color})"

    print("Welcome to Roulette!")
    print_board(board)

    while True:
        input("Press Enter to spin the wheel... ")
        result = spin_wheel()
        print(f"The ball landed on {result}")
        color = determine_color(result)
        print(f"The color is {color}")

        bet = input("Enter your bet (number/color): ").lower()
        if bet.isdigit():
            bet = int(bet)
            if bet == result:
                print("Congratulations! You won!")
            else:
                print("Sorry, you lost.")
        elif bet == color:
            print("Congratulations! You won!")
        else:
            print("Sorry, you lost.")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    main()
