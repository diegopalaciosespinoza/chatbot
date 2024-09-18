import streamlit as st

# Función para el chatbot que genera bloques de Streamlit
def chatbot():
    st.title("Chatbot Generador de Bloques para Streamlit")

    # Pregunta inicial
    st.write("¡Hola! Te ayudaré a crear una aplicación en Streamlit. Selecciona el bloque que deseas agregar:")

    # Menú para elegir el tipo de bloque
    block_type = st.selectbox("Elige el tipo de bloque que deseas agregar:", 
                              ("Texto", "Gráfico", "Imagen", "Entrada de usuario", "Datos"))

    # Dependiendo del bloque, muestra más opciones
    if block_type == "Texto":
        st.write("Has seleccionado **Texto**. ¿Qué tipo de texto te gustaría agregar?")
        text_type = st.selectbox("Elige el tipo de texto:", 
                                 ("Título", "Subtítulo", "Párrafo", "Código"))
        
        if text_type == "Título":
            st.write("Para agregar un título, utiliza el siguiente código:")
            st.code('st.title("Tu Título Aquí")')
        elif text_type == "Subtítulo":
            st.write("Para agregar un subtítulo, utiliza el siguiente código:")
            st.code('st.subheader("Tu Subtítulo Aquí")')
        elif text_type == "Párrafo":
            st.write("Para agregar un párrafo de texto, utiliza el siguiente código:")
            st.code('st.write("Este es un párrafo de ejemplo.")')
        elif text_type == "Código":
            st.write("Para agregar un bloque de código, utiliza el siguiente código:")
            st.code('st.code("print(\'Hola Mundo\')")')

    elif block_type == "Gráfico":
        st.write("Has seleccionado **Gráfico**. ¿Qué tipo de gráfico te gustaría agregar?")
        chart_type = st.selectbox("Elige el tipo de gráfico:", 
                                  ("Gráfico de líneas", "Gráfico de barras", "Gráfico de áreas"))
        
        if chart_type == "Gráfico de líneas":
            st.write("Para agregar un gráfico de líneas, utiliza el siguiente código:")
            st.code("""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
st.pyplot(fig)
            """)
        elif chart_type == "Gráfico de barras":
            st.write("Para agregar un gráfico de barras, utiliza el siguiente código:")
            st.code("""
import matplotlib.pyplot as plt

labels = ['A', 'B', 'C', 'D']
values = [10, 24, 36, 18]

fig, ax = plt.subplots()
ax.bar(labels, values)
st.pyplot(fig)
            """)
        elif chart_type == "Gráfico de áreas":
            st.write("Para agregar un gráfico de áreas, utiliza el siguiente código:")
            st.code("""
import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(50, 3),
    columns=["a", "b", "c"])

st.area_chart(df)
            """)

    elif block_type == "Imagen":
        st.write("Has seleccionado **Imagen**. ¿Qué tipo de imagen te gustaría agregar?")
        image_type = st.selectbox("Elige la fuente de la imagen:", 
                                  ("Imagen desde URL", "Imagen local"))

        if image_type == "Imagen desde URL":
            st.write("Para agregar una imagen desde una URL, utiliza el siguiente código:")
            st.code('st.image("https://example.com/imagen.jpg", caption="Descripción de la imagen")')
        elif image_type == "Imagen local":
            st.write("Para agregar una imagen desde un archivo local, utiliza el siguiente código:")
            st.code('st.image("ruta/a/la/imagen.jpg", caption="Descripción de la imagen")')

    elif block_type == "Entrada de usuario":
        st.write("Has seleccionado **Entrada de usuario**. ¿Qué tipo de entrada te gustaría agregar?")
        input_type = st.selectbox("Elige el tipo de entrada:", 
                                  ("Campo de texto", "Número", "Botón", "Desplegable"))

        if input_type == "Campo de texto":
            st.write("Para agregar un campo de texto, utiliza el siguiente código:")
            st.code('st.text_input("Ingrese un valor:")')
        elif input_type == "Número":
            st.write("Para agregar un campo numérico, utiliza el siguiente código:")
            st.code('st.number_input("Ingrese un número:")')
        elif input_type == "Botón":
            st.write("Para agregar un botón, utiliza el siguiente código:")
            st.code('st.button("Clic aquí")')
        elif input_type == "Desplegable":
            st.write("Para agregar un menú desplegable, utiliza el siguiente código:")
            st.code('st.selectbox("Seleccione una opción:", ["Opción 1", "Opción 2", "Opción 3"])')

    elif block_type == "Datos":
        st.write("Has seleccionado **Datos**. ¿Qué tipo de datos te gustaría mostrar?")
        data_type = st.selectbox("Elige cómo te gustaría mostrar los datos:", 
                                 ("Tabla", "DataFrame"))

        if data_type == "Tabla":
            st.write("Para mostrar una tabla de datos, utiliza el siguiente código:")
            st.code("""
data = {
    "Nombre": ["Ana", "Luis", "Pedro"],
    "Edad": [23, 30, 34]
}

st.table(data)
            """)
        elif data_type == "DataFrame":
            st.write("Para mostrar un DataFrame de Pandas, utiliza el siguiente código:")
            st.code("""
import pandas as pd

data = {
    "Nombre": ["Ana", "Luis", "Pedro"],
    "Edad": [23, 30, 34]
}

df = pd.DataFrame(data)
st.dataframe(df)
            """)

# Ejecutar el chatbot
chatbot()