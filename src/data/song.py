import json
import sys
sys.path.append('src') 
from data.base_song import BaseSong

class Song(BaseSong):
    def __init__(self):
        self.original_url = ""
        self.transliteration_url = ""
        self.translation_url = ""
        self.original = ""
        self.transliteration = ""
        self.translation = ""