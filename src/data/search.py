from googlesearch import search 
from bs4 import BeautifulSoup as bs
import requests
import re

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

def clean_text(*text):
    test_re = '[^A-Za-z0-9]+'
    keywords = []
    [keywords.append(re.sub(test_re, '', word).lower()) for word in text]
    return keywords

def isTextInTitle(page_title, song_title, artist):
    return song_title in page_title and artist in page_title

def check_title(title, artist, song_name):
    is_target_page = False
    title, artist, song_name = clean_text(title, artist, song_name)
    if isTextInTitle(title, song_name, artist):
        is_target_page = True
    return is_target_page
