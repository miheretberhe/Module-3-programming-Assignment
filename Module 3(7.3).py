#Miheret Gebrehans
#Programing assignment 7.3
#this program loops though numbers 0 to 9 and compares each number to 5. 
#15 September 2025

guess_me = 5
for number in range(10):
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it!")
        break
    else:
        print("oops")
        break