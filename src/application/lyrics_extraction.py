import sys
sys.path.append('src') 
import data.search as search
from data.song import Song
import data.lyrics_scraper as scraper
import data.kpop_post2015 as kpop2015
import json

song = Song()

song.artist = sys.argv[1]

song.song_name = sys.argv[2]

output_file = sys.argv[3]

def get_page(urls):
    for i in urls:
        tmp_html = search.get_html(i)
        title = search.get_title(tmp_html)
        if search.check_title(title, song.artist, song.song_name ):
            url = i 
            html = tmp_html
            break
    return html, url

if __name__ == '__main__':
    queries = kpop2015.get_queries(song.artist, song.song_name)
    
    original_html, song.original_url = get_page(search.get_urls(queries["original_rom_lyrics"]))
    rom_html, song.transliteration_url = get_page(search.get_urls(queries["original_rom_lyrics"]))
    english_html, song.translation_url = get_page(search.get_urls(queries["english_lyrics"]))
    
    song.original = scraper.get_original_lyrics(original_html)
    song.transliteration = scraper.get_romanization(rom_html)
    song.translation = scraper.get_english_lyrics(english_html)
    with open(output_file, 'w') as outfile:
        json.dump(song.toJSON(), outfile)
    print("Éxito~")