from matplotlib import cm #Para manejar colores
import numpy as np
import matplotlib.pyplot as plt

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

    plt.show()


if __name__ == "__main__":
    run()