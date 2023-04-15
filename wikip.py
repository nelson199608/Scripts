from urllib.parse import quote_plus

import simplebot
from deltachat import Message
from simplebot.bot import DeltaBot, Replies
from simplebot_instantview import prepare_html, session  # noqa
import wikipedia

# Definir la función para buscar en Wikipedia
def search_wikipedia(query):
     try:
         # Realizar la búsqueda en Wikipedia
         result = wikipedia.summary(query, sentences=3)
         return result
     except:
         return "Lo siento, no pude encontrar información sobre eso en 
Wikipedia."
@simplebot.command()
	def wiki(bot: DeltaBot, message: Message, replies: Replies)->None:
	"""Search in Wikipedia"""
		# Obtener el término de búsqueda
     query = message.text.split(' ', 1)[1]
     # Realizar la búsqueda en Wikipedia
     result = search_wikipedia(query)
     # Enviar el resultado al usuario
     bot.send_message(message.chat.id, result)
