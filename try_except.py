# TRY/EXCEPT
# = TRY (EXECUTE) tento program, sript, kód a POKUD je něco špatně, přejdi na EXCEPT
# The try block: lets me "test" a block of code for errors
# The except block: catches the errors and lets me handle it

# Stejný příklad jako ve skriptu 03_Conditionals
# PRINCIP:
	# Pokud user_input_2.isdigit(): je TRUE, tak hledám další podmínky.
	# Pokud se něco stane, co nedokážu ani popsat podmínkama, nebo třeba
	# na některou zapomenu, hodí to chybu a program se ukončí.
	# Namísto podmínky If user_input_2.isdigit(): dám Try a pak Except

calculation_to_units = 24
name_of_units = "hours"

def days_to_units_2(num_of_days):
	return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}"


def validate_and_execute_2():
	try:
		user_input_number = int(user_input_2)
		if user_input_number > 0:
			calculated_value = days_to_units_2(user_input_number)
			print(calculated_value)
		elif user_input_number == 0:
			print("You entered a 0, please enter a valid positive number")
		else:
			print("You entered a negative value, so no conversion for you!")

	except ValueError:	# ValueError můžu smazat. Dostanu sice Warning, ale taky to jde
		print("Your input is not a valid number. Don´t ruin my program!")


user_input_2 = input("Hey user, enter a number of days and I will convert it to hours!\n")
validate_and_execute_2()
