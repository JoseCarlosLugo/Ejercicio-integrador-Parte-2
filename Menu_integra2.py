
from integrador_2 import masPasajeros
from integrador_2 import menosPasajeros
from integrador_2 import aeroPromedio
from integrador_2 import crearArchivo




#Se crea un while para el menu
while True:

    #Se imprimen las opciones del menu
    print(" Que quieres hacer? \n",
          "ver los aeropuertos con mas pasajeros                (1) \n",
          "ver los aeropuertos con menos pasajeros              (2) \n",
          "ver el promedio de personas que viajan hacia Sinaloa (3) \n",
          "crear un archivos 'CSV' con los datos                (4) \n",
          "Salir                                                (5)")
          
    #Input para la eleccion
    #       
    do = input(": ")
    print("\n")
    
    #Se usa la funccion segun la eleccion
    if do == "1":
        masPasajeros()
    elif do == "2":
        menosPasajeros()
    elif do == "3":
        aeroPromedio()
    elif do == "4":
        crearArchivo()
    elif do == "5":
        print("Cerrando programa.")
        break                     
    else:
        print("Error con la eleccion \n") 