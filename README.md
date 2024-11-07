# Miaumis
## Chatbot de Cuidado y Asistencia para Gatos Domésticos

---

## Descripción general
Miaumis es un chatbot diseñado para ofrecer consejos sobre el cuidado general de gatos, responder preguntas frecuentes sobre salud, alimentación y comportamiento felino, y guiar a los tutores en el manejo adecuado de sus mascotas. Además, sugiere cuándo es necesario consultar a un veterinario para casos más graves.

## Objetivo
Facilitar el acceso a información confiable sobre el cuidado de gatos para mejorar su bienestar y calidad de vida.

## Destinatarios
Tutores de gatos domesticos, dueños de mascotas, veterinarios, y cualquier persona interesada en el bienestar de los gatos.

---

## Arquitectura

### Interfaz de usuario (UI)
Implementada con Streamlit, la interfaz permite una interacción amigable mediante una ventana de chat. Los usuarios pueden enviar preguntas, recibir respuestas, y tienen acceso a la opcion de borrar el historial para reiniciar la conversación y la memoria.

### Backend
Incluye los siguientes archivos principales:
- app.py: Responsable de la interfaz de usuario, configuración de las columnas, botones, e integración con el modelo de chat.
- embeddings.ipynb: Utiliza embeddings de OpenAI para procesar y almacenar documentos en una base de datos de Chroma, facilitando la recuperación de información relevante de la base de conocimiento sobre el cuidado de gatos.
- main.py: Configura el agente de inteligencia artificial basado en GPT-3.5-Turbo, así como herramientas de recuperación de información y memoria de conversación para mejorar la continuidad y calidad de las respuestas.
- Motor de IA: El chatbot utiliza GPT-3.5-Turbo como motor principal, empleando prompts específicos para asegurar que las respuestas sean precisas, empáticas y centradas en el cuidado de gatos domésticos.

---

## Interacción del Usuario con el Bot y Flujo de conversación

El bot sigue un flujo de conversación que permite a los usuarios recibir respuestas detalladas y útiles en base a sus consultas. 

Ejemplos de interacción:
- Consulta del usuario: ¿Cómo puedo mejorar la dieta de mi gato?
- Respuesta de Miaumis: Puede sugerir consejos sobre nutrición específica para gatos y advertencias sobre alimentos no recomendados.

Preguntas Frecuentes:
Los usuarios pueden hacer preguntas como:
- ¿Qué hacer si mi gato muestra signos de estrés?
- ¿Cuántas veces al día debo alimentar a mi gato?
- ¿Cómo puedo hacer que mi gato use el rascador?

---

## Instrucciones de Configuración
Abrir terminal o IDE y ejecutar el siguiente comando:
1) Crear el entorno virtual: python -m venv env
2) Activar el entorno virtual: env/scripts/activate
3) Instalar dependencias: pip install -r requirements.txt
4) El usuario deberá colocar su API Key en el archivo .env.
5) Ejecutar la notebook embeddings.ipynb para crear la base de datos Chroma con información relevante sobre el cuidado de gatos.
- Notas:Si encuentras problemas de autorización en Windows, ejecuta el siguiente comando en PowerShell como administrador: 'Set-ExecutionPolicy RemoteSigned -Scope LocalMachine' y luego, confirma con "s" y repite desde el paso 2.

También, información más detallada sobre la instalación y el funcionamiento del software se encuentra disponible dentro del directorio miaumis, en el archivo setup.txt.
