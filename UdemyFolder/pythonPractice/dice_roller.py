from random import randint
#Set # of dice and # of sides to an integer
dice_number = int(input("How many dice are we rolling?"))
dice_sides = int(input("How many sides on each die?"))
#If user inputs data, print a pipe and for each die then generate a random # between 1 and the number of sides. 
while True:
    result =  "|"
    for die in range(dice_number):
#So, if there are 6 sides, generate a random ## b/w 1-6
        rand = randint(1, dice_sides)
        #result is reset to equal | + the random integer generated above followed by |
        result += f"{rand}|"
    print(result)
    reply = input("Roll again? (press q to quit)")
    if reply == "q":
        break
    