import random

def name_to_number(name):
    if name == 'rock':
        number = 0
    elif name == 'Spock':
        number = 1
    elif name == 'paper':
        number = 2
    elif name == 'lizard':
        number = 3
    elif name == 'scissors':
        number = 4
    else:
        print('Invalid Name')
    return number


def number_to_name(number):
    if number == 0:
        name = 'rock'
    elif number == 1:
        name = 'Spock'
    elif number == 2:
        name = 'paper'
    elif number == 3:
        name = 'lizard'
    elif number == 4:
        name = 'scissors'
    else:
        print('Invalid Number')
    return name

def rpsls(player_choice): 
    print("")    
    print("Player's Choice:"+player_choice)
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(4)
    comp_choice = number_to_name(comp_number)
    print("Computer's Choice:"+comp_choice)
    diff=(comp_number-player_number)%5
    print(diff)
    if diff == 1 or diff == 2:
        print("Computer Wins!!!")
    elif diff == 3 or diff == 4:
        print("Player Wins!!!")
    else:
        print("Game Tied!!!")
        
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")