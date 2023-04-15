from simplebot import SimpleBot
import wikipedia

# Inicializar el bot
bot = SimpleBot()

# Definir la función para buscar en Wikipedia
def search_wikipedia(query):
     try:
         # Realizar la búsqueda en Wikipedia
         result = wikipedia.summary(query, sentences=3)
         return result
     except:
         return "Lo siento, no pude encontrar información sobre eso en 
Wikipedia."

# Definir el comando /wiki
@bot.command('wiki')
def wiki_command(message):
     # Obtener el término de búsqueda
     query = message.text.split(' ', 1)[1]
     # Realizar la búsqueda en Wikipedia
     result = search_wikipedia(query)
     # Enviar el resultado al usuario
     bot.send_message(message.chat.id, result)

# Ejecutar el bot
bot.run()
