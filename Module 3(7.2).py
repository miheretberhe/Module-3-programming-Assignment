#Miheret Gebrehans
# Programing assignment 7.2
#It's a guessing game.
#15 September 2025

guess_me =7
number=1
while True:
    if number < guess_me:
        print("too low!")
    elif number == guess_me:
        print("found it!")
    else:
        print("oops")
        break
    number +=1
