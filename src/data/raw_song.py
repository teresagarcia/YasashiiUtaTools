import sys
sys.path.append('src') 
from data.base_song import BaseSong

class RawSong(BaseSong):
    def __init__(self):
        self.original_html = ""
        self.transliteration_html = ""
        self.translation_html = ""
        

    