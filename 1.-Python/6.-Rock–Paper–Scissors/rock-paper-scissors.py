

import random

gestures = ["rock", "paper", "scissors"]

print("Hello and welcome human! I am the champion of:",gestures, "... wanna challenge me?")

print("""
Just a couple of warnings, human:

1) I am the champion of this game...

2) ... In the universe I mean.

3) I let you choose how many rounds you want to play, BUT PAY ATTENTION:
 - If you will just press Enter without typing anything we cannot play, I don't really care cause I am the champion!
 - If you will enter some Text we cannot play, again I don't really care cause I am the champion!
 - If you will enter a non-INTEGER number, it is rounded to the closest lower INTEGER, I decide cause I am the champion!
""")

#Choice of number of rounds

n_rounds = int(float(input("How many rounds do we want to play? Please type an ODD number: ")))
    
while (n_rounds % 2 != 0) == False:    
    if n_rounds == 0:
        print("\nOk funny human, you want to play",n_rounds," rounds...nice try! But I am the champion in charge, so YOU LOST! \n")
        n_rounds = int(float(input("How many rounds do we want to play? Please type an ODD number: ")))
    elif n_rounds % 2 == 0:
        print(n_rounds,"is even! Math basics missing here... \n")
        n_rounds = int(float(input("How many rounds do we want to play? Please type an ODD number: ")))

print("\nAlright, let's play",n_rounds,"rounds!")

rounds_to_win = int((n_rounds + 1)/2)

print("\nThe player who wins", rounds_to_win,"rounds wins this game!")

cpu_score = 0

player_score = 0

#Functions definition:

def cpu_choice(gestures):
    cpu_gesture = random.choice(gestures)
    return cpu_gesture

def player_choice(gestures):
    player_gesture = input("\nChoose between rock, paper or scissors: ")
    while player_gesture not in gestures:
        print("\nThis is not a gesture of the game... Read and type carefully. Or just stop messing with me, human!")
        player_gesture = input("\nChoose between rock, paper or scissors: ")
    return player_gesture

def check_choice(cpu_gesture,player_gesture):
    result = 0
    if cpu_gesture == player_gesture:
        result = 0
    elif (cpu_gesture == gestures[0] and player_gesture == gestures[2]) or (cpu_gesture == gestures[1] and player_gesture == gestures[0]) or (cpu_gesture == gestures[2] and player_gesture == gestures[1]):
        result = 1
    elif (cpu_gesture == gestures[0] and player_gesture == gestures[1]) or (cpu_gesture == gestures[1] and player_gesture == gestures[2]) or (cpu_gesture == gestures[2] and player_gesture == gestures[0]):
        result = 2
    return result

def round_outcome(cpu_gesture,player_gesture,result):
    print("\nI chose:", cpu_gesture)
    print("\nYOU chose:", player_gesture)
    if result == 0:
        return print("\nIt's a TIE! This is curious...")
    elif result == 1:
        return print("\nI WON huahauh! Too easy!")
    elif result == 2:
        return print("\nYOU WON... pure luck! C'mon, next round I will smash you!")

# Game execution:

rounds_played = 0

while rounds_played < n_rounds and cpu_score < rounds_to_win and player_score < rounds_to_win:
    
    print("I have chosen, now it's up to you! \n")
    
    cpu_gesture = cpu_choice(gestures)
       
    player_gesture = player_choice(gestures)
    
    result = check_choice(cpu_gesture,player_gesture)
    
    round_outcome(cpu_gesture,player_gesture,result)
    
    if result == 0:
        rounds_played += 1
    elif result == 1:
        cpu_score += 1
        rounds_played +=1
    elif result == 2:
        player_score += 1
        rounds_played +=1
    
    print("\nYOUR score is:", player_score, "\n")
    print("MY score is:", cpu_score, "\n")
    print("Rounds left to play in this game:",(n_rounds - rounds_played), "\n")

# Game results

if cpu_score == rounds_to_win or (rounds_played == n_rounds and cpu_score > player_score):
    print("\n I WON THE GAME, loooooooser!")
elif player_score == rounds_to_win or (rounds_played == n_rounds and player_score > cpu_score):
    print("\n YOU WON THE GAME, well...I am still the champion anyway...you need to beat me over 21 rounds to get the title!")
else:
    print("\n WE TIED THE GAME...I can't believe it!")
