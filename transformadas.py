import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
from generador import generador_fibonacci


# Transformada Inversa para variable aleatoria discreta
def transformada_inversa_discreta(n, valorSemilla=None):
    valores = [1, 2, 3, 4]
    probabilidades = [0.1, 0.2, 0.3, 0.4]
    acumulada = [sum(probabilidades[: i + 1]) for i in range(len(probabilidades))]
    resultados = []
    valores_aleatorios = generador_fibonacci(n, valorSemilla=valorSemilla)
    for u in valores_aleatorios:
        for i, p_acum in enumerate(acumulada):
            if u <= p_acum:
                resultados.append(valores[i])
                break

    # Contar ocurrencias
    conteo = Counter(resultados)
    conteo_str = "\nConteo de variables generadas:\n"
    for valor in valores:
        conteo_str += f"Variable {valor}: {conteo.get(valor, 0)}\n"

    fig, ax = plt.subplots()
    ax.hist(
        resultados,
        bins=np.arange(min(valores), max(valores) + 2) - 0.5,
        edgecolor="black",
        rwidth=0.8,
    )
    ax.set_title("Transformada Inversa - Variable Aleatoria Discreta")
    return fig, conteo_str + "\n".join(map(str, resultados))


# Aceptación y Rechazo para variable aleatoria continua
def aceptacion_rechazo_continua(n, valorSemilla=None):
    a, b = 0, 1
    M = 2
    muestras = []
    log_resultado = []

    r1_vals = generador_fibonacci(n, valorSemilla=valorSemilla)
    r2_vals = generador_fibonacci(n, valorSemilla=valorSemilla)

    for r1, r2 in zip(r1_vals, r2_vals):
        x_star = a + (b - a) * r1
        y_star = 2 * x_star
        aceptado = r2 <= y_star / M

        if aceptado:
            muestras.append(x_star)
            log_resultado.append(
                f"Aceptado: x={x_star:.4f}, y={y_star:.4f}, r2={r2:.4f}"
            )
        else:
            log_resultado.append(
                f"Rechazado: x={x_star:.4f}, y={y_star:.4f}, r2={r2:.4f}"
            )

    fig, ax = plt.subplots()
    bins = round(np.sqrt(len(muestras)))
    ax.hist(muestras, bins=bins, density=True, alpha=0.7)
    ax.plot(
        np.linspace(a, b, 100),
        [2 * t for t in np.linspace(a, b, 100)],
        "r",
        label="f(x)=2x",
    )
    ax.set_title("Aceptación-Rechazo - Variable Continua")
    ax.legend()

    return fig, "\n".join(log_resultado)
