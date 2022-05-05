from functools import reduce
def run():
# funcion que recibe como parametro a otra funcion 
# filter: esta recibe dos parametros; una lambda y un iterable.....retorna un iterador
    # my_list = [1,3,8,6,4,46,90]
    # odd = list(filter(lambda x: x % 2 != 0, my_list))

    # print(odd)


#map
#ejemplo con list comprehensions
    nums = [1, 2, 3, 4, 5,]
    # nums2 = [i**2 for i in nums]
    # print(nums2)

#ahora con map
    nums2 = list(map(lambda x: x**2, nums))
    print(nums2)


#reduce

    my_list = [2, 2, 2, 2, 2]
#     multiplicador = 1

#     for i in my_list:
#         multiplicador = multiplicador * i

#     print(multiplicador)       
# #ahora con reduce

    multiplicador = reduce(lambda a, b: a * b, my_list )
    print(multiplicador)



if __name__ == "__main__":
    run()