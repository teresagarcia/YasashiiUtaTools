import sys
sys.path.append('src') 
from constants import constants
from search.search import check_title, get_title, get_html, get_urls
from data.song import Song
import scrapers.lyrics_scraper as scraper
import scrapers.kpop_post2015 as kpop2015
import json

output_file = constants.BASE_INFO
song = Song()

def __get_page(urls):
    url = ""
    html = ""
    for i in urls:
            tmp_html = get_html(i)
            title = get_title(tmp_html)
            if check_title(title, song.artist, song.song_name):
                url = i 
                html = tmp_html
                break 
    if url == "":
        raise ValueError("No se encontró la página")    
    return url, html

def set_search_data():
    print("Dime el artista:")
    artist = input()
    print("Y la canción:")
    song_name = input()
    return artist, song_name

def __get_page_data(queries):
    page_data = {}
    page_data["original_url"], page_data["original_html"] = __get_page(get_urls(queries["original_rom_lyrics"]))
    page_data["transliteration_url"], page_data["transliteration_html"] = __get_page(get_urls(queries["original_rom_lyrics"]))
    page_data["translation_url"], page_data["translation_html"] = __get_page(get_urls(queries["english_lyrics"]))
    return page_data

def extract_lyrics():
    song.artist, song.song_name = set_search_data()

    queries = kpop2015.get_queries(song.artist, song.song_name)
    
    page_data = __get_page_data(queries)

    song.original_url = page_data["original_url"],
    song.transliteration_url = page_data["transliteration_url"]
    song.translation_url = page_data["translation_url"]
    song.original = scraper.get_original_lyrics(page_data["original_html"])
    song.transliteration = scraper.get_romanization(page_data["transliteration_html"])
    song.translation = scraper.get_english_lyrics(page_data["translation_html"] )
    
    with open(output_file, 'w') as outfile:
        json.dump(song.toJSON(), outfile)
    
    print("Éxito~")

if __name__ == '__main__':
    extract_lyrics()