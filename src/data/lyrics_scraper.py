from bs4 import BeautifulSoup as bs

def get_original_lyrics(raw_html):
    return raw_html.find_all("table")