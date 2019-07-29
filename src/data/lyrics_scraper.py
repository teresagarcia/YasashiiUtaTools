from bs4 import BeautifulSoup as bs

# Con ilyricsbuzz.com
def get_original_lyrics(raw_html):
    content = raw_html.find_all('div', {"class": "td-post-content"})[0]
    return content.get_text()

# Con popgasa.com
def get_english_lyrics(raw_html):
    content = raw_html.find('div', {"class": "entry-content"})
    content.find('div', {'class': 'sharedaddy'}).decompose()
    return content.get_text()