import random
# import time
import sys
# import os

# from threading import Event # Needed for the  wait() method
# from time import sleep 

GAME_TEAM = ""
COMPUTER_TEAM = ""
event_times = []
event_num = 1
no_events = 0
event_types = []
statdiffs = [0, 0, 0]
match_clock = 0
targets = []


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
    """
    Call game functions:
    To display teams for user
    To randomly generate stats for user team and computer team
    To call match start func
    """
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
    
    game_team_num = validate_int(1, 2, 3, 4, 5, 0)
    global GAME_TEAM
    GAME_TEAM = teams[game_team_num - 1]
    teams.pop(game_team_num - 1)
    opp_team_num = random.randint(0, 8)
    global COMPUTER_TEAM
    COMPUTER_TEAM = teams[opp_team_num]
    print(f"\nYou have chosen {GAME_TEAM.name} ")
    print(f"and you will play against {COMPUTER_TEAM.name} \n")


def generate_stats(GAME_TEAM, COMPUTER_TEAM):
    """
    Generate stats for both teams and save to team attributes
    """
    current_team = GAME_TEAM
    opp_team = COMPUTER_TEAM
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

    print(f"""
    TEAM STATS FOR {current_team.name.upper()}:
    Defence(Max 100): {current_team.defence}
    Attack(Max 100): {current_team.attack}
    Stamina(Max 100): {current_team.stamina}
    Skill(Max 100): {current_team.skill}
    Curent Form(Max 10): {current_team.form}""")

    print(f"""
    TEAM STATS FOR {opp_team.name.upper()}:
    Defence(Max 100): {opp_team.defence},
    Attack(Max 100): {opp_team.attack}
    Stamina(Max 100): {opp_team.stamina}
    Skill(Max 100): {opp_team.skill}
    Curent Form(Max 10): {opp_team.form}""")

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
    start_choice = validate_str("Are you ready to kick off?"
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
    """
    Function to call game events
    """
    events()
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
        print(f"Event {i} of {no_events}")
        eventtype = event_types[event_num-1]
        print(eventtype)
        print(f"Match Time: {event_times[event_num-1]} mins")
        if eventtype == 0:
            print("ATTACK: What action are you taking?")
            print("1: Shoot, 2: Pass, 3: Dribble")
            user_choice = validate_int(1, 2, 3, 4, 5, 6)
            print(f"you selected {user_choice}")
            calc_targets(0)
            usershot = show_targets(0)
            if targets[usershot-1] == 1:
                print("GOAL")
                GAME_TEAM.goals += 1
            else:
                print("Miss")
        else:
            print("DEFEND: What action are you taking?")
            print("1: Tackle, 2: Pull shirt, 3: Shoulder")
            user_choice = validate_int(1, 2, 3, 4, 5, 6)
            print(f"you selected {user_choice}")
            calc_targets(1)
            usershot = show_targets(1)
            if targets[usershot-1] == 1:
                print("GOAL")
                COMPUTER_TEAM.goals += 1
            else:
                print("SAVE")
        if i == no_events:
            print(f"FINAL SCORE: {GAME_TEAM.name} : {GAME_TEAM.goals}")
            print(f"             {COMPUTER_TEAM.name} : {COMPUTER_TEAM.goals}")
        else:
            print(f"MATCH SCORE: {GAME_TEAM.name} : {GAME_TEAM.goals}")
            print(f"             {COMPUTER_TEAM.name} : {COMPUTER_TEAM.goals}")

        i += 1
        event_num += 1


def show_targets(attack_defend):
    """
    Function that displays the shot options
    takes input from user and returns that
    """
    if attack_defend == 0:
        print("Chance to Shoot: Where are you shooting?")
    else:
        print("Chance to Save: Where are you diving?")

    print(" 1: Top Left     2: Top Mid      3: Top Right")
    print(" 4: Bottom Left  5: Bottom Mid   6: Bottom Right")

    usershot = validate_int(1, 2, 3, 4, 5, 6)
    return usershot


def calc_targets(attdef):
    """
    Calculate number of targets that nca return a GOAL
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
    print(targets)

# def show_timer():
    """global match_clock
    event_times = sorted(random.sample(range(1, 90), 5))
    print(event_times)

    Event().wait(event_times[0])
    print(f"Here is event {event_times[0]}")
    match_clock = event_times[0]
    print(f"Match time is {event_times[0]}")
    call_scene(0)
    Event().wait(event_times[1]-event_times[0])
    print(f"Here {event_times[1]}")
    print("scene 2")
    print(f"Match time is {event_times[1]}")
    call_scene(1)

    Event().wait(event_times[2]-event_times[1])
    call_scene(2)
    print("scene 3")
    print(f"Match time is {event_times[2]}")

    Event().wait(event_times[3]-event_times[2])
    call_scene(3)
    print("scene 4")
    print(f"Match time is {event_times[3]}")

    Event().wait(event_times[4]-event_times[3])
    call_scene(4)
    print("scene 5")
    print(f"Match time is {event_times[4]}")"""
# https://stackoverflow.com/questions/29082268/python-time-sleep-vs-event-wait


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
