#!/usr/bin/python2.7

# WP featured image poster
# --------------------------

from view import View
from wposter import WPoster

import shutil, glob, os, ntpath
from sys import platform

# Settings
# --------------------------------------------
IMAGE_EXTENSION = 'png'
ID_FILE = '/home/icebox/Desktop/current_id.txt'
UNUSED_FOLDER = '/home/icebox/Desktop/unused'
USED_FOLDER = '/home/icebox/Desktop/used'

# WP config
# ---------
WP_URL = 'http://localhost/wordpress/xmlrpc.php'
WP_USER = 'admin'
WP_PASSWORD = 'lolozaur'

# End settings
# --------------------------------------------

WP = None

# read current id
def read_current_id():
    if not os.path.exists(ID_FILE): return 1        # return 1 if file does not exist
    try:
        with open(ID_FILE, 'r') as f:
            return int(f.read().strip())
    except:
        View.warning('Cannot read current ID, setting it to 1')
        return 1

# increase current id
def write_current_id(id):
    with open(ID_FILE, 'w') as f:
        f.write('{}'.format(id))

# read images from folder
def read_images():
    return [x for x in glob.glob(os.path.join(UNUSED_FOLDER, '*.{}'.format(IMAGE_EXTENSION)))]

# tells if on windows
def is_win():
    return platform == 'win32'

# move image to different folder
def move_image(image):
    if not os.path.exists(USED_FOLDER):
        os.makedirs(USED_FOLDER)
    shutil.move(image, os.path.join(USED_FOLDER, ntpath.basename(image)))

# post image to WP
def post_image(current_id, image):
    View.normal('{} - {}'.format(current_id, image))

    # upload image / media
    image_id = WP.upload_image(image)
    View.normal('Image uploaded, ID: {}'.format(image_id))

    # create post
    post_id = WP.new_post(current_id, '', image_id)
    View.normal('Post published, ID: {}'.format(post_id))
    move_image(image)       # move image to used folder


# post images to WP
def post(current_id, images):
    errs = 0
    # post images
    for image in images:
        try:
            post_image(current_id, image)
            errs = 0
            current_id += 1
            write_current_id(current_id)
        except Exception, ex:
            View.error(ex)
            errs += 1
            if errs == 5:
                raise Exception('got 5 consecutive errors, stopping')

# main method
def main():
    global WP
    View.banner()
    try:
        # read images
        images = read_images()
        # check if we have any images
        if not images: raise Exception('No images in {}, stopping'.format(UNUSED_FOLDER))
        # get current id
        current_id = read_current_id()

        # print to user what's going on
        View.normal('Current ID: {}'.format(current_id))
        View.normal('Images: {}'.format(len(images)))
        raw_input('[+] Press ENTER to continue')

        # define WPoster obj (XMLRPC)
        WP = WPoster(WP_URL, WP_USER, WP_PASSWORD)
        post(current_id, images)        # start posting images
    except Exception, ex:
        View.error(ex)
    finally:
        View.new_line()
        View.normal('Finished !')
        if is_win(): raw_input()

if __name__ == "__main__":
    main()
