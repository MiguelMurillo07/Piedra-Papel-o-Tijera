# Juego Piedra, Papel o Tijera con opción aleatoria

import random

print("-------------------------------")
print("-----Piedra, Papel o Tijera----")
print("-------------------------------")

# input
print(" \nDime el valor que quieres tener en el juego: \n")
# Se despliega el menú de opciones para empezar a jugar:
print("1. Sacar Piedra.")
print("2. Sacar Papel.")
print("3. Sacar Tijera.")
num_maq = random.randint(1, 3)

opcion = int(input("Dame el lugar que quieres tener para jugar: "))

# Processing and output

if(opcion) ==1:
    if num_maq==1:
        print("La máquina sacó Piedra, lo que quiere decir que hubo empate!.")
    elif num_maq==2:
        print("La máquina sacó Papel, lo que quiere decir que perdiste!.")
    elif num_maq==3:
        print("La máquina sacó Tijera, lo que quiere decir que ganaste!.")

if(opcion) ==2:
    if num_maq==1:
        print("La máquina sacó Piedra, lo que quiere decir que ganaste!. ")
    elif num_maq==2:
        print("La máquina sacó Papel, lo que quiere decir que hubo empate!.")
    elif num_maq==3:
        print("La máquina sacó Tijera, lo que quiere decir perdiste!.")

if(opcion) ==3:
    if num_maq==1:
        print("La máquina sacó Piedra, lo que quiere decir que perdiste!.")
    elif num_maq==2:
        print("La máquina sacó Papel, lo que quiere decir que ganaste!.")
    elif num_maq==3:
        print("La máquina sacó Tijera, lo que quiere decir que hubo empate!.")
