import gradio as gr
from test_estadisticos import sistema_general  # Import the main logic function


# Interfaz dinámica
def actualizar_campos(tipo):
    if tipo == "Número Aleatorio":
        return (
            gr.update(
                choices=[
                    "Generador",
                    "Kolmogorov-Smirnov",
                    "Chi-Cuadrado",
                    "Rachas",
                    "Poker",
                    "Serial",
                ],
                value="Generador",
            ),
            gr.update(visible=True),  # semilla
            gr.update(visible=False),  # a
            gr.update(visible=False),  # c
            gr.update(visible=False),  # m
        )
    else:
        return (
            gr.update(
                choices=["Transformada Inversa", "Aceptación-Rechazo"],
                value="Transformada Inversa",
            ),
            gr.update(visible=True),  # semilla
            gr.update(visible=False),  # a
            gr.update(visible=False),  # c
            gr.update(visible=False),  # m
        )


with gr.Blocks() as demo:
    tipo = gr.Radio(
        ["Número Aleatorio", "Variable Aleatoria"],
        label="Tipo de Simulación",
        value="Número Aleatorio",
    )
    test = gr.Dropdown(choices=[], label="Test o Método")
    n = gr.Slider(10, 1000, step=10, label="Cantidad", value=100)
    semilla = gr.Number(label="Semilla", visible=False)
    a = gr.Number(label="Multiplicador (a)", visible=False)
    c = gr.Number(label="Incremento (c)", visible=False)
    m = gr.Number(label="Módulo (m)", visible=False)
    umbral = gr.Number(label="Valor crítico (de la tabla correspondiente)", value=1.96)
    btn = gr.Button("Ejecutar")
    grafico = gr.Plot()
    salida = gr.Textbox()

    tipo.change(fn=actualizar_campos, inputs=tipo, outputs=[test, semilla, a, c, m])
    btn.click(
        fn=sistema_general,
        inputs=[tipo, test, semilla, a, c, m, n, umbral],
        outputs=[grafico, salida],
    )

demo.launch()
