import sys
sys.path.append('src') 
from utils.text_utils import clean_text

artist = "Arashi"
song_name = "Jidai"

artists_source = {
    "arashi":{"original": "yarukizero.livejournal.com",
            "transliteration": "yarukizero.livejournal.com",
            "translation": "yarukizero.livejournal.com"},
    "kpop":{"original": "melon.com",
            "transliteration": "colorcodedlyrics.com",
            "translation": "popgasa.com"},
    "bollywood":{"original": "bollynook.com",
            "translation": "bollynook.com"}
}


artists_names = {
    "arashi": ["Arashi"],
    "bollywood": ["Armaan Malik", "Arijit Singh", "Falak Shabir"],
}

def get_category(artist):
    category = "kpop"
    for key in artists_names:
        print(key)
        print(clean_text(artist))
        print(clean_text(artists_names[key]))
        if clean_text(artist) in clean_text(artists_names[key]):
            category = key
    return category


def mystery_fun(artist, song_name):
    print(get_category(artist))

if __name__ == "__main__":
    mystery_fun(artist, song_name)