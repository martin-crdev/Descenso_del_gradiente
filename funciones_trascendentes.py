import numpy as np
import matplotlib.pyplot as plt

#Funcion de coseno
def f_coseno(x):
    return np.cos(x) #Numpy ya tiene una funcion para determinar el coseno

#Funcion de seno
def f_seno(x):
    return np.sin(x)

#Funcion exponencial
def f_exponencial(x):
    return 2**x

#Funcion logaritmica
def f_log(x):
    return np.log2(x)

#Funcion seccionada con el ejemplo de la función escalón de Heaviside:
def h(x):
    #Definimos nuestra funcion seccionada
    y = np.zeros(len(x)) # np.zeros llena nuestro arreglo con 0

    #For es porque indicamos en que parte se secciona 
    for idx, x in enumerate(x): #obtenemos un indice idx, y el valor de x con el metodo enumerate 
        if x >= 0: #Indicamos que cuando x sea mayor o igual a 0 Y = 1
            y[idx] = 1.0
    return y #Como la funcion np.zeros llena el arrlego con 0 ya no tenemos que especificar cuando x < 0

def graficar(x, y):
    #Obtenemos la figura y los ejes de la grafica con el metodo
    fig, ax = plt.subplots()

    ax.plot(x, y) #Empezar a graficar colocando nuestros ejes 
    ax.grid()
    ax.axhline(y=0, color="r") #Agregamos una linea horizontal en y=0
    ax.axvline(x=0, color="r") #Agregamos una linea vertical en x=0 

    plt.show()

def run():
    print("""1. Funcion del coseno
    2. Funcion del seno
    3. Funcion exponencial
    4. Funcion logaritmica
    5. Funcion seccionada

    """)
    respuesta = int(input("Seleciona una opcion para ver su grafica: "))

    if respuesta == 1:
        res = 100

        #np.linspace es para llamarlo como un vector en el rango -10 a 10, numero de puntos del vector
        x = np.linspace(-10.0, 10.0, num=res)

        y = f_coseno(x) #Pasar valores a nuestra funcion

        graficar(x, y)

    elif respuesta == 2:
        res = 100

        #np.linspace es para llamarlo como un vector en el rango -10 a 10, numero de puntos del vector
        x = np.linspace(-10.0, 10.0, num=res)

        y = f_seno(x) #Pasar valores a nuestra  funcion

        graficar(x, y)

    elif respuesta == 3:
        res = 100

        #np.linspace es para llamarlo como un vector en el rango -10 a 10, numero de puntos del vector
        x = np.linspace(-10.0, 10.0, num=res)

        y = f_exponencial(x) #Pasar valores a nuestra  funcion

        graficar(x, y)

    elif respuesta == 4:
        res = 100

        #np.linspace es para llamarlo como un vector en el rango -10 a 10, numero de puntos del vector
        x = np.linspace(0.01, 2.0, num=res) #El dominio de logaritmo no puede ser negativo solo acercarse a 0

        y = f_log(x) #Pasar valores a nuestra  funcion

        graficar(x, y)

    elif respuesta == 5:
        res = 100

        #np.linspace es para llamarlo como un vector en el rango -10 a 10, numero de puntos del vector
        x = np.linspace(-10.0, 10.0, num=res)

        y = h(x) #Pasar valores a nuestra  funcion

        graficar(x, y)

if __name__ == "__main__":
    run()