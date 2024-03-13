#!/usr/bin/env python3
#Author: (ops445) Group 1 

import random

def get_player_choice():
    while True:
        player_choice = input("Select your input! (Is it rock, Is it paper, or Is it scissors): ").lower()
        if player_choice in ['rock', 'paper', 'scissors']:
            return player_choice
        else:
            print("Oops! That's not a valid choice. Please choose rock, paper, or scissors.")

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    player_choice = get_player_choice()
    
    print("You chose:", player_choice)
    print("The computer chose:", computer_choice)
    print(determine_winner(player_choice, computer_choice))
    print("Thanks for playing!")

if __name__ == "__main__":
    print("Welcome to the Rock, Paper, Scissors game!")
    play_game()

