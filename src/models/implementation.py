import sys
sys.path.append('src') #Habrá otra forma
import data.search as search

artist = sys.argv[1]

song_name = sys.argv[2]

default_site = "colorcodedlyrics.com" # esto vendrá de alguna función

query = artist + " " + song_name + " " + "site:" + default_site

if __name__ == '__main__':
    urls = search.get_urls(query)
    search_items = {}
    for i in urls:
        print(i)
        title = search.get_title(i)
        print(title)
        search.check_title(title, artist, song_name)
