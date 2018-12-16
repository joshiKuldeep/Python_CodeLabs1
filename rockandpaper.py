import random

lst= ['rock', 'paper', 'scissors']

print("hello world")
print("let's play rock, paper, scissors")

def fun(s):
	if(s=='n'):
		return

	print("***************************".center(50))
	print("1".center(50))
	print("2".center(50))
	print("GO".center(50))
	print("***************************".center(50))

	player1= input("Player 1, Enter your input:")
	player1= player1.lower()
	while(not(player1 in lst)):
		player1= input("Player 1, Enter VALID input:").lower()
        	
	player2= input("Player 2, Enter your input:")
	player2= player2.lower()
	while(not(player2 in lst)):
		player2= input("Player 2, Enter VALID input:").lower()
	

	val= random.choice(lst)

	if(val==player1):
		print("Player 1 Wins")
	elif(val==player2):
		print("Player 2 Wins")
	else:
		print("Its a tie, machine predicted value is:", val)
	rTry=input("retry it(Y/N): ")
	rTry=rTry.lower()
	fun(rTry)

fun('y')

