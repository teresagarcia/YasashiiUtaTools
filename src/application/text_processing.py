import sys
sys.path.append('src') 
import json
from utils.file_utils import load_dict
import processing.text_setup as text_setup
from data.editor_content import EditorContent
from editor.content_setup import set_title, set_tags, set_credits, get_language_refs
from langdetect import detect
import jsonpickle

input_file = sys.argv[1]
translation_file = sys.argv[2]
original_rom_file = sys.argv[3]
info_file = sys.argv[4]

def save_translation_txt(translation_file, translation):
    with open(translation_file,'w') as translation_file:
        translation_file.write(translation)

def save_original_txt(original_rom_file, original_rom_text):
    with open(original_rom_file,'w') as original_rom:
        original_rom.write(original_rom_text)

def save_editor_content(song_data):
    editor_content = EditorContent()
    language_refs = get_language_refs(detect(song_data['original']))
    editor_content.title = set_title(song_data['artist'], song_data['song_name'])
    editor_content.translation = song_data['translation']
    editor_content.original = text_setup.mix_original_transliteration(song_data['original'], song_data['transliteration'])
    editor_content.tags = set_tags(song_data['artist'], song_data['song_name'], language_refs)
    editor_content.credits = set_credits(song_data['original_url'], song_data['transliteration_url'], song_data['translation_url'], language_refs)
    editor_content.video_code = ""
    return editor_content

if __name__ == '__main__':
    song_data = load_dict(input_file)
    editor_content = save_editor_content(song_data)
    with open(info_file, 'w') as outfile:
        json.dump(jsonpickle.encode(editor_content), outfile)
    print("Todo guardado")