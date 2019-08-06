from bs4 import BeautifulSoup as bs
import re

# Con ilyricsbuzz.com
def get_original_lyrics(raw_html):
    content = raw_html.find('div', {"class": "td-post-content"})
    content.find('div', {'class': 'code-block code-block-2'}).decompose()
    content.find('div', {'class': 'code-block code-block-3'}).decompose()
    b = re.compile('HANGUL(.*)ROMANIZATION', re.S)
    c = re.compile('HANGUL(.*)MUSIC VIDEO', re.S)
    final_text = re.search(b, content.get_text()).group(1)
    final_text2 = re.search(c, final_text).group(1)
    return final_text2

# Con popgasa.com
def get_english_lyrics(raw_html):
    content = raw_html.find('div', {"class": "entry-content"})
    content.find('div', {'class': 'sharedaddy'}).decompose()
    return content.get_text()