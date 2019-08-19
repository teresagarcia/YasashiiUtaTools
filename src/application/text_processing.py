import sys
sys.path.append('src') 
import json

input_file = sys.argv[1]
translation_file = sys.argv[2]
original_rom_file = sys.argv[3]

if __name__ == '__main__':
    with open(input_file) as json_file:
        data = json.load(json_file)
    song_data = json.loads(data)
    print(song_data['translation'])
    with open(translation_file,'w') as translation:
        translation.write(song_data['translation'])
    print("Guardado txt traducción")