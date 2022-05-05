from unicodedata import name


# sintaxis
# lambda argumentos: expresion


def run():
    palindrome = lambda string: string == string[ ::-1]
    
    print(palindrome("webos"))

if __name__ == "__main__":
    run()   