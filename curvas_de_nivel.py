from matplotlib import cm #Libreria para manejar colores
import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return np.sin(x) + 2*np.cos(y)

def run():
    res = 100
    x = np.linspace(-4, 4, num=res)
    y = np.linspace(-4, 4, num=res)

    x, y = np.meshgrid(x, y) #Marcamos los pares coordenados 

    z = f(x, y)

    #Indiquicamos el tipo de subplots por defecto es 2d
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    #Superficie
    surf = ax.plot_surface(x, y, z, cmap= cm.cool)
    fig.colorbar(surf) #Muestra la barra 

    plt.show()

    #Plano que representa la superficie 
    fig2, ax2 = plt.subplots()

    #Se crean niveles, planos que cortan a la superficie de manera horizontal
    level_map = np.linspace(np.min(z), np.max(z), num=res) 

    cp= ax2.contour(x, y, z, levels=level_map, cmap=cm.cool)
    fig2.colorbar(cp)

    plt.show()

if __name__ == "__main__":
    run()