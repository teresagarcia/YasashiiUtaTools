from __future__ import print_function

import sys
sys.path.append('src') 
import utils.file_utils as utils
from oauth2client import client
from googleapiclient import sample_tools
import jsonpickle
from constants import constants

other_data_file = constants.OTHER_DATA

def send_draft(post_file , argv="") :
    # Authenticate and construct service.
    service, flags = sample_tools.init(
        argv, 'blogger', 'v3', __doc__, __file__,
        scope="https://www.googleapis.com/auth/blogger")

    other_data = utils.load_json(other_data_file)
    post_json = utils.load_json(post_file)
    post_content = jsonpickle.decode(post_json)

    try:
        blogs = service.blogs()

        # Retrieve the list of Blogs this user has write privileges on
        thisusersblogs = blogs.listByUser(userId='self').execute()

        posts = service.posts()
        body = {
        "kind": "blogger#post",
        "title": post_content.title,
        "content": post_content.content,
        "labels": post_content.labels,
        }
        blog = thisusersblogs['items'][0]
        if blog['id'] == other_data['blog_id']:
            posts.insert(blogId=blog['id'], body=body, isDraft=True).execute()
            print("Borrador enviado")

    except client.AccessTokenRefreshError:
        print ('The credentials have been revoked or expired, please re-run'
               'the application to re-authorize')