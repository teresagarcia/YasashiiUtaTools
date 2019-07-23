import sys
sys.path.append('src') #Habrá otra forma
import data.search as search

artist = sys.argv[1]

song_name = sys.argv[2]

default_site = "colorcodedlyrics.com" # esto vendrá de alguna función

query = artist + " " + song_name + " " + "site:" + default_site

if __name__ == '__main__':
    result = search.get_urls(query)
    for i in result:
        print(i)
        print(search.check_title(i))