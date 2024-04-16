import numpy as np


#Creamos la funcion que nos crea el tablero
def Inicializar_tablero():
    tablero = np.full((10,10), "🌊")
    return tablero


#Colocar barcos de manera aleatoria.
def Colocar_barco(matrix):
    #Colocamos un barco de 4 posiciones
    tamaño_barco =[4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    for i in tamaño_barco:
        validacion = False
       
        while validacion == False:
            direc = np.random.choice(["N", "S", "E", "W"])
            if direc =="N":
                coor_x =np.random.randint(i,10)
                coor_y = np.random.randint(0,10)
                
                
                if coor_x == i:
                                        
                    if coor_y == 0 and np.all(matrix[coor_x::-1,coor_y:coor_y+1] == "🌊") == True:
                        matrix[coor_x:coor_x-i:-1,coor_y] = "⛵"
                        validacion = True

                    if (coor_y == 9 or coor_y == 8) and np.all(matrix[coor_x::-1,coor_y-1::] == "🌊") == True:
                        matrix[coor_x:coor_x-i:-1,coor_y] = "⛵"
                        validacion = True

                    if np.all(matrix[coor_x::-1,coor_y-1:coor_y+1] == "🌊") == True:
                        matrix[coor_x:coor_x-i:-1,coor_y] = "⛵"
                        validacion = True
                    
                elif coor_x ==9:

                    if coor_y == 0 and np.all(matrix[coor_x-i::,coor_y:coor_y+1] == "🌊") == True:
                        matrix[coor_x-i::,coor_y] = "⛵"
                        validacion = True

                    if (coor_y == 9 or coor_y == 8) and np.all(matrix[coor_x-i::,coor_y-1::] == "🌊") == True:
                        matrix[coor_x-i::,coor_y] = "⛵"
                        validacion = True

                    if np.all(matrix[coor_x-i::,coor_y-1:coor_y+1] == "🌊") == True:
                        matrix[coor_x-i::,coor_y] = "⛵"
                        validacion = True

                else:

                    if coor_y == 0 and np.all(matrix[coor_x+1:coor_x-i-1:-1,coor_y:coor_y+1] == "🌊") == True:
                        matrix[coor_x:coor_x-i:-1,coor_y] = "⛵"
                        validacion = True
                    
                    if (coor_y == 9 or coor_y == 8) and np.all(matrix[coor_x-i-1:coor_x+1,coor_y-1::] == "🌊") == True:
                        matrix[coor_x:coor_x-i:-1,coor_y] = "⛵"
                        validacion = True

                    if np.all(matrix[coor_x-i-1:coor_x+1,coor_y-1:coor_y+1] == "🌊") == True:
                        matrix[coor_x:coor_x-i:-1,coor_y] = "⛵"
                        validacion = True 

            if direc == "S":
                coor_x =np.random.randint(0,10-i)
                coor_y = np.random.randint(0,10)
                
                if coor_x == 10-i:
                                        
                    if coor_y == 0 and np.all(matrix[coor_x::,coor_y:coor_y+1] == "🌊") == True:
                        matrix[coor_x::,coor_y] = "⛵"
                        validacion = True

                    if (coor_y == 9 or coor_y == 8) and np.all(matrix[coor_x::,coor_y-1::] == "🌊") == True:
                        matrix[coor_x::,coor_y] = "⛵"
                        validacion = True

                    if np.all(matrix[coor_x::,coor_y-1:coor_y+1] == "🌊") == True:
                        matrix[coor_x::,coor_y] = "⛵"
                        validacion = True

                elif coor_x ==0:

                    if coor_y == 0 and np.all(matrix[coor_x:coor_x+i+1,coor_y:coor_y+1] == "🌊") == True:
                        matrix[coor_x:coor_x+i,coor_y] = "⛵"
                        validacion = True

                    if (coor_y == 9 or coor_y == 8) and np.all(matrix[coor_x:coor_x+i+1,coor_y-1::] == "🌊") == True:
                        matrix[coor_x:coor_x+i,coor_y] = "⛵"
                        validacion = True

                    if np.all(matrix[coor_x:coor_x+i+1,coor_y-1:coor_y+1] == "🌊") == True:
                        matrix[coor_x:coor_x+i,coor_y] = "⛵"
                        validacion = True
                else:

                    if coor_y == 0 and np.all(matrix[coor_x-1:coor_x+i+1,coor_y:coor_y+1] == "🌊") == True:
                        matrix[coor_x:coor_x+i,coor_y] = "⛵"
                        validacion = True
                    
                    if (coor_y == 9 or coor_y == 8) and np.all(matrix[coor_x-1:coor_x+i+1,coor_y-1::] == "🌊") == True:
                        matrix[coor_x:coor_x+i,coor_y] = "⛵"
                        validacion = True

                    if np.all(matrix[coor_x-1:coor_x+i+1,coor_y-1:coor_y+1] == "🌊") == True:
                        matrix[coor_x:coor_x+i,coor_y] = "⛵"
                        validacion = True
            if direc =="O":
                coor_x =np.random.randint(0,10)
                coor_y = np.random.randint(i,10)
                
                
                if coor_y == i:
                                        
                    if coor_x == 0 and np.all(matrix[coor_x:coor_x+1,coor_y::-1] == "🌊") == True:
                        matrix[coor_x,coor_y:coor_y-i:-1] = "⛵"
                        validacion = True

                    if (coor_x == 9 or coor_x == 8) and np.all(matrix[coor_x::-1,coor_y::-1] == "🌊") == True:
                        matrix[coor_x,coor_y:coor_y-i:-1] = "⛵"
                        validacion = True

                    if np.all(matrix[coor_x-1:coor_x+2,coor_y::-1] == "🌊") == True:
                        matrix[coor_x,coor_y:coor_y-i:-1] = "⛵"
                        validacion = True
                    
                elif coor_y ==9:

                    if coor_x == 0 and np.all(matrix[coor_x:coor_x+2,coor_y-i::] == "🌊") == True:
                        matrix[coor_x,coor_y:coor_y-i:-1] = "⛵"
                        validacion = True

                    if (coor_x == 9 or coor_x == 8) and np.all(matrix[coor_x::,coor_y-i::] == "🌊") == True:
                        matrix[coor_x,coor_y:coor_y-i:-1] = "⛵"
                        validacion = True

                    if np.all(matrix[coor_x-1:coor_x+1:-1,coor_y-i::] == "🌊") == True:
                        matrix[coor_x,coor_y:coor_y-i:-1] = "⛵"
                        validacion = True

                else:

                    if coor_x == 0 and np.all(matrix[coor_x:coor_x+1,coor_y+1:coor_y-i-1:-1] == "🌊") == True:
                        matrix[coor_x,coor_y:coor_y-i:-1] = "⛵"
                        validacion = True
                    
                    if (coor_x == 9 or coor_x == 8) and np.all(matrix[coor_x::,coor_y+1:coor_y-i-1:-1] == "🌊") == True:
                        matrix[coor_x,coor_y:coor_y-i:-1] = "⛵"
                        validacion = True

                    if np.all(matrix[coor_x-1:coor_x+1:-1,coor_y+1:coor_y-i-1:-1] == "🌊") == True:
                        matrix[coor_x,coor_y:coor_y-i:-1] = "⛵"
                        validacion = True
            if direc == "E":
                coor_x =np.random.randint(0,10-i)
                coor_y = np.random.randint(0,10)
                
                if coor_y == 10-i:
                                        
                    if coor_x == 0 and np.all(matrix[coor_x:coor_x+1,coor_y::] == "🌊") == True:
                        matrix[coor_x,coor_y::] = "⛵"
                        validacion = True

                    if (coor_x == 9 or coor_x == 8) and np.all(matrix[coor_x-1::, coor_y::] == "🌊") == True:
                        matrix[coor_x,coor_y::] = "⛵"
                        validacion = True

                    if np.all(matrix[coor_y-1:coor_y+1, coor_y::] == "🌊") == True:
                        matrix[coor_y, coor_y::] = "⛵"
                        validacion = True

                elif coor_y ==0:

                    if coor_x == 0 and np.all(matrix[coor_x:coor_x+1, coor_y:coor_y+i+1] == "🌊") == True:
                        matrix[coor_x, coor_y:coor_y+i] = "⛵"
                        validacion = True

                    if (coor_x == 9 or coor_x == 8) and np.all(matrix[coor_x-1::, coor_y:coor_y+i+1] == "🌊") == True:
                        matrix[coor_x,coor_y:coor_y+i] = "⛵"
                        validacion = True

                    if np.all(matrix[coor_x:coor_x+i+1,coor_y-1:coor_y+1] == "🌊") == True:
                        matrix[coor_x, coor_y:coor_y+i] = "⛵"
                        validacion = True
                else:

                    if coor_x == 0 and np.all(matrix[coor_x:coor_x+1, coor_y-1:coor_y+i+1] == "🌊") == True:
                        matrix[coor_x, coor_y:coor_y+i] = "⛵"
                        validacion = True
                    
                    if (coor_x == 9 or coor_y == 8) and np.all(matrix[coor_x-1::, coor_y-1:coor_y+i+1] == "🌊") == True:
                        matrix[coor_x, coor_y:coor_y+i] = "⛵"
                        validacion = True

                    if np.all(matrix[coor_x-1:coor_x+1, coor_y-1:coor_y+i+1] == "🌊") == True:
                        matrix[coor_x, coor_y:coor_y+i] = "⛵"
                        validacion = True
                        
    
    return matrix 

def disparar(tablero, tablero_imagen,turno):
    try:
        if turno == True:
            coor_x = int(input("Coord X:"))
            coor_y = int(input("Coord Y:"))

            if tablero[coor_x, coor_y] == "⛵":
                tablero_imagen[coor_x, coor_y] = "💥"
                print("Has acertado!")
            elif tablero[coor_x, coor_y] == "🌊":
                tablero_imagen[coor_x, coor_y] = "⬛"
                print("Has fallado!")
                turno = False

            else:
                print("Has repetido el disparo.")
        else:
            coor_x = np.random.randint(0,10)
            coor_y = np.random.randint(0,10)  


            if tablero[coor_x, coor_y] == "⛵":
                tablero_imagen[coor_x, coor_y] = "💥"
                print("La Maquina ha acertado!")        

            elif tablero[coor_x, coor_y] == "🌊":
                tablero_imagen[coor_x, coor_y] = "⬛"
                print("La maquina ha fallado!")
                turno = True
                
            else:
                print("Has repetido el disparo.")
    except:
        print("Las coordenadas seleccionadas son erroneas")
    return turno
