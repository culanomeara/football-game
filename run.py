# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import sys
import os
import random
import time

class Player:
  def __init__(self, name, defence, attack, stamina, skill, injury, luck):
    self.name = name
    self.defence = defence
    self.attack = attack
    self.stamina = stamina
    self.skill = skill
    self.injury = injury
    self.luck = luck

p1 = Player("Mbappe", 0,0,0,0,0,0)
p2 = Player("Messi", 0,0,0,0,0,0)
p3 = Player("Ronaldo", 0,0,0,0,0,0)
p4 = Player("Salah", 0,0,0,0,0,0)
p5 = Player("Haaland", 0,0,0,0,0,0)
p6 = Player("Mane", 0,0,0,0,0,0)
p6 = Player("Benzema", 0,0,0,0,0,0)
p7 = Player("Lewandowski", 0,0,0,0,0,0)
p8 = Player("Neymar", 0,0,0,0,0,0)
p9 = Player("Obafemi", 0,0,0,0,0,0)
p10 = Player("O Meara", 0,0,0,0,0,0)


def intro():
    """
    Tell the player what the game is about.
    """
    print("Welcome to Football Stars")
    print("The game that puts you 90 minutes away from glory")
    print("You select your player. The player has randomly assigned attributes")
    print("Start the match and choose actions as the game plays out")
    print("The outcome depends on your player attributes")

    ready_game = input("Are you ready?")
    print(f"You have said {ready_game}")
    display_players()

def display_players():
    """
    Display 5 random players for player to choose from
    """
    first_player, second_player, third_player, fourth_player, fifth_player = random.sample({p1.name, p2.name, p3.name, p4.name, p5.name, p6.name, p7.name, p8.name, p9.name, p10.name}, 5)
    print(f"Player 1: {first_player}")
    print(f"Player 2: {second_player}")
    print(f"Player 3: {third_player}")
    print(f"Player 4: {fourth_player}")
    print(f"Player 5: {fifth_player}")

intro()