# rock paper scissors project test
# WORK ON: if the user inputs a different value than r, p, s
# WORK ON: keeping score of player and computer
# WORK ON: [keeping score] till the user wants to quit
# once the user quits, program displays who the winner is based of points

import random

name = input("Enter Name: ")

r = 'Rock'
p = 'Paper'
s = 'Scissors'

game_list = [r, p, s]
computer = random.choice(game_list)

user_points = 0
computer_points = 0

while True:
    while True:
        user_input = str.lower(input('Pick a choice, rock(r), paper(p), or scissors(s): '))
        if user_input.lower() not in ('r', 'p', 's'):
            print('INVALID ENTRY PLEASE TRY AGAIN')
            continue
        else:
            break

    print("The computer has chosen", computer)

    if user_input == 'r' and computer == s:
        user_points += 1
        print(name, "has won the game!")
    if user_input == 'r' and computer == p:
        computer_points += 1
        print("The computer has won")
    if user_input == 'r' and computer == r:
        print("It's a draw")

    if user_input == 'p' and computer == r:
        user_points += 1
        print(name, "has won the game!")
    if user_input == 'p' and computer == s:
        computer_points += 1
        print("The computer has won")
    if user_input == 'p' and computer == p:
        print("It's a draw")

    if user_input == 's' and computer == p:
        user_points += 1
        print(name, "has won the game!")
    if user_input == 's' and computer == r:
        computer_points += 1
        print("The computer has won")
    if user_input == 's' and computer == s:
        print("It's a draw")

    play_again = str.lower(input('Would you like to play again? (y) or (n): '))
    if play_again.lower == 'y':
        print(name, "has", user_points)
        print("The Computer has", computer_points)
        if user_points > computer_points:
            print(name, "is winning!")
        if computer_points > user_points:
            print("The computer is winning! You're not good at this game!")
    continue

    if play_again.lower() not in ('y'):
        if user_points > computer_points:
            print(name, "has won the game!")
        if computer_points > user_points:
            print("The computer has won! You're not good at this game!")
        break
