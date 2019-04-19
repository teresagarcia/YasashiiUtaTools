SEARCH_URL = 'data/raw/tweets.csv'

clean:
	rm -f data/raw/*.csv
	rm -f data/interim/*.json
	rm -f data/processed/*.tsv

search:
	python src/data/search_keyword.py $(word) $(SEARCH_URL)