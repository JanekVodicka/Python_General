# DATATYPES
# Změna dadatype = Casting
	# Když použiju fci input(), vždy získám string → zadám číslo → potřebuji číslo →
		# my_var_str = input()
		# my_var_num = int(my_var)
		# my_var_str = str(my_var_num)
# Built-In Functions
	# Funkce, které můžu použít na dytetypes a jsou součástí interpreteru
	# each data type has its own built-in function
	# which are useful/make sense only for this specific data type
# Variables are containers for storing values

from math import *  # math = tzv. MODULE

""" DATA TYPES """
# Proměnná typu STRING
# str()
name = "Janek"
age = "27"

print("Ahoj, moje jméno je " + name + " a")		# Vypíše: Ahoj, moje jméno je Janek a
print(f"je mi {age} let")						# Vypíše: je mi 27 let

# Proměnná typu NUMBER
# int()
	# - whole number
	# - positive or negative
	# - without decimals
x = 50
# float()
	# - positive or negative
	# - number
	# - containing one ore more decimals
y = 20.638
my_num = -5

# Proměnná typu BOOLEN
is_Male = True
is_Female = False

# Když chceme zjistit datatype
print()
print("Zjisti typy proměnných: ")
print(type(name))
print(type(x))
print(type(y))
print(type(is_Male))

# ----- LISTS -----
""" Lists
	- []
	- To store multiple items in a single variable
	- A List can contain different data types """

friends = ["Ondra", "Lucka", "Niki", "Ondra"]
numbers = [2, 5, 8, 3]
print()
print("LISTS: ")
print(friends)

# ----- SETS -----
""" Sets
	- {}
	- Another built-in data type of Python
	- as with Lists, used to store multiple items of data
	- does NOT allow duplicate values
	- Unordered and unchangeable
		- Items in a set do not have a defined order
		- Items cannot be referred to by index
		- Items cannot be changed, only added/removed """

print()
print("SETS: ")
print(set(friends))
my_set = {"January", "February", "March"}
for element in my_set:
	print(my_set)

my_set.add("April")
print(my_set)
my_set.remove("January")
print(my_set)

# ----- DICTIONARY -----
""" Dictionary
	- Are used to store values in key: value pairs
	- Is a collection, which does not allow duplicate values
	- Syntax
		- Dictionary_name = {"key name 1": data_type_1, "key name 2": data_type_2, ...}
	- Accesing Items in a Dictionary
		- Items can be accessed by its key name
		- I can use square brackets or get() method """

my_list_for_dictionary = [30, "hours"]
my_dictionary =  {"days": my_list_for_dictionary[0], "units": my_list_for_dictionary[1]}
print()
print("DICTIONARY: ")
print(my_dictionary)
print(my_dictionary["days"])
print(my_dictionary.get("units"))

# ----------------------------------------------------------------------------------------------------------------------
# WORKING WITH STRINGS
	# \n ... novy radek
	# \ ... vypise ten znak, co je za \ ... napr. \# \"
my_phrase = "Ahoj Janku"
print()
print("WORKING WITH STRINGS:")
print(my_phrase.upper()) 						# Všechna písmena velká
print(my_phrase.lower()) 						# Všechna písmena malá
print(my_phrase.isupper()) 						# Pokud je pravda, že jsou všechna písmena (isupper()) velká, vypíše se True, jinak False
print(my_phrase.upper().isupper())
print(len(my_phrase)) 							# Počet písmen
print(my_phrase[0]) 							# Jaké je první písmeno? 0 je pro první prvek
print(my_phrase.index("a")) 					# Najde místo, kde je "a" --- bacha! začíná od 0
print(my_phrase.replace("Ahoj", "Čau")) 		# Vymění Ahoj za Čau
# String.split()
# "10 22 50 100" → [10, 22, 50, 100]
# String.split(",")
# "10, 22, 50, 100" → [10, 22, 50, 100]

# WORKING WITH NUMBERS
	# int ... integer ... CELE CISLO
	# float ... CISLO S DESETINNYMA MISTAMA
print()
print("WORKING WITH NUMBERS:")
print(10 % 3) 									# Vypíše zbytek: 9/3=3 --- tedy 1
print(str(my_num)) 								# Předělá číslo na string
print(abs(my_num)) 								# Absolutní hodnota
print(pow(3,2))    						# 3^2
print(sqrt(36))    								# Odmocnina z 36
print(min(3,6))									# Minimum z 3 a 6
print(round(3.4))  								# Zaokrouhlení
print(floor(3.7))  								# Vypíše nejnižší celé číslo --- 3

# WORKING WITH LISTS - NUMBERS
print()
print("WORKING WITH LISTS - NUMBERS:")
print(friends[0])								# Vypíše první prvek: Ondra
print(friends[-1])								# Vypíše poslední prvek: Niki
print(friends[1:2]) 							# Do konce můžu psát jen 1

# WORKING WITH LISTS - GENERALLY
	#Basic list operations
		# Create a list
		# Add an item to the list
		# Remove an item from the list
		# Change items in the list
		# Access items of the list
print()
print("WORKING WITH LISTS - GENERALLY:")
print(friends[1])
friends.extend(numbers)							# Za friends připojí množinu numbers
print(friends)
friends.append(11)								# Za friends připojí číslo 11
print(friends)
friends.insert(2,"Tom")			# Na třetí místo dá další prvek - Tom
print(friends)
friends.remove("Tom")							# Odstraní prvek Tom
print(friends)
friends.clear()									# Vytvoří prízdnou množinu
print(friends)
friends = ["Ondra", "Lucka", "Niki"]
friends.pop()									# Vyřadí poslední prvek
print(friends)

# ALL TYPES OF DATA TYPES
message = "enter some value"
days = 20
price = 9.99
valid_number = True
exit_imput = False
list_of_days = [20, 30, 40, 25]
list_of_months = ["January", "February", "June"]
set_of_days = {20, 40, 100}
days_and_units = {"days": 10, "units": "hours"}
