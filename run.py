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
    view_players()

def view_players():
    """
    Display 5 random players for player to choose from
    """
    

intro()