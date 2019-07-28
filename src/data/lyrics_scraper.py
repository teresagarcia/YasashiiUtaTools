from bs4 import BeautifulSoup as bs

def get_english_lyrics(raw_html):
    table =  raw_html.find_all('article')[0]
    div = table.find_all('div')[2]
    pinside = div.find_all('p')
    return pinside