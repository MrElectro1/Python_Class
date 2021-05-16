# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
#Eric Hayden 05/14/2021
# This is a typical part of any program
# Author: <author>
# Creation Date: <date>
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()
#5 and #6 there was a spaceing error with cave = '' and it needed to be def chosenCave():
def choosenCave():
	cave = ''
	while cave !='1'and cave !='2':
		print('Which cave will you go into? (1 or 2)')
		cave = input()

#1 Below you put caves rather than cave. sence python reads cave as a veriable caves is read as a seperate veriable than cave
	return cave

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#8 this note below should have been sleep for 3 seconds
	#sleep for 3 seconds
	time.sleep(3)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
#2 You forgot the () in the print function
		print('Gobbles you down in one bite!')

playAgain = 'yes'
#4 you need 2 = sighns not one when using while
while playAgain == 'yes' or playAgain == 'y':
	displayIntro()
#3 and #7 you forgot to capitalize the second C in chooseCave() and it needed to be chosenCave
	caveNumber = choosenCave()
	checkCave(caveNumber)
    
	print('Do you want to play again? (yes or no)')
	playAgain = input()
	#9 you forgot to add the or playAgain == "n"
	if playAgain == "no" or playAgain == "n":
		print("Thanks for planing")

