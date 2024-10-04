# TVORBA UKLÁDÁNÍ SOUBORŮ
import os

""" 
Textové soubory
    # w = write
    # r = read
    # a = append - připojit
    # + vytvoř, pokud není
"""

# Jméno souboru
filename = "Textovy_soubor_zk.txt"

file = open(filename,"w+")

text = ("This is line new\n"
        "This is also line \n"
        "Ahoj \n"
        "Haha \n")

zk_input = input("Zadej číslo:")

file.write(text + str(zk_input))
file.close

