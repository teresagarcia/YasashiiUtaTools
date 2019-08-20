import json
import sys
sys.path.append('src') 
from data.base_song import BaseSong

class SongInfo(BaseSong):
    def __init__(self):
        self.language = ""