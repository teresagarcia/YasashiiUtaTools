def set_title(artist, song_name):
    title = "[Letra] " + artist + " - " + song_name
    return title

def get_language_tags(language):
    switcher = {
        'ko': "coreano, romanización",
        'ja': "japonés, romaji",
        'hi': "hindi",
        'ru': "ruso, transliteración",
        'uk': "ucraniano, transliteración"
    }
    return switcher.get(language, "Invalid language")

def set_tags(artist, song_name, language):
    song_tags = artist + ", " + song_name
    language_tags = get_language_tags(language)
    constant_tags = "español, letra"
    final_tags = song_tags + ", " + language_tags + ", " + constant_tags
    return final_tags

def set_credits(original_url, transliteration_url, translation_url):
    return original_url + "\n" + transliteration_url + "\n" + translation_url