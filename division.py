def dividir(a, b):
    if(b != 0):
        return a / b
    else:
        return 'Operacion no permitida'

if __name__ == "__main__":
    print(dividir(5, 3))