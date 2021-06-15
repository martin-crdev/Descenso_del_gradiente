import numpy as np
import matplotlib.pyplot as plt

#Funcion lineal
def f(m, x, b):
    return m*x+b

#Funcion potencia que es un caso particular de las funciones polinomicas 
def f_b(x):
    return x**2

#Funcion polinomico
def f_p(x):
    return 2*x**7 - x**4 + 3*x**2 + 4

def graficar(x, y):
    #Obtenemos la figura y los ejes de la grafica con el metodo
    fig, ax = plt.subplots()

    ax.plot(x, y) #Empezar a graficar colocando nuestros ejes 
    ax.grid()
    ax.axhline(y=0, color="r") #Agregamos una linea horizontal en y=0
    ax.axvline(x=0, color="r") #Agregamos una linea vertical en x=0 

    plt.show()




def run():
    print("""1. Y= mx + b
    2. Y= x**2
    3. Y= 2x**7 - x**4 + 3x**2 + 4 
    
    """)
    respuesta = int(input("Elije una funcion a graficar: "))

    if respuesta == 1:
        res = 100
        m = 10
        b = 5

        #np.linspace es para llamarlo como un vector en el rango -10 a 10, numero de puntos del vector
        x = np.linspace(-10.0, 10.0, num=res) 

        y = f(m, x, b) #Pasar valores a nuestra funcion

        graficar(x, y)

    elif respuesta == 2:
        res = 100
   

        #np.linspace es para llamarlo como un vector en el rango -10 a 10, numero de puntos del vector
        x = np.linspace(-10.0, 10.0, num=res) 

        y = f_b(x) #Pasar valores a nuestra funcion

        graficar(x, y)

    else:
        res = 100
   

        #np.linspace es para llamarlo como un vector en el rango -10 a 10, numero de puntos del vector
        x = np.linspace(-10.0, 10.0, num=res) 

        y = f_p(x) #Pasar valores a nuestra funcion

        graficar(x, y)

    


if __name__ == "__main__":
    run()