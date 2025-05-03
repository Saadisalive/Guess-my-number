import random
import time

#pick a muber between 1 and 100
number = random.randint(1,100)

def intro():
    print("May I ask you for your name")

    global name 
    name = input()
    print(name +"We are going to play a game.I am thinking of a number between 1 and 100 ")

    if(number%2==0):
        x = 'even'
    else:
        x = 'odd'
    print("\nThis is an {} number".format(x))
    time.sleep(.5)
    print("Go ahead.Guess!")
def pick():
    guessTaken = 0

    while guessTaken < 6:
        time.sleep(.25)

        enter = input('Guess:')

        try:

            guess = int(enter)
            if guess<=100 and guess>=1:
                guessTaken=guessTaken+1

                if guessTaken<6:
                    if guess<number:
                        print("the guess of the number that you have entered is too low")
                    if guess>number:
                        print("the guess of the number that you have entered is too high")
                    if guess != number:
                        time.sleep(.5)
                        print("Try again!")


                    if guess==number:
                        break
            if guess>100 or guess<1:
                print("silly goose That number isn't in the range")
                time.sleep(.25)
                print("PLease enter a number between 1 and 100")
        except:
            print("I dont think that"+enter+" is a number.Sorry")
    if guess == number:
        guessTaken = str(guessTaken)
        print('good job.{}! You guessed my number in guesses!.'.format(name,guessTaken))

    if guess != number:
        print('nope the number i thinking was',str(number))
playagain = "yes"
while playagain=="yes"or playagain=="y"or playagain=="yes":
    intro()
    pick()
    print("Do you want to play again?")
    playagain= input()