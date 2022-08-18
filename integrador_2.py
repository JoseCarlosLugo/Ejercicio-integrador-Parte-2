#se importa  la libreria  de pandas
import pandas as pd

#Se abre el archivo 'aeropuertos_pasajeros.csv'
df = pd.read_csv('aeropuertos_pasajeros.csv')

def masPasajeros():

    #Se ordena de mayor a menor segun la columna de 'Pasajero'
    print("Los aeropuertos con mas pasajeros\n")
    print(df.sort_values('Pasajeros', ascending=False)[0:5])

    #Se crea una variable para que sea igual a la columna 'pasajeros'
    total_mayor = df.sort_values('Pasajeros', ascending=False)[0:5]
    #Se usa la funcion sum() para sumar toda la columna
    #Se usa la funcion shape[0] para obtener el numero de filas
    #y se dividen
    print("Los aeropuertos con mas pasajeros tienen un promedio de",
        f"{total_mayor['Pasajeros'].sum() / total_mayor.shape[0]} Personas que viajan hacia Sinaloa\n")

def menosPasajeros():
    #Se ordena de menor a mayor segun la columna de 'Pasajero'
    print("Los aeropuertos con menos pasajeros\n")
    print(df.sort_values(['Pasajeros'], ascending=True)[0:5])
    #Se usa la funcion sum() para sumar toda la columna
    #Se usa la funcion shape[0] para obtener el numero de filas
    #y se dividen
    total_menor = df.sort_values(['Pasajeros'], ascending=True)[0:5]
    print("Los aeropuertos con menos pasajeros tienen un promedio de",
        f"{total_menor['Pasajeros'].sum() / total_menor.shape[0]} Personas que viajan hacia Sinaloa \n")

def aeroPromedio():
    print(f"El total de aeropuertos tienen un promedio de",
        #se usa la funcion round() para redondear a dos decimales
        #Se usa la funcion sum() para sumar toda la columna
        #Se usa la funcion shape[0] para obtener el numero de filas
        f"{round(df['Pasajeros'].sum() / df.shape[0],2)} Personas que viajan hacia Sinaloa")


def crearArchivo():
    #Se crea un dataframe para que sea igual a los 5 mejores aeropuertos
    Datos_VuelosMayor = df.sort_values('Pasajeros', ascending=False)[0:5]
    #Se crea un dataframe para que sea igual a los 5 peores aeropuertos
    Datos_VuelosMenor = df.sort_values(['Pasajeros'], ascending=True)[0:5]
    #Se crea dataframe para juntar los dos anteriores
    #Se usa la funcion contat() para concatenar los dos dataframe por columnas
    Datos_Vuelos = pd.concat([Datos_VuelosMayor, Datos_VuelosMenor], axis=0)

    #Se crea un archivo.CSV
    Datos_Vuelos.to_csv('Datos_Vuelos.csv')




