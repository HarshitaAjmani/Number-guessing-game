import random
import math
print("\n************************************************","\n\t LETS PLAY NUMBER GUESSING GAME","\n************************************************")
print("\n\tSelect a Range of Numbers:")
lower = int(input("\nEnter the minimum Number: "))
upper = int(input("Enter the Maximum Number: "))
x = random.randint(lower, upper)
mini_ges = round(math.log(upper - lower + 1, 2))
print("\n\tYou've only ", mini_ges," chances to guess the CORRECT Number!\n")
a=0
for count in range( 0 , mini_ges ) :
    count += 1
    guess = int(input("Your Guess: "))
    if x == guess :
        a=1
        print("\n\t ** CONGRATULATIONS **","You have guessed the correct number in ",count,"trails :-))")
        break
    elif x < guess:
        print(" Your guess is too high! Try again")
    elif x > guess:
        print("Your guess is too low! Try again")

if a == 0:
    print("The correct Number was: ",x,"\n You Failed! GO FISH :[")
