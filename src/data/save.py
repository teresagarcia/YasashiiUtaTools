import json


def new_json():
    data =  '{"artist": "", "song_name": "", "original_url": "", "transliteration_url": "","translation_url": "", "original": "", \
    "transliteration": "", "translation": ""}'
    songs_data = json.loads(data)
    return songs_data
