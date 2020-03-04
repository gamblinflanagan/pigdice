print("\n")
import random

die1 = 0
score1 = 0
score2 = 0
decision = ""

print("Pig Dice")
print('''die rolls a number between 1 and 6
the number rolled gets added to the players score
the player can choose between rolling or holding
if the player chooses to hold it is the next players turn
if the player rolls a 1 his or her score is reset to 0
first player reach a score of 100 wins\n''')

while decision != "quit":
 
	print("player1's turn")
	decision = input("enter roll to roll enter hold to hold or quit to quit ")
	
	if decision == "quit":
		break

	print("\n")

	while decision == "roll":
		die1 = random.randint(1, 6)
		print("die1:     " + str(die1))

		if die1 != 1:
			score1 = score1 + die1
		else:
			score1 = 0

		print("\n")
		print("player1: ", score1)
		print("player2: ", score2)
	
		if die1 == 1:
			break
	
		if score1 == 100:
			print("player1 wins!!!")
			break
		decision = input("enter roll to roll enter hold to hold ")
		print("\n")


	print("player2's turn ")
	decision = input("enter roll to roll enter hold to hold or quit to quit ")
	print("\n")

	while decision == "roll":
            die1 = random.randint(1, 6)
            print("die1:     " + str(die1))

            if die1 != 1:
                score2 = score2 + die1
            else:
                score2 = 0

            print("\n")
            print("player1: ", score1)
            print("player2: ", score2)

            if die1 == 1:
                break
            if score2 == 100:
                print("player2 wins!!!")
                break	

            decision = input("enter roll to roll enter hold to hold ")
            print("\n\n\n")
print("\n\n\n")