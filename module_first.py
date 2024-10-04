# Modules
	# is just a .py file, that containts functions and variables that I can use i another python file
	# I can reference one module to another
	# I can structure my application using modules
	# Logically organize your Python code
	# Module should contain related code
	# Když mám velký projekt a nechci mít jenom tisíce řádků, ale trochu si zorganizovat Project file
	# Můžu používat řadu skriptů a podsložek s dalšími skripty - Moduly


# import název_modulu(.py souboru)
	# importuje vše
	# Syntax pro použití
		# název_modulu(.py souboru).název_funkce()
# import název_modulu(.py souboru) as ___
	# Syntax pro použití
		# ___.název_funkce()
# from název_modulu(.py souboru) import název_funkce, název_variable
	# název_funkce, název_variable = Definitions of a module
	# Syntax pro použití
		# název_funkce()
# from název_modulu(.py souboru) import *
	# Syntax pro použití
		# název_funkce()


# IF __NAME__
	# Znamená to toto:
		# Když spustím skript, jméno toho skriptu (__name__) je brané jako "__main__"
		# Takže cokoliv píšu do IMPORTOVANÉHO skriptu a NECHCI, aby se to při spuštění hlavního skriptu zobrazilo,
		# dám to do podmínky if __name__ == "__main__":

# Built-in modules
	# když zmáčknu CTRL a pak kliknu na modul (import module_name), otevře se mi skript
# Third-Party modules
""" Python comes only with a set of built-in modules
	Many more modules out there, which are NOT part of the Python Installation
	I need to install these third-party packages
	Built-In Modules and Packages are most common ones
	Depending on what application I write, add specific ones"""
	# PyPI
		# is a repository (storage) for third-party Python packages
		# Python Package Index
		# People can publish their packages to this repository
		# Si it becoms available for everyone to us
		# A large community means, many people are creating useful modules and make them available for others
	# Pip
		# package manager tool for Python
		# every programming language has its own package manager tool
		# used to install packages from the Python Package Index, but also other indexes
		# Instalace
			# v Terminálu (nejlepší v Pycharm) pip (un)install _____


# Package vs Module
	# Package is a collection of Python Modules

print(__name__) # Když spustím tento skript, toto vypíše __main__

def greet():
	print("Hello world")

if __name__ == "__main__":
	greet()
