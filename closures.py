#hola 3 -> holaholahola
#esta sera la idea de este programa ingresar el dato a repetir y las veces que lo hara 

from timeit import repeat


def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "Solo puedes ingresar cadenas"
        return string*n
    return repeater    

def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5("hola"))



if __name__ == "__main__":
    run()