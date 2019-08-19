import itertools

def split_text(original, transliteration):
    original_split = original.splitlines(True)
    transliteration_split = transliteration.splitlines(True)
    return original_split, transliteration_split

def transliteration_to_uppercase(transliteration_split):
    corrected_transliteration_split = []
    for line in transliteration_split:
        corrected_transliteration_split.append(line.capitalize())
    return corrected_transliteration_split

def mix_text(original_split, transliteration_split):
    mixed_text = ""
    for original_line, transliteration_line in itertools.zip_longest(original_split, transliteration_split):
        mixed_text += original_line + transliteration_line + "\n"
    return mixed_text

def mix_original_transliteration(original, transliteration):
    original_split, transliteration_split = split_text(original, transliteration)
    corrected_transliteration_split = transliteration_to_uppercase(transliteration_split)
    mixed_text = mix_text(original_split, corrected_transliteration_split)
    return mixed_text