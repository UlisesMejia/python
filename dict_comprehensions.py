from ast import Import
import math


def run():
    # my_dict = {}

    # for i in range (1, 101):
    #     if i % 3 != 0: 
    #         my_dict[i] = i**3
    my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}


    print(my_dict)    

    # Crear un diccionario con los primeros 1000 numerois naturales cuya llave sea el numero natural y el valor sea su raiz cuadrada 

    natural_num = {i: math.sqrt(i) for i in range(1, 1001) }

    print(natural_num)

if __name__ == "__main__":
    run()    