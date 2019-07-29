from googlesearch import search 
from bs4 import BeautifulSoup as bs
import requests

# Controlar error HTTP Error 429: Too Many Requests (!!)
def get_urls(query):
    urls = []
    for i in search(query, tld="es", num=20, stop=25, pause=2): 
        urls.append(i)
    return urls

def get_html(url):
    response = requests.get(url)
    html_text = bs(response.text, 'html.parser')
    return html_text

def get_title(html):
    if html.title is not None:
        title = html.title.string
    else:
        title = "Sin título"
    return title

def check_title(title, artist, song_name):
    is_target_page = False
    if artist.lower() in title.lower() and song_name.lower() in title.lower():
        is_target_page = True
    return is_target_page
