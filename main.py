from funciones import *
from variables import *

tablero_jugador = TABLERO_JUGADOR
tablero_maquina = TABLERO_MAQUINA

jugador = Colocar_barco(Inicializar_tablero())
maquina = Colocar_barco(Inicializar_tablero())

counter = 0
turno = True

while "⛵" in jugador and counter < 28:

    while turno == True:
        print("TABLERO DE LA MAQUINA")
        print(tablero_maquina)
        print("-"*50)
        print ("TU TABLERO")
        print(tablero_jugador)

        turno = disparar(tablero=maquina, tablero_imagen= tablero_maquina, turno=turno)
        
        counter += 1

    while turno == False:
        print("TABLERO DE LA MAQUINA")
        print(tablero_maquina)
        print("-"*50)
        print ("TU TABLERO")
        print(tablero_jugador)
        
        turno = disparar(tablero=jugador, tablero_imagen= tablero_jugador, turno= turno)
        

    

