import matplotlib.pyplot as plt
import random

def collatz_conjecture():
    number = random.randint(0,123456789)
    iterations = 0
    y_list = []
    x_list=[]
    while number !=1:
        iterations += 1
        x_list.append(iterations)
        y_list.append(int(number))   
        if number % 2 == 0:
           number = number/2
        else:
            number = number*3+1
    dispersion_diagram(x_list,y_list)
    line_diagram(x_list,y_list)
    area_diagrams(x_list,y_list)
    bar_vertical_diagram(x_list,y_list)
    bar_horizontal_diagram(x_list,y_list)


def dispersion_diagram(x,y):
    fig, ax = plt.subplots()
    ax.scatter( x,y)
    plt.savefig('diagrama-dispersion.png')
    plt.show()


def line_diagram(x,y):
    fig, ax = plt.subplots()
    ax.plot( x,y)
    plt.savefig('diagrama-linea.png')
    plt.show()


def area_diagrams(x,y):
    fig, ax = plt.subplots()
    ax.fill_between( x,y)
    plt.savefig('diagrama-area.png')
    plt.show()


def bar_vertical_diagram(x,y):
    fig, ax = plt.subplots()
    ax.bar( x,y)
    plt.savefig('diagrama-barra-vertical.png')
    plt.show()


def bar_horizontal_diagram(x,y):
    fig, ax = plt.subplots()
    ax.barh( x,y)
    plt.savefig('diagrama-barra-horizontal.png')
    plt.show()



collatz_conjecture()