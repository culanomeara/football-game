# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random

teams = []
game_team = ""

class Team:
    def __init__(self, name, defence, attack, stamina, skill, injury, form):
        self.name = name
        self.defence = defence
        self.attack = attack
        self.stamina = stamina
        self.skill = skill
        self.injury = injury
        self.form = form


t1 = Team("Liverpool", 0, 0, 0, 0, 0, 0)
t2 = Team("PSG", 0, 0, 0, 0, 0, 0)
t3 = Team("Man City", 0, 0, 0, 0, 0, 0)
t4 = Team("Chelsea", 0, 0, 0, 0, 0, 0)
t5 = Team("Bayern Munich", 0, 0, 0, 0, 0, 0)
t6 = Team("Real Madrid", 0, 0, 0, 0, 0, 0)
t7 = Team("Juventus", 0, 0, 0, 0, 0, 0)
t8 = Team("Glasgow Celtic", 0, 0, 0, 0, 0, 0)
t9 = Team("Barcelona", 0, 0, 0, 0, 0, 0)
t10 = Team("Benfica", 0, 0, 0, 0, 0, 0)



def intro():
    """
    Tell the team what the game is about.
    """
    print("                     Welcome to Football Stars                   ")
    print("         The game that puts you 90 minutes away from glory       ")
    print("You select your team. The team has randomly assigned attributes")
    print("     Start the match and choose actions as the game plays out")
    print("         The outcome depends on your team attributes")

    ready_game = validate_str(input("Are you ready?"), "y", "n")
    display_teams()
    


def display_teams():
    """
    Display 5 random teams for user to choose from
    """
    

    (
        first_team,
        second_team,
        third_team,
        fourth_team,
        fifth_team,
    ) = random.sample(
        {
            t1,
            t2,
            t3,
            t4,
            t5,
            t6,
            t7,
            t8,
            t9,
            t10,
        },
        5,
    )

    teams = [first_team, second_team, third_team, fourth_team, fifth_team]
    print(f"Team 1: {first_team.name}")
    print(f"Team 2: {second_team.name}")
    print(f"team 3: {third_team.name}")
    print(f"team 4: {fourth_team.name}")
    print(f"team 5: {fifth_team.name}")
    
    game_team_num = validate_int(1, 5)
    global game_team
    game_team = teams[game_team_num - 1]
   
    print(f"You have chosen {game_team.name}")
    """print(f"His current form is {form}")
     generate_stats()
    print("The team stats are: Defence {} " )"""


def validate_int(int1, int2):
    """
    Validates input and gives error message if invalid
    """
    low = int1
    high = int2

    while True:
        try:
            user_choice = int(input("Please make your choice: "))
            assert low <= user_choice <= high
        except ValueError:
            print("Not a number! Please enter a number.")
        except AssertionError:
            print(f"Please enter a number between {low} and {high}")
        else:
            return user_choice
def validate_str(user, str1, str2)   
    user_input = user
    valid1=str1
    valid2=str2
    while True:
        if user_input = 'y':
            print("You pick up the slab and begin reading.")
            break
        elif pick == 'no':
            print("You walk forwards and land facefirst onto the slab.")
            break
        else:
            print("You have to choose Yes or No")

        

intro()

