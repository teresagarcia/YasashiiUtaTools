import sys
sys.path.append('src') 
import json
import processing.text_setup as text_setup
from data.song_info import SongInfo
from langdetect import detect

input_file = sys.argv[1]
translation_file = sys.argv[2]
original_rom_file = sys.argv[3]
info_file = sys.argv[4]

def load_song_data(input_file):
    with open(input_file) as json_file:
        data = json.load(json_file)
    song_data = json.loads(data)
    return song_data

def save_translation_txt(translation_file, translation):
    with open(translation_file,'w') as translation_file:
        translation_file.write(translation)

def save_original_txt(original_rom_file, original_rom_text):
    with open(original_rom_file,'w') as original_rom:
        original_rom.write(original_rom_text)

def save_song_info(song_data):
    song_info = SongInfo()
    song_info.artist = song_data['artist']
    song_info.song_name = song_data['song_name']
    song_info.original_url = song_data['original_url']
    song_info.transliteration_url = song_data['transliteration_url']
    song_info.translation_url = song_data['translation_url']
    song_info.language = detect(song_data['original'])
    return song_info

if __name__ == '__main__':
    song_data = load_song_data(input_file)
    save_translation_txt(translation_file, song_data['translation'])
    original_rom_text = text_setup.mix_original_transliteration(song_data['original'], song_data['transliteration'])
    save_original_txt(original_rom_file, original_rom_text)
    song_info = save_song_info(song_data)
    with open(info_file, 'w') as outfile:
        json.dump(song_info.toJSON(), outfile)
    print("Todo guardado")