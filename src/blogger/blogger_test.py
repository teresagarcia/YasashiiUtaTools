from __future__ import print_function

import sys

from oauth2client import client
from googleapiclient import sample_tools

def main(argv):
    # Authenticate and construct service.
    service, flags = sample_tools.init(
        argv, 'blogger', 'v3', __doc__, __file__,
        scope="https://www.googleapis.com/auth/blogger")

    try:
        users = service.users()

        # Retrieve this user's profile information
        thisuser = users.get(userId='self').execute()

        blogs = service.blogs()

        # Retrieve the list of Blogs this user has write privileges on
        thisusersblogs = blogs.listByUser(userId='self').execute()

        posts = service.posts()
        body = {
        "kind": "blogger#post",
        "id": "6814573853229626501",
        "title": "[Letra] PewDiePie - Hej Monika",
        "content":"Hej hej Monika"
        }
        blog = thisusersblogs['items'][0]
        if blog['id'] == '1234':
            posts.insert(blogId=blog['id'], body=body, isDraft=True).execute()

    except client.AccessTokenRefreshError:
        print ('The credentials have been revoked or expired, please re-run'
               'the application to re-authorize')

if __name__ == '__main__':
    main(sys.argv)