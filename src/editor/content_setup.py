import tldextract

def set_title(artist, song_name):
    title = "[Letra] " + artist + " - " + song_name
    return title

def get_language_refs(language):
    switcher = {
        'ko': {'main_lan': 'coreano', 'translit':'romanización'},
        'ja': {'main_lan': 'japonés', 'translit':'romaji'},
        'ru': {'main_lan': 'ruso', 'translit':'transliteración'},
        'uk': {'main_lan': 'ucraniano', 'translit':'transliteración'}
    }
    return switcher.get(language, "Invalid language")

def set_tags(artist, song_name, language_refs):
    song_tags = artist + ", " + song_name
    constant_tags = "español, letra"
    final_tags = song_tags + ", " + language_refs['main_lan'] + ", " + language_refs['translit'] + ", " + constant_tags
    return final_tags

def get_domain(url):
    ext = tldextract.extract(url)
    return ext.domain

def set_credits(original_url, transliteration_url, translation_url, language_refs):
    original_dom = get_domain(original_url)
    transliteration_dom = get_domain(transliteration_url)
    translation_dom = get_domain(translation_url)
    return language_refs['main_lan'] + ": " + original_url + "\n" + language_refs['translit'] + ": " + transliteration_url + "\n" + "Inglés: " + translation_url + "\nTraducción al español: Yasashii Uta"