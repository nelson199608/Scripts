import requests
import random
import simplebot
from deltachat import Message
from simplebot.bot import DeltaBot, Replies
from bs4 import BeautifulSoup


@simplebot.filter(trylast=True)
def search_filter(bot: DeltaBot, message: Message, replies: Replies) -> None:
    if message.text and message.text.strip().lower().startswith("/bing"):
        query = message.text.strip()[len("/bing"):].strip()
        if query:
            image_urls = _search_images(query)
            if len(image_urls) == 0:
                replies.add(text="No se encontraron imágenes para la búsqueda: " + query)
                return
            random.shuffle(image_urls)
            for i in range(min(5, len(image_urls))):
                image_url = image_urls[i]
                image_data = requests.get(image_url).content
                replies.add(image=image_data, quote=message)


def _search_images(query: str) -> list:
    image_urls = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    search_url = "https://www.bing.com/images/search?q=" + query
    response = requests.get(search_url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        image_divs = soup.find_all('div', {'class': 'imgpt'})
        for div in image_divs:
            image_url = div.find('a')['href']
            image_urls.append(image_url)
    return image_urls
