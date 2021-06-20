from matplotlib import cm #Para manejar colores
import numpy as np
import matplotlib.pyplot as plt

h = 0.01 #Incremento muy pequeño
lr = 0.01 #Learning rate nos indica la proporcion de los pasos a seguir

#Definimos nuestra funcion derivate que utiliza como parametros a la copia de nuestro punto con el punto
def derivate(cp, p):
    return (f(cp[0], cp[1]) - f(p[0], p[1])) / h #Aplicamos la definicion de la derivada

#Definimos nuestro gradiente que toma como parametro nuestro punto aleatorio 
def gradient(p):
    
    grad = np.zeros(2) #definimos un vector con 2 dimensiones y las llenamos con 0 
    for idx, val in enumerate(p): #iteramos nuestro gradiente con la funcion enumerate que nos regresa el indice y su valor
        cp = np.copy(p) #hacemos una copia de nuestro punto 
        cp[idx] = cp[idx] + h #Ir agregando un pequeño incremento (h) a la copia

        dp = derivate(cp, p) #dp = derivada parcial de nuestro punto utilizando la copia con el incremento y nuestro punto original
        grad[idx] = dp #Guardamos los componentes de nuestra derivada parcial 
    return grad

        
def f(x,y):
    return x**2 + y**2

def run():
    #Graficar nuestra funcion 
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    res = 100

    x = np.linspace(-4, 4, num=res)
    y = np.linspace(-4, 4, num=res)
    X, Y = np.meshgrid(x, y)

    Z = f(X, Y)

    surf = ax.plot_surface(X, Y, Z, cmap=cm.cool)

    plt.show()

    #Curvas de nivel
    level_map = np.linspace(np.min(Z), np.max(Z), res)
    plt.contourf(X, Y, Z, levels=level_map, cmap=cm.cool)
    plt.colorbar()
    plt.title("Descenso del gradiente")

    #Nos da dos elementos aleatorios entre 0 y 1, se multiplica por 8 y se resta 4 para que este en el rango de -4 a 4
    p = np.random.rand(2) *8 - 4 
    plt.plot(p[0], p[1], "o", c="k")

    for i in range(100):
        p = p - lr*gradient(p)
        if (i % 10 == 0):
            plt.plot(p[0], p[1], "o", c="r") #Graficamos el camino en color rojo cada 10 iteraciones
    plt.plot(p[0], p[1], "o", c="w") #Graficamos el final de nuestro algoritmo

    plt.show()


if __name__ == "__main__":
    run()