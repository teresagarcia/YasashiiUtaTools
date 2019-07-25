from googlesearch import search 
from bs4 import BeautifulSoup as bs
import requests

def get_urls(query):
    urls = []
    for i in search(query, tld="es", num=20, stop=25, pause=2): 
        urls.append(i)
    return urls

def get_title(url):
    response = requests.get(url)
    html_text = bs(response.text, 'html.parser')
    if html_text.title is not None:
        title = html_text.title.string
    else:
        title = "Sin título"
    return title

def check_title(title, artist, song_name):
    if artist.lower() in title.lower() and song_name.lower() in title.lower():
        print("guardar")
    else:
        print("ignorar")
