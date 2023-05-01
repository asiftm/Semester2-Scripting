import random


plays = ["rock", "paper", "scissors"]


def check_valid(value):
    if value in plays:
        return True
    return False


def random_play():
    play = random.randint(0, 2)
    print(f"PC plays: {plays[play]}")
    return play


def check_winner(player, cpu):
    if player == cpu:
        print(f"Tie! Both players played '{plays[cpu]}'")
        return 0
    elif (player == 2 and cpu == 1) or (player == 1 and cpu == 0) or (player == 0 and cpu == 2):
        print("USER WINS!")
        return 1
    else:
        print("PC3 WINS!")
        return 2


def game(num):
    print(f"\nGame {num+1}\n---")
    winner = 0
    while winner == 0:
        player = input("Insert your entry: ")
        while not check_valid(player):
            player = input("Invalid entry, please insert a valid entry: ")
        winner = check_winner(plays.index(player), random_play())
    return winner-1


if __name__ == '__main__':
    user = 0
    cpu = 0
    num = int(input("How many matches do you want to play? "))
    for i in range(num):
        win = game(i)
        if win == 0:
            user += 1
        else:
            cpu += 1

    if user > cpu:
        winner = "User"
    else:
        winner = "PC"

    print(f"\n---\nThe Overall winner is {winner}!\nUser won {user} time(s), on average {user/(user+cpu)*100}%\n"
          f"PC won {cpu} time(s), on average {cpu/(user+cpu)*100}%")
