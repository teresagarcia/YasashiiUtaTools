from googlesearch import search 
from bs4 import BeautifulSoup as bs
import requests

def get_urls(query):
    urls = []
    for i in search(query, tld="es", num=20, stop=25, pause=2): 
        urls.append(i)
    return urls

def check_title(url):
    response = requests.get(url)
    html_text = bs(response.text, 'html.parser')
    return html_text.title.string #Falla si no hay título