print("Hello this is a Game of guessing")
print("Basically you type a number from 0 to 100 and if that number matches with a random number in memory you got it right!! if not then try again!!")
from random import randint
var=randint(1,100)
guesslist=[]
difference_list=[]
turn=0
while guess!=var:
    guess=int(input("Enter a number: "))
    difference=abs(guess-var)
    difference_list.append(difference)
    if guess<1 or guess>100:
        print("OUT OF BOUNDS"
        turn+=1
        guesslist.append(guess)
        continue
    elif guess==var:
        guesslist.append(guess)
        continue
    elif difference<=10 and turn==0:
        print("WARM!!")
        guesslist.append(guess)
        turn+=1
        continue
    elif difference>10 and turn==0:
        print("COLD!")
        guesslist.append(guess)
        turn+=1
        continue
    elif difference_list[turn-1]<difference and turn>0:
        print("COLDER")
        guesslist.append(guess)
        turn+=1
        continue
    elif difference_list[turn-1]>difference and turn>0:
        print("WARMER")
        guesslist.append(guess)
        turn+=1
        continue
else:
    print(f"You guessed it RIGHT!! {guess}")
    print(f"The number stored in memory was {var}")
    print(f"Number of guesses was : {len(guesslist)} ")
