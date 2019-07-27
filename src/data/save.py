import json


def new_json():
    data =  '{"artist": "", "song_name": "", "url": "", "html": "", "original": "", \
    "transliteration": "", "translation": ""}'
    songs_data = json.loads(data)
    return songs_data
