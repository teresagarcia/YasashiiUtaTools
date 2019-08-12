BASE_JSON = 'data/interim/song_data.json'
TRANSLATION_TXT = 'data/processed/translation.txt'
ORIGINAL_TXT = 'data/processed/original.txt'

clean:
	rm -f data/raw/*.json
	rm -f data/interim/*.json
	rm -f data/processed/*.txt
	rm -f data/processed/*.json

get_lyrics:
	python src/application/lyrics_extraction.py $(artist) $(song_name) $(BASE_JSON)

process_text: 
	python src/application/text_processing.py $(BASE_JSON)