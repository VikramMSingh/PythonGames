from random import randint

o = ["Rock","Paper","Scissor"]

p_name=input("Enter your name ")

comp=o[randint(0,2)]

player=False

while player == False:
	player = input("Rock, Paper, Scissor?")
	if player == comp:
		print("Tie!")
	elif player == "Paper":
		if comp == "Scissor":
			print("%s lost!" %p_name, comp, "cuts", player)
		else:
			print("%s wins!" %p_name ,player,"covers",comp)
	elif player == "Rock":
		if comp == "Scissor":
			print ("%s wins!" %p_name, player, "breaks", comp)
		else:
			print("%s loses!" %p_name, comp, "covers", player)
	elif player == "Scissor":
		if comp == "Rock":
			print("%s loses!" %p_name, comp,"breaks", player)
		else:
			print("%s wins!" %p_name, player, "cuts", comp)

	else:
		print("Check your spelling %s ji" %p_name)

	player=False
	comp=o[randint(0,2)]
