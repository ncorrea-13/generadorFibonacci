import math
import statistics
from collections import Counter
import numpy as np

# Assuming generador.py and transformadas.py are in the same directory
from generador import generador_fibonacci
from transformadas import transformada_inversa_discreta, aceptacion_rechazo_continua


# Clasificador para Poker
def clasificar_poker(digitos):
    conteo = Counter(digitos)
    valores = sorted(conteo.values(), reverse=True)
    if valores == [5]:
        return "Quintilla"
    if valores == [4, 1]:
        return "Poker"
    if valores == [3, 2]:
        return "Full"
    if valores == [3, 1, 1]:
        return "Tercia"
    if valores == [2, 2, 1]:
        return "Dos pares"
    if valores == [2, 1, 1, 1]:
        return "Un par"
    return "Todos diferentes"


# Lógica principal
def sistema_general(tipo, test, semilla, a, c, m, n, umbral):
    if tipo == "Variable Aleatoria":
        if test == "Transformada Inversa":
            return transformada_inversa_discreta(n)
        elif test == "Aceptación-Rechazo":
            return aceptacion_rechazo_continua(n)
        else:
            return None, "❌ Este método corresponde a variables aleatorias."

    numeros = generador_fibonacci(n, valorSemilla=semilla)

    if test == "Generador":
        return None, "Secuencia: " + ", ".join(f"{x:.4f}" for x in numeros)

    elif test == "Kolmogorov-Smirnov":
        numeros.sort()
        d_mas = [(i + 1) / n - numeros[i] for i in range(n)]
        d_menos = [numeros[i] - i / n for i in range(n)]
        d_estadistico = max(max(d_mas), max(d_menos))
        texto = f"D = {d_estadistico:.5f}, D crítico = {umbral:.5f}\n"
        texto += "✅ Aceptado" if d_estadistico < umbral else "❌ Rechazado"
        return None, texto

    elif test == "Chi-Cuadrado":
        k = 10
        intervalos = [0] * k
        for x in numeros:
            idx = int(x * k)
            if idx == k:
                idx -= 1
            intervalos[idx] += 1
        fe = n / k
        chi2 = sum((fo - fe) ** 2 / fe for fo in intervalos)
        texto = f"Chi² = {chi2:.4f}, Crítico = {umbral:.4f}\n"
        texto += "✅ Aceptado" if chi2 < umbral else "❌ Rechazado"
        return None, texto

    elif test == "Rachas":
        media = statistics.mean(numeros)
        secuencia = ["+" if x >= media else "-" for x in numeros]
        b = 1 + sum(secuencia[i] != secuencia[i - 1] for i in range(1, n))
        n1 = secuencia.count("-")
        n2 = secuencia.count("+")
        eb = (2 * n1 * n2) / n + 0.5
        vb = (2 * n1 * n2 * (2 * n1 * n2 - n)) / (n**2 * (n - 1))
        zb = (b - eb) / math.sqrt(vb) if vb > 0 else 0
        texto = f"Z observado = {zb:.4f}, Z crítico = {umbral:.4f}\n"
        texto += "✅ Aceptado" if abs(zb) < umbral else "❌ Rechazado"
        return None, texto

    elif test == "Poker":
        manos = [f"{int(x * 100000):05d}" for x in numeros[: (n // 5) * 5]]
        probs = {
            "Todos diferentes": 0.3024,
            "Un par": 0.5040,
            "Dos pares": 0.1080,
            "Tercia": 0.0720,
            "Full": 0.0090,
            "Poker": 0.0045,
            "Quintilla": 0.0001,
        }
        conteo = Counter(clasificar_poker(mano) for mano in manos)
        total = len(manos)
        chi2 = sum(
            ((conteo.get(k, 0) - total * p) ** 2) / (total * p)
            for k, p in probs.items()
        )
        texto = f"Chi² = {chi2:.4f}, Crítico = {umbral:.4f}\n"
        texto += "✅ Aceptado" if chi2 < umbral else "❌ Rechazado"
        return None, texto

    elif test == "Serial":
        k = 5
        parejas = [(numeros[i], numeros[i + 1]) for i in range(0, n - 1, 2)]
        tabla = [[0] * k for _ in range(k)]
        for x, y in parejas:
            i, j = min(int(x * k), k - 1), min(int(y * k), k - 1)
            tabla[i][j] += 1
        fe = len(parejas) / (k * k)
        chi2 = sum(((tabla[i][j] - fe) ** 2) / fe for i in range(k) for j in range(k))
        texto = f"Chi² serial = {chi2:.4f}, Crítico = {umbral:.4f}\n"
        texto += "✅ Aceptado" if chi2 < umbral else "❌ Rechazado"
        return None, texto

    return None, "❌ Test no reconocido."
