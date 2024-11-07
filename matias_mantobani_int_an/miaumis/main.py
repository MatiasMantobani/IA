from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory, ChatMessageHistory, ConversationBufferWindowMemory
from langchain.tools.retriever import create_retriever_tool
from langchain import hub
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain.tools import Tool
from langchain.utilities import PythonREPL
from langchain_community.tools import YouTubeSearchTool

#cargamos variables de entorno
load_dotenv()

#Definimos funcion de embeddings
embeddings_function = OpenAIEmbeddings()

#Instanciamos el modelo
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature= 0    
)

#Cargamos la db
db = Chroma(
    persist_directory = 'docs/Chroma',
    embedding_function = embeddings_function
)

retriever = db.as_retriever()

#Crear memoria para agente

memory = ConversationBufferWindowMemory(
    memory_key='chat_history',
    k=4,
    return_messages=True,
    chat_memory=ChatMessageHistory()
)

# Creamos una herramienta de ejecución de código Python con un nombre válido
python_repl = Tool(
    name="python_repl",  # Nombre de la función corregido
    func=PythonREPL().run,
    description="useful for when you need to use python to answer a question. You should call the function with a string that contains the full python code to run."
)

#Creamos una tool de búsqueda
busqueda_informacion_gatos = create_retriever_tool(
    retriever=retriever,
    name='busqueda_informacion_gatos',
    description="Search for and return information on domestic cat care"
)

videos_youtube = YouTubeSearchTool()

# Agregamos la herramienta a la lista de herramientas
tools = [busqueda_informacion_gatos, python_repl, videos_youtube]

# Definir Prompt
prompt = hub.pull("hwchase17/openai-tools-agent")
prompt.messages[0].prompt.template = """
Eres Miaumis, un asistente virtual especializado exclusivamente en el cuidado de gatos domésticos, dirigido a amantes de los gatos. Tu tarea es proporcionar información precisa y accesible sobre el cuidado de gatos, utilizando siempre un tono amable y cariñoso.

Instrucciones:
1. **Uso del documento de referencia**: Siempre consulta primero el documento de referencia provisto mediante la herramienta de recuperación (retriever) antes de responder. Usa exclusivamente la información del documento cuando esté disponible.
2. **Temas**: Responde únicamente sobre temas de gatos domésticos. No hagas referencias a futuros temas o preguntas que no sean sobre gatos. Si recibes una consulta sobre otro tema, deberas explicarle al usuario con amabilidad que solo puedes brindar información sobre el cuidado de gatos.
3. **Extensión de las respuestas**: Mantén tus respuestas concisas, con un máximo de 200 palabras.
4. **Formato**: Usa listas con viñetas cuando sea útil para organizar la información y utiliza negrita cuando lo creas conveniente.
5. **Lenguaje**: Evita el uso de groserías en tus respuestas y no repitas ninguna palabra ofensiva que el usuario haya mencionado.
6. **Personaje**: No adoptes un comportamiento de gato ni uses términos como "miau".

Recuerda, tu objetivo es ser un recurso confiable y empático exclusivamente para temas relacionados con el cuidado de gatos, y siempre debes consultar el documento de referencia antes de proporcionar una respuesta.

"""

#Creamos el agente
agent = create_openai_tools_agent(
    llm= llm,
    tools= tools,
    prompt=prompt
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    memory=memory,
    verbose=True
)

def chatbot(query:str, chat_history):
    response = agent_executor.invoke({'input': f'{query}', "chat_history":chat_history })['output']
    return response
