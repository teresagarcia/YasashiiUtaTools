import sys
sys.path.append('src') 
import utils.file_utils as utils
import jsonpickle
import json
from data.final_content import FinalContent

def get_post_labels(tags):
    return tags.split(", ")

def get_post_content(video_code, original, post_credits):
    post_content = video_code + "<br/><br/>" + original + "<br/><br/>" + "Créditos:<br/>" + post_credits
    post_content = post_content.replace("\n", "<br/>")
    return post_content

def adapt_final_content(content):
    final_content = FinalContent()
    final_content.title = content.title
    final_content.content = get_post_content(content.video_code, content.original, content.credits)
    final_content.labels = get_post_labels(content.tags)
    return final_content

def get_final_content(editor_content, result_file):
    info = utils.load_json(editor_content)
    content = jsonpickle.decode(info)
    
    final_content = adapt_final_content(content)

    with open(result_file, 'w') as outfile:
        json.dump(jsonpickle.encode(final_content), outfile)

