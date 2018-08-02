from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media
from wordpress_xmlrpc import WordPressPost
import ntpath

class WPoster:
    def __init__(self, url, user, password):
        self._wp = Client(url, user, password)

    # upload image / media
    def upload_image(self, image_path):

        # prepare metadata
        data = {
            'name': ntpath.basename(image_path),
            'type': 'image/jpeg',  # mimetype
        }

        # read the binary file and let the XMLRPC library encode it into base64
        with open(image_path, 'rb') as img:
            data['bits'] = xmlrpc_client.Binary(img.read())

        response = self._wp.call(media.UploadFile(data))
        # response == {
        #       'id': 6,
        #       'file': 'picture.jpg'
        #       'url': 'http://www.example.com/wp-content/uploads/2012/04/16/picture.jpg',
        #       'type': 'image/jpeg',
        # }
        attachment_id = response['id']
        return attachment_id

    # new post (with feautured image)
    def new_post(self, title, content, image_id):
        post = WordPressPost()
        post.title = title
        post.content = content
        post.thumbnail = image_id
        post.post_status = 'publish'
        post.id = self._wp.call(NewPost(post))
        return post.id

    # get posts (testing)
    def get_posts(self):
        return self._wp.call(GetPosts())
