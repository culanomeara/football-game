import random
import time
import sys
import os
# import keyboard
# import termcolor
# https://github.com/joeyespo/py-getch
from getch import pause

from graphics import game_graphics
from eventdescriptions import event_desc
# from termcolor import colored, cprint

# from threading import Event # Needed for the  wait() method
# from time import sleep 

game_team = ""
computer_team = ""
event_times = []
event_num = 1
no_events = 0
event_types = []
statdiffs = [0, 0, 0]
match_clock = 0
targets = []
outcomes = []
shot_outcome = ''


class Team:
    """
    Set up TEAM class with various attributes
    """
    def __init__(self, name, defence, attack,
                 stamina, skill, form, goals):
        self.name = name
        self.defence = defence
        self.attack = attack
        self.stamina = stamina
        self.skill = skill
        self.form = form
        self.goals = goals


t1 = Team("Liverpool", 0, 0, 0, 0, 0, 0)
t2 = Team("PSG", 0, 0, 0, 0, 0, 0)
t3 = Team("Man City", 0, 0, 0, 0, 0, 0)
t4 = Team("Chelsea", 0, 0, 0, 0, 0, 0)
t5 = Team("Bayern Munich", 0, 0, 0, 0, 0, 0)
t6 = Team("Real Madrid", 0, 0, 0, 0, 0, 0)
t7 = Team("Juventus", 0, 0, 0, 0, 0, 0)
t8 = Team("Inter Milan", 0, 0, 0, 0, 0, 0)
t9 = Team("Barcelona", 0, 0, 0, 0, 0, 0)
t10 = Team("Borrusia Dortmund", 0, 0, 0, 0, 0, 0)


def intro():
    """
    Tell the team what the game is about.
    """
    print(game_graphics[0])
    time.sleep(2)
    os.system("clear")
    print(game_graphics[5])
    pause()
    start_game()


def start_game():
    """
    Clear screen then
    Call game functions:
    To display teams for user
    To randomly generate stats for user team and computer team
    To call match start func
    """
    os.system("clear")
    display_teams()
    generate_stats(game_team, computer_team)
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
    game_team_num = validate_int(1, 2, 3, 4, 5, 0)
    global game_team
    game_team = teams[game_team_num - 1]
    teams.pop(game_team_num - 1)
    opp_team_num = random.randint(0, 8)
    global computer_team
    computer_team = teams[opp_team_num]


def generate_stats(game_team, computer_team):
    """
    Generate stats for both teams and save to team attributes
    """
    current_team = game_team
    opp_team = computer_team
    current_team.defence = random.randint(80, 100)
    current_team.attack = random.randint(80, 100)
    current_team.stamina = random.randint(80, 100)
    current_team.skill = random.randint(80, 100)
    current_team.form = random.randint(3, 10)
    opp_team.defence = random.randint(80, 100)
    opp_team.attack = random.randint(80, 100)
    opp_team.stamina = random.randint(80, 100)
    opp_team.skill = random.randint(80, 100)
    opp_team.form = random.randint(3, 10)
    print(f"\nYou have chosen {game_team.name} ")
    print(f"and you will play against {computer_team.name}\n")
    show_stats = validate_str(
        "Do you want to see the team stats? (y = Yes, n = No, q = Quit) \
            \n", "y", "n", "q")
    os.system('clear')
    if show_stats == 'y':
        print(f"""
        Defence(Max 100):
            {current_team.name}: {current_team.defence}
            {opp_team.name}: {opp_team.defence}
        Attack(Max 100):
            {current_team.name}: {current_team.attack}
            {opp_team.name}: {opp_team.attack}
        Stamina(Max 100):
            {current_team.name}: {current_team.stamina}
            {opp_team.name}: {opp_team.stamina}  
        Skill(Max 100):
            {current_team.name}: {current_team.skill}
            {opp_team.name}: {opp_team.skill}
        Form(Max 10):
            {current_team.name}: {current_team.form}
            {opp_team.name}: {opp_team.form}""")
        pause()
        os.system("clear")
    elif show_stats == 'n':
        return
    else:
        sys.exit("They think it's all over...It is now!")
    # calculate probabilities:
    global statdiffs
    defdiff = int((current_team.defence*current_team.form/10) -
                  (opp_team.attack*opp_team.form/10))
    statdiffs[0] = defdiff
    attdiff = int((current_team.attack*current_team.form/10) -
                  (opp_team.defence*opp_team.form/10))
    statdiffs[1] = attdiff
    skilldiff = int((current_team.skill*current_team.form/10) -
                    (opp_team.skill*opp_team.form/10))
    statdiffs[2] = skilldiff


def match_start():
    """
    If user selects to start match, the game event is called
    If restart game is called, then we restart from beginning of program
    Otherwise, we exit the program
    """
    os.system("clear")
    start_choice = validate_str("Are you ready to kick off? "
                                " y = Kick Off,"
                                " n = restart game,"
                                " x = Exit \n", "y", "n", "x")
    if start_choice == 'y':
        kick_off()
    elif start_choice == 'n':
        print("We're just going to restart the game so...")
        os.system('clear')
        intro()
    else:
        sys.exit("You don't want to kick off? That makes me sad :( ")


def kick_off():
    """
    Function to call game events
    """
    os.system("clear")
    print("Welcome to this European Super League Match")
    print(f"between {game_team.name} and {computer_team.name}")
    time.sleep(2)
    os.system("clear")
    print(game_graphics[4])
    time.sleep(2)
    events()
    time.sleep(2)
    call_event()


def events():
    """
    This generates the various event data:
    First the number of events that user can act on
    Then the match times when these events occur
    Lastly, we randomly decide how many of the events
    are either attack or defend scenarios
    """
    global event_times
    global no_events
    global event_types
    no_events = random.randrange(5, 8)
    event_times = sorted(random.sample(range(1, 90), no_events))
    # attacking event code = 0 defend attack code = 1
    event_choices = (0, 1)
    event_types = random.choices(event_choices, k=no_events)


def call_event():
    """
    Function to call each event, give user options
    and based on user selection, determine an outcome
    then amend scoreboard as necessary
    """
    global event_num
    i = 1
    while i <= no_events:
        os.system("clear")
        print(f"Event {i} of {no_events}")
        eventtype = event_types[event_num-1]
        print(f"Match Time: {event_times[event_num-1]} mins")
        if eventtype == 0:
            attack_play()
            if shot_outcome == 'y':
                game_team.goals += 1
            else:
                game_team.goals += 0
        else:
            defend_play()
            if shot_outcome == 'y':
                computer_team.goals += 1
            else:
                game_team.goals += 0
        if i == no_events:
            print(f"FINAL SCORE: {game_team.name} : {game_team.goals}")
            print(f"             {computer_team.name} : {computer_team.goals}")
            pause()
            start_choice = validate_str("What do you want to do now? "
                                " y = kick off match again,"
                                " n = restart game,"
                                " x = Exit \n", "y", "n", "x")
    if start_choice == 'y':
        os.system('clear')
        kick_off()
    elif start_choice == 'n':
        print("We're just going to restart the game so...")
        os.system('clear')
        intro()
    else:
        sys.exit("You don't want to kick off? That makes me sad :( ")
        else:
            print(f"MATCH SCORE: {game_team.name} : {game_team.goals}")
            print(f"             {computer_team.name} : {computer_team.goals}")
            pause()
        i += 1
        event_num += 1


def attack_play():
    """
    Function called when event is attack type.
    It gives user attacking options and based
    on the choice, calls outcomes
    """
    global shot_outcome
    calc_outcomes(0)
    print("\nATTACK: ")
    attack_desc = random.randrange(0, 4)
    print(f"{game_team.name} {event_desc[attack_desc]}")
    print_delay("> > > > > > >")
    print("\nWhat action are you taking?")
    print("1: Shoot, 2: Pass, 3: Dribble\n")
    user_choice = validate_int(1, 2, 3, 0, 0, 0)
    if user_choice == 1:
        print(f"The {game_team.name} player has decided to shoot")
        print_delay("......")
        print("\n")
        if outcomes[0] == 1:
            shot_outcome = shoot(0)
        else:
            print("He skies it over the bar")
    elif user_choice == 2:
        print(f"The {game_team.name} player has decided to pass")
        print_delay("......")
        print("\n")
        if outcomes[1] == 1:
            shot_outcome = shoot(0)
        else:
            print("The pass is intercepted and the attack breaks down")
    else:
        print(f"The {game_team.name} player has decided to dribble")
        print_delay("......")
        print("\n")
        if outcomes[2] == 1:
            shot_outcome = shoot(0)
        else:
            print("He loses the ball. Bad decision to dribble!")


def defend_play():
    """
    Function called when event is defend type.
    It gives user defending options and based
    on the choice, calls outcomes
    """
    global shot_outcome
    calc_outcomes(1)
    print("\nDEFEND: ")
    def_desc = random.randrange(0, 4)
    print(f"{computer_team.name} {event_desc[def_desc]}")
    print_delay("< < < < < < <")
    print("\nWhat action are you taking?")
    print("1: Tackle, 2: Press, 3: Foul\n")
    user_choice = validate_int(1, 2, 3, 0, 0, 0)
    if user_choice == 1:
        print(f"The {game_team.name} player has decided to tackle")
        print_delay("......")
        print("\n")
        if outcomes[0] == 0:
            shot_outcome = shoot(1)
        else:
            print("What a tackle! He clears the ball")
    elif user_choice == 2:
        print(f"The {game_team.name} player has decided to press the player")
        print_delay("......")
        print("\n")
        if outcomes[1] == 0:
            shot_outcome = shoot(1)
        else:
            print("The pressure tells and the defender stops the attack")
    else:
        print(f"The {game_team.name} player has decided to foul him")
        print_delay("......")
        print("\n")
        if outcomes[2] == 0:
            shot_outcome = shoot(1)
        else:
            print("The ref didn't see the foul and the attacker is raging!")


def shoot(attdef):
    """
    Function that is called when user choice leads to a shot.
    Argument is attdef: att = 0 def = 1
    This calls the related function and prints the related graphic
    and adjusts match score as needed.
    
    """
    calc_targets(attdef)
    os.system("clear")
    usershot = show_targets(attdef)
    os.system("clear")
    if targets[usershot-1] == 1:
        print(game_graphics[1])
        pause()
        os.system("clear")
        goal_yn = 'y'
    else:
        if attdef == 0:
            print(game_graphics[2])
        else:
            print(game_graphics[6])
        pause()
        os.system("clear")
        goal_yn = 'n'
    return goal_yn


def show_targets(attack_defend):
    """
    Function that displays the shot options
    takes input from user and returns that
    """
    print(game_graphics[3])
    time.sleep(2)
    if attack_defend == 0:
        print("\nChance to Shoot: Where are you shooting?\n")
    else:
        print("\nChance to Save: Where are you diving?\n")
    print(" 1: Top Left     2: Top Mid      3: Top Right")
    print(" 4: Low Left  5: Low Mid   6: Low Right")

    usershot = validate_int(1, 2, 3, 4, 5, 6)
    return usershot


def calc_targets(attdef):
    """
    Calculate number of targets that can return a GOAL
    based on previously generated stats and probabilities
    """
    global targets
    i = attdef
    if 16 <= statdiffs[i]:
        usertargets = [1, 1, 1, 1, 1, 0]
    elif 10 <= statdiffs[i] <= 15:
        usertargets = [1, 1, 1, 1, 0, 0]
    elif -9 <= statdiffs[i] <= 9:
        usertargets = [1, 1, 1, 0, 0, 0]
    elif -15 <= statdiffs[i] <= -10:
        usertargets = [1, 1, 0, 0, 0, 0]
    elif statdiffs[i] <= -16:
        usertargets = [1, 0, 0, 0, 0, 0]
    targets = random.sample(usertargets, 6)


def calc_outcomes(attdef):
    """
    Function that randomly decides whether user choice will lead
    to a shot or not.
    Based on statsdiff skill rating.
    Function fills the outcomes global array
    """
    global outcomes
    if attdef == 0:
        if 10 <= statdiffs[2]:
            useroutcomes = [1, 1, 1]
        elif -9 <= statdiffs[2] <= 9:
            useroutcomes = [1, 1, 0]
        elif statdiffs[2] <= -10:
            useroutcomes = [1, 0, 0]
    else:
        if 10 <= statdiffs[2]:
            useroutcomes = [1, 0, 0]
        elif -9 <= statdiffs[2] <= 9:
            useroutcomes = [1, 1, 0]
        elif statdiffs[2] <= -10:
            useroutcomes = [1, 1, 1]
    outcomes = random.sample(useroutcomes, 3)


def print_delay(displaytext):
    """
    Function that allow print text to be printed slowly
    adding to the drama!
    """
    for char in displaytext:
        # https://stackoverflow.com/questions/4627033/how-to-print-a-string-with-a-little-delay-between-the-chars
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.4)


def validate_int(int1, int2, int3, int4, int5, int6):
    """
    Validates integer input and gives error message if invalid
    """
    low = int1
    if int3 == 0:
        high = int2
    elif int4 == 0:
        high = int3
    elif int6 == 0:
        high = int5
    else:
        high = int6
    
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
    """
    Validates string input and gives error message if invalid
    """
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


intro()
