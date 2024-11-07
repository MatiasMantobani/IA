import streamlit as st
from main import *
from PIL import Image
import time

img = Image.open("imagen.png")

st.set_page_config(page_title="Ayudante Gatuno", page_icon = img)

# Crear 3 columnas
col1, col2, col3 = st.columns(3)

# Colocar contenido en la columna del medio (col2)
with col2:
    # Título que ocupa todo el ancho usando CSS
    st.markdown("<h1 style='width: auto; text-align: center;'>Ayudante Gatuno</h1>", unsafe_allow_html=True)

    # Imagen
    st.image(img, width=200, caption="Hola, soy Miaumis, tu ayudante para asistirte con todas tus preguntas sobre gatos domésticos")

    # Botón para borrar historial
    if st.button("Borrar historial", key="clear_history", help="Haz clic para borrar el historial"):
        st.session_state.messages = []  # Limpia los mensajes en el estado de sesión
        chat_history = []  # Reinicia el historial de chat
        memory.clear()  # Limpia la memoria


usuario = "🧑🏻"
bot = "😺"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    
# Display chat messages from history on app rerun
for message in st.session_state.messages:
    avatar = usuario if message["role"] == "user" else bot
    with st.chat_message(message["role"], avatar = avatar):
        st.markdown(message["content"])
        
# Accept user input
if prompt := st.chat_input("Ingrese su consulta:"):
    while prompt is None:
        time.sleep()
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user", avatar = usuario):
        st.markdown(prompt)
        
    chat_history = "\n".join([message["content"] for message in st.session_state.messages if message["role"] == "user"])
        
    with st.chat_message("assistant", avatar = bot):
       contenedor_respuesta = st.empty()
       full_response = ""

# manejo de visualizacion natural del chatbot escribiendo
    respuesta = chatbot(prompt, chat_history)
    full_response = ""  # Inicializa la variable completa

    for line in respuesta.splitlines():  # Divide la respuesta en líneas para conservar los bullets y párrafos
        current_line = ""  # Línea actual que se va a mostrar progresivamente

        # Agrega un salto de línea solo antes del primer bullet si full_response está vacío
        if full_response == "":
            full_response += "\n\n"

        for word in line.split():  # Divide la línea en palabras
            current_line += word + " "  # Agrega cada palabra con un espacio
            contenedor_respuesta.markdown(
                f"<div class='assistant-message'>{full_response + current_line}▌</div>",
                unsafe_allow_html=True,
            )
            time.sleep(0.15)  # Ajusta el tiempo para controlar la velocidad de escritura

        # Agrega la línea completa al texto acumulado con un salto de línea
        # full_response += current_line + "\n\n"
        full_response += current_line.strip() + "\n\n"

    # Muestra la respuesta final sin el símbolo "▌"
    contenedor_respuesta.markdown(
        f"<div class='assistant-message'>{full_response.rstrip()}</div>",
        unsafe_allow_html=True,
    )

#
    st.session_state.messages.append({"role": "assistant", "content": respuesta})