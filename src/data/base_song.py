import json

class BaseSong(object):
    def __init__(self):
        self.artist = ""
        self.song_name = ""
        self.original_url = ""
        self.transliteration_url = ""
        self.translation_url = ""

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)