SEARCH_URL = 'data/raw/urls_list.csv'

clean:
	rm -f data/raw/*.csv
	rm -f data/interim/*.json
	rm -f data/processed/*.tsv

search:
	python src/data/search.py $(artist) $(song_name) $(SEARCH_URL)