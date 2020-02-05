from random import randint

def guesseNumber():
    randNumber = randint(1,9)
    # print(randNumber)
    while True:
        try:
            userNumber = int(input("Try to guesse a random number 1-9!: "))
        except ValueError:
            print("Be sure to input a number")
            continue
        if(userNumber == randNumber):
            print(f"Succes you guessed the right number: {randNumber}")
            break
        else:
            print("Darn try again")
            
guesseNumber()