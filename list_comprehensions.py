def run():
    # squares = []
    # for i in range (1, 101):
    #     if i % 3 != 0:
    #         squares.append(i**2)

    # squares = [i**2 for i in range (1, 101) if i % 3 != 3]
    
    # print(squares)

    # En la lista se va a guardar....para cada elemento en el iterable ese elemento solo si se cumple la condicion
    # Crear un list comprehension, una lista con multiplos de 4 que a su vez tambien sean multiplos de 6 y de 9 hasta 5 digitos 
            
    # multiplos = []
    # for i in range (1, 1001):
    #     if i % 4 == 0 and i % 6 == 0 and i % 9 == 0:
    #         multiplos.append(i)
    # print(multiplos)
    

    # Ahora en una sola linea 

    multiplos = [ i for i in range(1, 1001) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    print(multiplos)
if __name__ == "__main__":
    run()