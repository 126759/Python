name = input("What is your Name?")
print(name, ",Lets play the animal themed Hang Man!")

import random
word = random.choice(["dog","cat","mouse","rat","lion","tiger","chicken","elephant"])

guesses = ''

turns = 10

while turns > 0:

    failed = 0
 
    for char in word:
    
        if char in guesses:
            print(char)

        else:
            failed += 1

    

 
    if failed == 0:
        print ("You won")

 
        break

   
    guess = input(" guess a character:")

    guesses += guess

    if guess not in word:

        turns -= 1

        print("Wrong")

        print("You have", + turns, 'more guesses')

        if turns == 0:
            print("You Lose")
