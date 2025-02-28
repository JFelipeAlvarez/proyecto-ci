def es_primo(x):
    if x < 2:  # Los números menores que 2 no son primos
        return False
    i = 0
    for n in range(2, x):  # Comienza desde 2, porque 1 siempre divide a cualquier número
        if x % n == 0:
            i += 1
    if i == 0:
        return True  # Si no hemos encontrado divisores, es primo
    return False  # Si encontramos divisores, no es primo
