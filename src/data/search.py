import sys
from googlesearch import search 

artist = sys.argv[1]

song_name = sys.argv[2]

output_file = sys.argv[3]

default_site = "colorcodedlyrics.com" # esto vendrá de alguna función

query = artist + " " + song_name + " " + "site:" + default_site

for i in search(query, tld="es", num=20, stop=25, pause=2): 
    print(i) 