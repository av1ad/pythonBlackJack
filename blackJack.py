# Player 1
# Player 2
# Each start with a random card
# Player 1 can choose to draw a card or stay
# Player 2 can choose to draw a card or stay
# If player 1 stays, player 2 can draw a card or stay
# Whoever is closest to 21 wins
# If you exceed 21, you bust or lose.
# If you stay, you cannot draw a card anymore

# If player picks a king, jack, queen it equalsa 10
# If  player picks an ace it's a 1 or 11.

import random

playerOne = "Player 1"
playerTwo = "Player 2"

cards = ["Diamond", " Spade", "Heart", "Club"]
ranks = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
cardValues = {"King": 10, "Queen": 10, "Ace": [1, 11], "Jack": 10}

def pick_card():
