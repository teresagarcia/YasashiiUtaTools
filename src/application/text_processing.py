import sys
sys.path.append('src') 
import json
import processing.text_setup as text_setup

input_file = sys.argv[1]
translation_file = sys.argv[2]
original_rom_file = sys.argv[3]

def load_song_data(input_file):
    with open(input_file) as json_file:
        data = json.load(json_file)
    song_data = json.loads(data)
    return song_data

def save_translation_txt(translation_file, translation):
    with open(translation_file,'w') as translation_file:
        translation_file.write(translation)
    print("Guardado txt traducción")

def save_original_txt(original_rom_file, original_rom_text):
    with open(original_rom_file,'w') as original_rom:
        original_rom.write(original_rom_text)
    print("Guardado txt original + transliteración")

if __name__ == '__main__':
    song_data = load_song_data(input_file)
    save_translation_txt(translation_file, song_data['translation'])
    original_rom_text = text_setup.mix_original_transliteration(song_data['original'], song_data['transliteration'])
    save_original_txt(original_rom_file, original_rom_text)
    