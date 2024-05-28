from models.persona import Persona
from models.cuenta import Cuenta
from models.cuenta_joven import CuentaJoven
from Utils.math_operations import mcd, mcm
from Utils.text_operations import contar_palabras, palabra_mas_frecuente
from Utils.input_operations import get_int, get_int_recursive

def main():
    # Ejemplo de uso de las funciones y clases
    
    # Operaciones matemáticas
    print("MCD de 54 y 24:", mcd(54, 24))
    print("MCM de 54 y 24:", mcm(54, 24))

    # Operaciones con texto
    texto = "Hola mundo mundo"
    frecuencia = contar_palabras(texto)
    print("Frecuencia de palabras:", frecuencia)
    palabra, freq = palabra_mas_frecuente(frecuencia)
    print(f"La palabra más frecuente es '{palabra}' con una frecuencia de {freq}")

    # Obtener un entero del usuario
    numero = get_int()
    print("Número ingresado:", numero)

    # Crear y mostrar una Persona
    persona = Persona("Juan", 20, "12345678A")
    print(persona.mostrar())

    # Crear y mostrar una Cuenta
    cuenta = Cuenta(persona, 100.50)
    cuenta.ingresar(50)
    cuenta.retirar(30)
    print(cuenta.mostrar())

    # Crear y mostrar una Cuenta Joven
    cuenta_joven = CuentaJoven(persona, 200.75, 10)
    if cuenta_joven.es_titular_valido():
        cuenta_joven.retirar(50)
    print(cuenta_joven.mostrar())

if __name__ == "__main__":
    main()
