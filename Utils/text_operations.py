def contar_palabras(cadena):
    palabras = cadena.split()
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia

def palabra_mas_frecuente(frecuencia):
    max_palabra = max(frecuencia, key=frecuencia.get)
    return max_palabra, frecuencia[max_palabra]
