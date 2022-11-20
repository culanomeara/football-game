# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
import sys
import math
from stopwatch import Stopwatch
#https://pypi.org/project/stopwatch.py/
# Argument specifies decimal precision for __str__
# e.g 2 digits = 1.00, 3 digits = 1.000
# Optional, defaults to 2
# stopwatch = Stopwatch(2) # Start a stopwatch
# It's just math with time.perf_counter() so there isn't really a task
# running in background

#stopwatch.stop() # Stop stopwatch, time freezes
#stopwatch.start() # Start it again
#stopwatch.reset() # Reset it back to 0
#stopwatch.restart() # Reset and start again
#stopwatch.running # Whether stopwatch is running
#stopwatch.duration # Get the duration (in seconds)
#str(stopwatch) # Get a friendly duration string

GAME_TEAM = ""
COMPUTER_TEAM = ""
event_times = []
match_clock = 0

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
    print("""
    Welcome to Football Stars
    The game that puts you 90 minutes away from glory
    You select your team. The team has randomly assigned attributes
    Start the match and choose actions as the game plays out
    The outcome depends on your team attributes \n
    """)

    ready_game = validate_str(
        "Ok to continue? (y=Yes, n=No, x=Exit) ", "y", "n", "x"
        )
    if ready_game == 'y':
        start_game()
    else:
        sys.exit("You want to just chill here? Bye then")

    
def start_game():
    display_teams()
    generate_stats(GAME_TEAM, COMPUTER_TEAM)
    match_start()


def display_teams():
    """
    Display 5 random teams for user to choose from
    """
    print("\nSelect one of the following 5 teams \n")
    (
        first_team,
        second_team,
        third_team,
        fourth_team,
        fifth_team,
        sixth_team,
        seventh_team,
        eight_team,
        ninth_team,
        tenth_team
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
        10,
    )

    teams = [first_team, second_team, third_team, fourth_team, fifth_team, 
             sixth_team, seventh_team, eight_team, ninth_team, tenth_team]
    print(f"Team 1: {first_team.name}")
    print(f"Team 2: {second_team.name}")
    print(f"Team 3: {third_team.name}")
    print(f"Team 4: {fourth_team.name}")
    print(f"Team 5: {fifth_team.name}\n")
    
    game_team_num = validate_int(1, 5)
    global GAME_TEAM
    GAME_TEAM = teams[game_team_num - 1]
    teams.pop(game_team_num - 1)
    opp_team_num = random.randint(0, 8)
    global COMPUTER_TEAM
    COMPUTER_TEAM = teams[opp_team_num]
    
   
    print(f"\nYou have chosen {GAME_TEAM.name} ")
    print(f"and you will play against {COMPUTER_TEAM.name} \n")


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


def validate_str(query, str1, str2, str3):

    valid1 = str1
    valid2 = str2
    valid3 = str3

    while True:
        answer = input(query).lower()
        if answer == valid1:
            return answer
        elif answer == valid2:
            return answer
        elif answer == valid3:
            return answer
        else:
            print(f"You have to choose {str1}, {str2} or {str3}")

def generate_stats(GAME_TEAM, COMPUTER_TEAM):
    current_team = GAME_TEAM
    opp_team = COMPUTER_TEAM
    current_team.defence = random.randint(80, 100)
    current_team.attack = random.randint(80, 100)
    current_team.stamina = random.randint(80, 100)
    current_team.skill = random.randint(80, 100)
    current_team.injury = random.randint(3, 10)
    current_team.form = random.randint(3, 10)
    opp_team.defence = random.randint(80, 100)
    opp_team.attack = random.randint(80, 100)
    opp_team.stamina = random.randint(80, 100)
    opp_team.skill = random.randint(80, 100)
    opp_team.injury = random.randint(3, 10)
    opp_team.form = random.randint(3, 10)

    print(f"""
    TEAM STATS FOR {current_team.name.upper()}:
    Defence(Max 100): {current_team.defence}
    Attack(Max 100): {current_team.attack}
    Stamina(Max 100): {current_team.stamina}
    Skill(Max 100): {current_team.skill}
    Injury Proneness(Max 10): {current_team.injury}
    Curent Form(Max 10): {current_team.form}""")

    print(f"""
    TEAM STATS FOR {opp_team.name.upper()}:
    Defence(Max 100): {opp_team.defence},
    Attack(Max 100): {opp_team.attack}
    Stamina(Max 100): {opp_team.stamina}
    Skill(Max 100): {opp_team.skill}
    Injury Proneness(Max 10): {opp_team.injury}
    Curent Form(Max 10): {opp_team.form}""")


def match_start():
    start_choice = validate_str("Kick off?"
                                " y=Kick Off,"
                                " n=restart game,"
                                " x=Exit", "y", "n", "x")
    if start_choice == 'y':
        kick_off()
    elif start_choice == 'n':
        print("We're just going to restart the game so...")
        intro()
    else:
        sys.exit("You don't want to kick off? That makes me sad :( ")

def kick_off():
    global event_times
    events()
    #show_timer()

def events():
    event_times = [sorted(random.sample(range(1, 90), 5))]
    print(event_times)

def show_timer():
    global match_clock
    event_times = sorted(random.sample(range(1, 90), 5))
    print(event_times)
    stopwatch = Stopwatch(0)
    match_time = str(stopwatch)
    match_clock = 1
    for match_time in range(match_clock, 91):
        if match_time == event_times[0]:
            print("scene 1")
            stopwatch.stop()
            match_clock = match_time
            print(match_clock)
            continue
        elif match_time == event_times[1]:
            print("scene 2")
            stopwatch.stop()
            match_clock = match_time
            print(match_clock)
            continue
        else:
            print("oops")



show_timer()


