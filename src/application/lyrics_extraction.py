import sys
sys.path.append('src') 
from constants import constants
from data.song import Song
import scrapers.lyrics_scraper as scraper
import json
from search.add_search_sites import get_source_pages
from search.search import get_urls

output_file = constants.BASE_INFO

def get_queries(artist, song_name, search_sites):
    queries = {}
    for key in search_sites:
        queries[key] = artist + " " + song_name + " " + "site:" + search_sites[key]
    return queries

def __get_search_urls(queries, artist, song_name):
    search_urls = {}
    for key in queries:
        print(queries[key])
        search_urls[key] = get_urls(queries[key])
    return search_urls

def __get_page_data(queries, artist, song_name):
    page_data = {}
    original_urls, transliteration_urls, translation_urls = get_urls(queries["original_rom_lyrics"], queries["original_rom_lyrics"], queries["english_lyrics"])
    page_data["original_url"], page_data["original_html"] = search_page(original_urls, artist, song_name)
    page_data["transliteration_url"], page_data["transliteration_html"] = search_page(transliteration_urls, artist, song_name)
    page_data["translation_url"], page_data["translation_html"] = search_page(translation_urls, artist, song_name)
    return page_data

def extract_lyrics(artist, song_name):
    song = Song() 

    song.artist, song.song_name = artist, song_name
    search_sites = get_source_pages(song.artist)

    queries = get_queries(song.artist, song.song_name, search_sites)
    print(queries)
    urls = __get_search_urls(queries, song.artist, song.song_name)
    print(urls)
    # page_data = __get_page_data(queries, song.artist, song.song_name)

    # song.original_url = page_data["original_url"],
    # song.transliteration_url = page_data["transliteration_url"]
    # song.translation_url = page_data["translation_url"]
    # song.original = scraper.get_original_lyrics(page_data["original_html"])
    # song.transliteration = scraper.get_romanization(page_data["transliteration_html"])
    # song.translation = scraper.get_english_lyrics(page_data["translation_html"] )
    
    # with open(output_file, 'w') as outfile:
    #     json.dump(song.toJSON(), outfile)
    
    print("Éxito~")

if __name__ == "__main__":
    extract_lyrics("akb48", "teacher teacher")

