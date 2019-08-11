import sys
sys.path.append('src') #Habrá otra forma
import data.search as search
import data.save as save
import data.lyrics_scraper as scraper
import data.kpop_post2015 as kpop2015

song_data = save.new_json()

song_data["artist"] = sys.argv[1]

song_data["song_name"] = sys.argv[2]

def get_page(urls):
    for i in urls:
        print(i)
        tmp_html = search.get_html(i)
        title = search.get_title(tmp_html)
        print(title)
        if search.check_title(title, song_data["artist"] , song_data["song_name"] ):
            song_data["url"] = i
            html = tmp_html
            break
    return html

if __name__ == '__main__':
    queries = kpop2015.get_queries(song_data["artist"], song_data["song_name"])
    
    original_html = get_page(search.get_urls(queries["original_rom_lyrics"]))
    rom_html = get_page(search.get_urls(queries["original_rom_lyrics"]))
    english_html = get_page(search.get_urls(queries["english_lyrics"]))
    
    print("Coreano: \n",scraper.get_original_lyrics(original_html))
    print("Romanización: \n",scraper.get_romanization(rom_html))
    print("Inglés: \n",scraper.get_english_lyrics(english_html))
            
