# WHILE = DOKUD
# To execute logic multiple times
	# x-times or until somethings happend
# Python has two Loop commands

# Stejný příklad jako 03_Conditionals
	# Dokud nezadám správný input, zadávám dál

# while ..... != ..... - např.: user_input != "exit"
user_input = ""					# musíme nejdříve seznámit while loop s variable user_input
while user_input != "exit":
	user_input = input("Hey user, enter something:\n")
	print(user_input)

# while Trube - executing indefinitelly

# For Loop
# Is used for iterating over a sequence (like a list)
# So we can execute smth for each item in a list
