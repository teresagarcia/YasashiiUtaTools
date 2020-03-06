import sys
sys.path.append('src') 
from googlesearch import search 
from bs4 import BeautifulSoup as bs
import requests
from utils.text_utils import clean_text

def get_urls(*queries):
    all_urls = []
    try:
        for query in queries:
            urls = []
            for i in search(query, tld="es", num=20, stop=25, pause=2): 
                urls.append(i)
            all_urls.append(urls)
        return all_urls
    # Controlar error HTTP Error 429: Too Many Requests (!!)
    except:
        print("Demasiadas peticiones, intenta de nuevo dentro de un rato...")

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

def isTextInTitle(page_title, song_title, artist):
    return song_title in page_title and artist in page_title

def check_title(title, artist, song_name):
    is_target_page = False
    title, artist, song_name = clean_text(title, artist, song_name)
    if isTextInTitle(title, song_name, artist):
        is_target_page = True
    return is_target_page


def search_page(urls, artist, song_name):
    url = ""
    html = ""
    for tmp_url in urls:
            tmp_html = get_html(tmp_url) 
            title = get_title(tmp_html) 
            if check_title(title, artist, song_name):
                url = tmp_url 
                html = tmp_html
                break 
    if url == "":
        raise ValueError("No se encontró la página")    
    return url, html