def get_queries(artist, song_name):
    queries = {}
    queries["original_rom_lyrics"] = artist + " " + song_name + " " + "site:ilyricsbuzz.com"
    queries["english_lyrics"] = artist + " " + song_name + " " + "site:popgasa.com"
    return queries

