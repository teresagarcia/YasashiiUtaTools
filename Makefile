BASE_JSON = 'data/interim/song_data.json'
TRANSLATION_TXT = 'data/processed/translation.txt'
ORIGINAL_TXT = 'data/processed/original.txt'
CONTENT_JSON = 'data/processed/editor_content.json'

clean:
	rm -f data/raw/*.json
	rm -f data/interim/*.json
	rm -f data/processed/*.txt
	rm -f data/processed/*.json

get_lyrics:
	python src/application/lyrics_extraction.py $(BASE_JSON)

process_text: 
	python src/application/text_processing.py $(BASE_JSON) $(TRANSLATION_TXT) $(ORIGINAL_TXT) $(CONTENT_JSON)

text_editor:
	python src/application/text_editor.py $(TRANSLATION_TXT) $(ORIGINAL_TXT) $(CONTENT_JSON)