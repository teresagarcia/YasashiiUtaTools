import json

class Song(object):
    def __init__(self):
        self.artist = ""
        self.song_name = ""
        self.original_url = ""
        self.transliteration_url = ""
        self.translation_url = ""
        self.original = ""
        self.transliteration = ""
        self.translation = ""


# def new_json():
#     data =  '{"artist": "", "song_name": "", "original_url": "", "transliteration_url": "","translation_url": "", "original": "", \
#     "transliteration": "", "translation": ""}'
#     songs_data = json.loads(data)
#     return songs_data
