import random
target = random.randint(1, 100)
     
guesses = 0
while True:
    guesses += 1
    userchoice = int(input("Guess the target:"))
    if (userchoice == target):
        print("success : correct Guess!!")
        break
    elif (userchoice < target):
        print("your number was too small. take a bigger guess...!")
    else:
        print("your number was too big. take a smaller guess...!")

print(f"----GAME OVER---- in {guesses} attempt")