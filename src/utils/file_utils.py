import json

def load_dict(input_file):
    with open(input_file) as json_file:
        data = json.load(json_file)
    dict_data = json.loads(data)
    return dict_data

def load_txt(input_file):
    with open(input_file, 'r') as txt_file:
        txt_data = txt_file.read()
    return txt_data
