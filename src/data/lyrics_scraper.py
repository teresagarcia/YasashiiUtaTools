from bs4 import BeautifulSoup as bs
import re

def get_content(raw_html):
    content = raw_html.find('div', {"class": "entry-content"})
    content.find('div', {'class': 'code-block code-block-2'}).decompose()
    content.find('div', {'class': 'code-block code-block-3'}).decompose()
    return content

def get_final_text(content_text, inter_filter, final_filter):
    inter_text = re.search(inter_filter, content_text).group(1)
    final_text = re.search(final_filter, inter_text).group(1)
    return final_text

# Con ilyricsbuzz.com
def get_original_lyrics(raw_html):
    content = get_content(raw_html)
    inter_filter = re.compile('HANGUL(.*)MUSIC VIDEO', re.S) #Revisar 
    final_filter = re.compile('HANGUL(.*)', re.S)
    final_text = get_final_text(content.get_text(), inter_filter, final_filter)
    return final_text

# Con ilyricsbuzz.com
def get_romanization(raw_html):
    content = get_content(raw_html)
    inter_filter = re.compile('ROMANIZATION(.*)ENGLISH TRANSLATION', re.S)
    final_filter = re.compile('ROMANIZATION(.*)', re.S)
    final_text = get_final_text(content.get_text(), inter_filter, final_filter)
    return final_text

# Con popgasa.com
def get_english_lyrics(raw_html):
    content = raw_html.find('div', {"class": "entry-content"})
    content.find('div', {'class': 'sharedaddy'}).decompose()
    return content.get_text()
