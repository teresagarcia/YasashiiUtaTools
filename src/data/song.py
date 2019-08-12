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


    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)