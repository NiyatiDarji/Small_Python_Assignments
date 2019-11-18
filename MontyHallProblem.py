# The program solve the Monty Hall Problem

import random
print("The program solve the Monty Hall Problem")

loose = 0
win = 0

try:
    simulations = int(input("Please enter how many simulations you want to try:"))
    prizes = ["Car","TV","Nothing"]

    for index in range(simulations):
        random.shuffle(prizes)              # shuffel the prizes behind the doors
        door_no = random.randrange(3)   # select the index of prize randomly. Will be guessed by the player

        if prizes[door_no] != "Nothing":
            win = win + 1
        else:
            loose = loose + 1
    winning_percent = (win*100)/simulations
    loosing_percent = (loose*100)/simulations

    print("The player will get a prize", winning_percent,"of the time")
    print("The player will get nothing", loosing_percent,"of the time")
except:
    print("Invalid input. Please enter an integer number")