import sys
sys.path.append('src') #Habrá otra forma
import data.search as search
import data.save as save
import data.lyrics_scraper as scraper

song_data = save.new_json()

song_data["artist"] = sys.argv[1]

song_data["song_name"] = sys.argv[2]

default_site = "popgasa.com" # esto vendrá de alguna función

query = song_data["artist"] + " " + song_data["song_name"] + " " + "site:" + default_site

if __name__ == '__main__':
    urls = search.get_urls(query)
    search_items = {}
    for i in urls:
        print(i)
        tmp_html = search.get_html(i)
        title = search.get_title(tmp_html)
        print(title)
        if search.check_title(title, song_data["artist"], song_data["song_name"]):
            song_data["url"] = i
            song_data["html"] = tmp_html
            break
    print(scraper.get_english_lyrics(song_data["html"]))
            
