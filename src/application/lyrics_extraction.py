import sys
sys.path.append('src') 
from constants import constants
from data.song import Song
import scrapers.lyrics_scraper as scraper
import json
from search.add_search_sites import get_source_pages
from search.search import get_urls, search_page
import jsonpickle

output_file = constants.BASE_INFO

def get_queries(artist, song_name, search_sites):
    queries = {}
    for key in search_sites:
        queries[key] = artist + " " + song_name + " " + "site:" + search_sites[key]
    return queries

def __get_search_urls(queries, artist, song_name):
    search_urls = {}
    for key in queries:
        search_urls[key] = get_urls(queries[key])
    return search_urls

def __get_page_data(urls, artist, song_name):
    page_data = {}
    for key in urls:
        found_url, found_html = search_page(artist, song_name, *urls[key])
        page_data[key] = {found_url : found_html}
    return page_data

def extract_lyrics(artist, song_name):
    song = Song() 

    song.artist, song.song_name = artist, song_name
    search_sites = get_source_pages(song.artist)

    queries = get_queries(song.artist, song.song_name, search_sites)
    urls = __get_search_urls(queries, song.artist, song.song_name)
    page_data = __get_page_data(urls, song.artist, song.song_name)
    print(page_data)

    song.original = page_data.get("original", "")
    song.transliteration = page_data.get("transliteration", "")
    song.translation = page_data.get("translation", "")
    
    with open(output_file, 'w') as outfile:
        json.dump(jsonpickle.encode(song), outfile)
    
    print("Éxito~")

if __name__ == "__main__":
    extract_lyrics("arashi", "jidai")

