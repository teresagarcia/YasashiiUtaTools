clean: 
	rm -f data/raw/*.json
	rm -f data/interim/*.json
	rm -f data/processed/*.txt
	rm -f data/processed/*.json

search_window:
	python src/application/search_lyrics.py
	
get_hmtl:
	python src/application/html_extraction.py 

process_text: 
	python src/application/text_processing.py 

text_editor:
	python src/application/text_editor.py 

adapt_content:
	python src/blogger/content_adapter.py 

send_draft:
	python src/blogger/send_blogger_draft.py 
