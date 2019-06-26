#Write a function game() number-guessing game, that takes 2 int parameters defining the range.
# Using some kind of random function to generate random int from the range.
# While user input isn't equal that number, print "Try again!". If user guess the number, congratulate him and exit.

def game(min,max):
    inp = ''
    for i in range(min,max,1):
        while True:
          message = "This is guess game. Please guess number from {0} to {1}"
          print(message.format(min,max))
          inp = int(input("enter number:"))
          if (i == inp):
              break

int1 = int("Enter minimal :")
int2 = int("Enter maximal :")
game (int1,int2)

