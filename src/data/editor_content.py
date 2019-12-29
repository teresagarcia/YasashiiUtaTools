import json

class EditorContent(object):
    def __init__(self):
        self.title = ""
        self.translation = ""
        self.original = ""
        self.video_code = ""
        self.tags = ""
        self.credits = ""

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)