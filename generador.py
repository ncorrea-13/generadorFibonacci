import random


def generador_fibonacci(n, j=5, k=17, mod=1.0, valorSemilla=None):
    if j >= k or j <= 0:
        raise ValueError("Se requiere 0 < j < k para el generador Fibonacci atrasado")

    if valorSemilla is not None:
        random.seed(valorSemilla)

    seed = [random.random() for _ in range(k)]
    secuencia = seed[:]
    for _ in range(n):
        nuevo = (secuencia[-j] + secuencia[-k]) % mod
        secuencia.append(nuevo)

    return secuencia[-n:]
