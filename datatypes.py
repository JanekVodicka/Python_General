# DATATYPES
	# Text type: 		str
	# Numeric Types: 	int, float, complex
	# Sequence Types: 	list, tuple, range
	# Mapping Type:		dict
	# Set Types: 		set, frozenset
	# Boolean Type:		bool
	# Binary Types:		bytes, bytearray, memoryview
	# None Type:		NoneType

# Změna dadatype = Casting
	# Když použiju fci input(), vždy získám string → zadám číslo → potřebuji číslo →
		# my_var_str = input()
		# my_var_num = int(my_var_str)
		# my_var_str = str(my_var_num)

# Built-In Functions
	# Funkce, které můžu použít na dytetypes a jsou součástí interpreteru
	# each data type has its own built-in function
	# which are useful/make sense only for this specific data type

# Variables are containers for storing values

from math import *  # math = tzv. MODULE


""" DATA TYPES """
# ---- Proměnná typu STRING ----
# str()
name = "Janek"
age = "27"

print("Ahoj, moje jméno je " + name + " a")		# Vypíše: Ahoj, moje jméno je Janek a
print(f"je mi {age} let")						# Vypíše: je mi 27 let
print()

# ---- Proměnná typu NUMBER ----
# int()
	# - whole number
	# - positive or negative
	# - without decimals
x = 50
y = -50

# float()
	# - positive or negative
	# - number
	# - containing one ore more decimals
z = 20.638
my_num = -5

# Proměnná typu BOOLEN
is_Male = True
is_Female = False

# ---- LISTS ----
""" Lists
	- []
	- To store multiple items in a single variable
	- A List can contain different data types """

my_list_1 = ["Ondra", "Lucka", "Niki", "Ondra"]
my_list_2 = [2, 5, 8, 3]

print("LISTS: ")
print(my_list_1)
print()

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

print("SETS: ")
print(set(my_list_1))

my_set = {"January", "February", "March"}
for element in my_set:
	print(my_set)

my_set.add("April")
print(my_set)
my_set.remove("January")
print(my_set)
print()

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

print("DICTIONARY: ")
print(my_dictionary)
print(my_dictionary["days"])
print(my_dictionary.get("units"))
print()

# ----------------------------------------------------------------------------------------------------------------------
# WORKING WITH STRINGS
	# \n ... novy radek
	# \ ... vypise ten znak, co je za \ ... napr. \# \"
my_phrase = "Ahoj Janku"

print("WORKING WITH STRINGS:")
print(my_phrase.upper()) 						# Všechna písmena velká
print(my_phrase.lower()) 						# Všechna písmena malá
print(my_phrase.isupper()) 						# Pokud je pravda, že jsou všechna písmena (isupper()) velká, vypíše se True, jinak False
print(my_phrase.upper().isupper())
print(len(my_phrase)) 							# Počet písmen
print(my_phrase[0]) 							# Jaké je první písmeno? 0 je pro první prvek
print(my_phrase.index("a")) 					# Najde místo, kde je "a" --- bacha! začíná od 0
print(my_phrase.replace("Ahoj", "Čau")) 		# Vymění Ahoj za Čau
print()
# String.split()
# "10 22 50 100" → [10, 22, 50, 100]
# String.split(",")
# "10, 22, 50, 100" → [10, 22, 50, 100]

# WORKING WITH NUMBERS
	# int ... integer ... CELE CISLO
	# float ... CISLO S DESETINNYMA MISTAMA
print("WORKING WITH NUMBERS:")
print(10 % 3) 									# Vypíše zbytek: 9/3=3 --- tedy 1
print(str(my_num)) 								# Předělá číslo na string
print(abs(my_num)) 								# Absolutní hodnota
print(pow(3,2))    						# 3^2
print(sqrt(36))    								# Odmocnina z 36
print(min(3,6))									# Minimum z 3 a 6
print(round(3.4))  								# Zaokrouhlení
print(floor(3.7))  								# Vypíše nejnižší celé číslo --- 3
print()

# WORKING WITH LISTS - NUMBERS
print("WORKING WITH LISTS - NUMBERS:")
print(my_list_1[0])								# Vypíše první prvek: Ondra
print(my_list_1[-1])							# Vypíše poslední prvek: Niki
print(my_list_1[1:2]) 							# Do konce můžu psát jen 1
print()

# WORKING WITH LISTS - GENERALLY
	#Basic list operations
		# Create a list
		# Add an item to the list
		# Remove an item from the list
		# Change items in the list
		# Access items of the list
print("WORKING WITH LISTS - GENERALLY:")
print(my_list_1[1])
my_list_1.extend(my_list_2)						# Za friends připojí množinu numbers
print(my_list_1)
my_list_1.append(11)							# Za friends připojí číslo 11
print(my_list_1)
my_list_1.insert(2, "Tom")		# Na třetí místo dá další prvek - Tom
print(my_list_1)
my_list_1.remove("Tom")							# Odstraní prvek Tom
print(my_list_1)
my_list_1.clear()								# Vytvoří prízdnou množinu
print(my_list_1)
my_list_1 = ["Ondra", "Lucka", "Niki"]
my_list_1.pop()									# Vyřadí poslední prvek
print(my_list_1)
print()

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

# Když chceme zjistit datatype
print("ZJISTI TYPY PROMĚNNÝCH: ")
print(type(name))
print(type(x))
print(type(z))
print(type(is_Male))
print(type(my_list_1))
print(type(my_set))
print(type(my_dictionary))
