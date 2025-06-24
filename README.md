# Generador Fibonacci con Tests Estadísticos

## Propósito
Este proyecto implementa un generador de números aleatorios basado en el algoritmo Fibonacci atrasado, junto con una interfaz gráfica y herramientas para realizar pruebas estadísticas sobre los números generados. Además, incluye métodos para generar variables aleatorias utilizando transformadas.

## Características
- **Generador Fibonacci:** Capaz de generar secuencias de números aleatorios con parámetros personalizables.
- **Transformadas:** Métodos de Transformada Inversa y Aceptación-Rechazo para generar variables aleatorias.
- **Pruebas Estadísticas:** Implementación de pruebas como Kolmogorov-Smirnov, Chi-Cuadrado, Rachas, Poker y Serial para evaluar la calidad de los números generados.
- **Interfaz gráfica:** Utiliza Gradio para proporcionar una interfaz interactiva que permite seleccionar métodos, parámetros y visualizar resultados.

## Requisitos
- Python 3.x
- Las siguientes librerías de Python:
  - `gradio`
  - `matplotlib`
  - `numpy`

  Puedes instalarlas ejecutando:
  ```bash
  pip install -r requirements.txt
  ```

## Estructura del Proyecto
- `main.py`: Punto de entrada del proyecto.
- `interfaz.py`: Define la interfaz gráfica usando Gradio.
- `generador.py`: Contiene el algoritmo del generador Fibonacci atrasado.
- `test_estadisticos.py`: Contiene las pruebas estadísticas para evaluar la calidad de los números generados.
- `transformadas.py`: Métodos para generar variables aleatorias.
- `requirements.txt`: Lista de dependencias necesarias.

## Cómo Ejecutar
1. Instala los requisitos:
   ```bash
   pip install -r requirements.txt
   ```
2. Ejecuta el archivo principal:
   ```bash
   python main.py
   ```
3. Abre el enlace generado en tu navegador para interactuar con la interfaz gráfica.

## Uso
### Generador Fibonacci
Puedes generar números aleatorios configurando los parámetros del generador como `j`, `k`, y `mod`. También puedes proporcionar una semilla para reproducibilidad.

### Transformadas
- **Transformada Inversa:** Genera variables aleatorias discretas de acuerdo a una distribución dada.
- **Aceptación-Rechazo:** Genera variables aleatorias continuas basadas en criterios de aceptación y rechazo.

### Tests Estadísticos
Evalúa los números generados usando los siguientes tests:
- **Kolmogorov-Smirnov:** Evalúa si los números siguen una distribución uniforme.
- **Chi-Cuadrado:** Analiza la frecuencia de los números en diferentes intervalos.
- **Rachas:** Determina si la secuencia muestra patrones significativos.
- **Poker:** Clasifica manos de Poker generadas por los números.
- **Serial:** Evalúa la independencia de números consecutivos.

## Créditos
Este proyecto fue desarrollado para fines educativos y de análisis estadístico. ¡Siéntete libre de contribuir o mejorar!

---

