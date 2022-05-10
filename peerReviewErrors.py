# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Tristan Flores
# Creation Date: 5/10/22
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')    
	print() #instead of print(), this line of code should be displayIntro(), as print() will print nothing.
	
def chooseCave():
    cave = ''
	while cave != '1' and cave != '2':      #instead of a while statement, an if statement followed by an else statement is appropiate. 
		print('Which cave will you go into? (1 or 2)')
		cave = input()  #the above print statement will not work as desired, so the string literal should be moved to the input() in the line below def chooseCave().

	return caves

def checkCave(chosenCave):                      #the variable chosenCave has not been created yet. Instead, the definition should read def checkCave().
        print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)                   #sleep has not been defined yet. 
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(3)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)
                                                        #checkCave() should be here in order for the strings to be printed and friendlycave to be assigned a value.

	if chosenCave == str(friendlyCave):             #this if/else block should not be indented, otherwise it will be part of the definition of checkCave.
		print('Gives you his treasure!')
	else:
                print 'Gobbles you down in one bite!'

playAgain = 'yes'                               # Here, the variable playAgain is assigned the string literal 'yes'. Instead, the programmer should use playAgain = input("....").
while playAgain = 'yes' or playAgain = 'y':    
	displayIntro()
	caveNumber = choosecave()
	checkCave(caveNumber)
    
	print('Do you want to play again? (yes or no)') # once again the input() should use the string literal from the print statement, as this bit of code will not work as intended. 
	playAgain = input()                             #also, this block of code should not be indented, except for the final print statement. 
	if playAgain == "no":
		print("Thanks for planing")

