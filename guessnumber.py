#guess number
import random 
guessestaken=0
print("hello, what's your name?")
myname= input()
number=random.randint(1,20)
print("well " +myname+  " i'm thinking of number between 1 and 20")
while guessestaken<6:
  guess=input()
  guess=int(guess)
  guessestaken=guessestaken+1
  if guess<number:
    print('your guess is too low')
  if guess>number:
    print('your guess is too hight')
  if guess==number:
   break
if guess==number:
  guessestaken=str(guessestaken)
  print('good job, '+myname+' you guessed mynumber in '+guessestaken+' guesses !')
if guess!=number:
  number=str(number)
  print('nope, the number i was thinking of was '+number)
