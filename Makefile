BASE_JSON = 'data/interim/song_data.json'
TRANSLATION_TXT = 'data/processed/translation.txt'
ORIGINAL_TXT = 'data/processed/original.txt'
CONTENT_JSON = 'data/processed/editor_content.json'
FINAL_JSON = 'data/processed/final_content.json'

clean: 
	rm -f data/raw/*.json
	rm -f data/interim/*.json
	rm -f data/processed/*.txt
	rm -f data/processed/*.json

get_lyrics:
	python src/application/lyrics_extraction.py 

process_text: 
	python src/application/text_processing.py 

text_editor:
	python src/application/text_editor.py 

adapt_content:
	python src/blogger/content_adapter.py 

send_draft:
	python src/blogger/send_blogger_draft.py 
