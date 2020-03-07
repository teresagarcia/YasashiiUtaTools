import sys
sys.path.append('src') 
from utils.text_utils import clean_text


artists_source = {
    "arashi":{"original": "yarukizero.livejournal.com",
            "transliteration": "yarukizero.livejournal.com",
            "translation": "yarukizero.livejournal.com"},
    "kpop":{"original": "melon.com/song",
            "translation": "popgasa.com"},
    "bollywood":{"original": "bollynook.com",
            "translation": "bollynook.com"},
    "family48":{"original": "stage48.net/studio48/",
            "transliteration": "stage48.net/studio48/",
            "translation": "stage48.net/studio48/"},
}


artists_names = {
    "arashi": ["Arashi"],
    "bollywood": ["Armaan Malik", "Arijit Singh", "Falak Shabir"],
    "family48": ["AKB48", "SDN48"]
}


def get_category(artist):
    category = "kpop"
    for key in artists_names:
        if clean_text(artist)[0] in clean_text(*artists_names[key]):
            category = key
    return category


def get_source_pages(artist):
    category = get_category(artist)
    return artists_source[category]


if __name__ == "__main__":
    print(get_source_pages("beast"))