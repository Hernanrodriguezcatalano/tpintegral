def get_int():
    while True:
        try:
            return int(input("Ingrese un número entero: "))
        except ValueError:
            print("Valor no válido. Intente nuevamente.")

def get_int_recursive():
    try:
        return int(input("Ingrese un número entero: "))
    except ValueError:
        print("Valor no válido. Intente nuevamente.")
        return get_int_recursive()
