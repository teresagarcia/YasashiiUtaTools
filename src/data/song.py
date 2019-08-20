import json
import sys
sys.path.append('src') 
from data.base_song import BaseSong

class Song(BaseSong):
    def __init__(self):
        self.original = ""
        self.transliteration = ""
        self.translation = ""