# f/5.6ish

import flickrapi
import inspect
import sys
import os.path
import logging
from globals import Globals
import keys
import add_utils
import xml.etree.ElementTree as ET
import time
import requests
from requests_oauthlib import OAuth1
from datetime import datetime, timedelta
from tenacity import retry


GEO_ACCURACY_WORLD   = 1
GEO_ACCURACY_COUNTRY = 3
GEO_ACCURACY_REGION  = 6
GEO_ACCURACY_CITY    = 9
GEO_ACCURACY_STREET  = 16
GEO_CONTEXT_INDOORS  = 1
GEO_CONTEXT_OUTDOORS = 2

# ------------------ Flickr API Methods ------------------
# --------------------------------------------------------

def authenticate():
    try:
        flickr = flickrapi.FlickrAPI(keys.FLICKR_API_KEY, keys.FLICKR_API_SECRET, store_token=True, format='parsed-json')
        flickr.authenticate_via_browser(perms='write')
        # verify = str(input('Press Enter to continue:> '))
        flickr.get_access_token("")
        login = flickr.test.login()
        print(f'You are now authenticated as {login["user"]["username"]["_content"]}')
        return flickr
    except flickrapi.exceptions.FlickrError as ex:
        print_error(ex)
        sys.exit()

# -------------------- Groups --------------------

def get_group_info(flickr, group_id):
    try:
        flickr_return = flickr.groups.getInfo(group_id=group_id)
        return flickr_return
    except flickrapi.exceptions.FlickrError as ex:
        print_error(ex)

def get_group_members(flickr, group_id, membertypes, page=1):
    try:
        flickr_return = flickr.groups.members.getList(group_id=group_id, membertypes=membertypes, page=page)
        return flickr_return
    except flickrapi.exceptions.FlickrError as ex:
        print_error(ex)

def add_photo_to_group(flickr, photo_id, group_id):
    try:
        print(f'Adding photo to group: {Globals.groups_by_id[group_id]}...')
        flickr.groups.pools.add(photo_id=photo_id, group_id=group_id)
    except flickrapi.exceptions.FlickrError as ex:
        print_error(ex)

def get_pool_groups(flickr):
    try:
        flickr_return = flickr.groups.pools.getGroups()
        return flickr_return
    except flickrapi.exceptions.FlickrError as ex:
        print_error(ex)

def get_group_photos(flickr, group_id, days):
    group_photos = []
    now = datetime.now()
    requested_date = int(time.mktime(now.timetuple())) - (int(days) * 24 * 60 * 60)
    try:
        flickr_return = flickr.groups.pools.getPhotos(group_id=group_id, extras="description,tags")
        for photo in flickr_return['photos']['photo']:
            if int(photo['dateadded']) > requested_date:
                group_photos.append(photo)
        return group_photos
    except flickrapi.exceptions.FlickrError as ex:
        print_error(ex)

# -------------------- Photos --------------------

def add_tag_to_photo(flickr, photo_id, tag):
    try:
        printable_tag = tag.strip('"')
        print(f'Adding tag "{printable_tag}"...')
        flickr.photos.addTags(photo_id=photo_id, tags=tag)
    except flickrapi.exceptions.FlickrError as ex:
        print_error(ex)

def get_photo_contexts(flickr, photo_id):
    try:
        flickr_return = flickr.photos.getAllContexts(photo_id=photo_id)
        return flickr_return
    except flickrapi.exceptions.FlickrError as ex:
        print_error(ex)

def get_photo_info(flickr, photo_id):
    try:
        flickr_return = flickr.photos.getInfo(photo_id=photo_id)
        return flickr_return
    except flickrapi.exceptions.FlickrError as ex:
        print_error(ex)

def get_photo_exif(flickr, photo_id):
    try:
        flickr_return = flickr.photos.getExif(photo_id=photo_id)
        return flickr_return
    except flickrapi.exceptions.FlickrError as ex:
        print_error(ex)

def get_photo_sizes(flickr, photo_id):
    try:
        flickr_return = flickr.photos.getSizes(photo_id=photo_id)
        return flickr_return
    except flickrapi.exceptions.FlickrError as ex:
        print_error(ex)

def set_photo_location(flickr, photo_id, lat, lon, accuracy, context):
    try:
        print(f'Setting location...')
        flickr.photos.geo.setLocation(photo_id=photo_id, lat=lat, lon=lon, accuracy=accuracy, context=context)
    except flickrapi.exceptions.FlickrError as ex:
        print_error(ex)

# -------------------- Photosets --------------------

def add_photo_to_photoset(flickr, photo_id, photoset_id):
    try:
        print(f'Adding photo to album: {Globals.albums_by_id[photoset_id]}...')
        flickr.photosets.addPhoto(photo_id=photo_id, photoset_id=photoset_id)
    except flickrapi.exceptions.FlickrError as ex:
        print_error(ex)

def get_photosets(flickr):
    try:
        flickr_return = flickr.photosets.getList()
        return flickr_return
    except flickrapi.exceptions.FlickrError as ex:
        print_error(ex)

# -------------------- Activity --------------------

def get_follower_notifications(flickr, page=1):
    try:
        flickr_return = flickr.activity.recentByType(notification_groups="followers", per_page=50, page=page)
        return flickr_return
    except flickrapi.exceptions.FlickrError as ex:
        print_error(ex)

# -------------------- People --------------------

@retry
def get_user_photo_count(flickr, user_id, days_ago):
    now = datetime.now()
    requested_date = int(time.mktime(now.timetuple())) - (int(days_ago) * 24 * 60 * 60)    
    try:
        flickr_return = flickr.people.getPhotos(user_id=user_id, min_taken_date=requested_date, per_page=1, page=1)
        return flickr_return
    except flickrapi.exceptions.FlickrError as ex:
        print_error(ex)

# -------------------- Contacts --------------------

def get_contacts(flickr, page=1):
    try:
        flickr_return = flickr.contacts.getList(per_page=50, page=page)
        return flickr_return
    except flickrapi.exceptions.FlickrError as ex:
        print_error(ex)


def get_followers(flickr):
    url = "https://www.flickr.com/people/me/contacts/rev"

    headers = {
        'User-Agent': 'Mozilla/5.0',
        # You might need to add 'Cookie' or 'Authorization' headers if required
    }

    request_token = flickr.token_cache.token
    oauth_token = request_token.token
    oauth_token_secret = request_token.token_secret

    client = OAuth1Session(keys.FLICKR_API_KEY, keys.FLICKR_API_SECRET, token=oauth_token, token_secret=oauth_token_secret)

    response = client.get(url, headers=headers)


    if response.status_code == 200:
        try:
            print(response)
            data = response.json()
            print("JSON response:", data)
        except ValueError:
            print("Response is not valid JSON")
    else:
        print(f"Request failed with status code {response.status_code}")
        print(response.text)


# -------------------- Favourites --------------------

@retry
def get_user_faves_count(flickr, user_id, days_ago):
    now = datetime.now()
    requested_date = int(time.mktime(now.timetuple())) - (int(days_ago) * 24 * 60 * 60)
    try:
        flickr_return = flickr.favorites.getList(user_id=user_id, min_fave_date=requested_date, per_page=1, page=1)
        return flickr_return
    except flickrapi.exceptions.FlickrError as ex:
        print_error(ex)

# -------------------- Upload --------------------

def upload(flickr, filename, title, description):
    fileobj = FileWithCallback(filename, add_utils.callback)
    try:
        rsp = flickr.upload(filename=filename, title=title, description=description, format='etree', fileobj=fileobj)
        if rsp.get('stat') == "ok":
            return rsp[0].text
    except flickrapi.exceptions.FlickrError as ex:
        print_error(ex)

# -------------------- Error handling --------------------

def print_error(ex):
    caller = inspect.stack()[1][3]
    if (caller == "get_photo_exif") & (ex.code == '2'):
        return
    if ex.code == '500':
        print(f'FlickrError (in {caller}):', ex.code)
    else:
        print(f'FlickrError (in {caller}):', ex)

def enable_debug_logging():
    flickrapi.set_log_level(logging.DEBUG)

# ---------------- End of Flickr API Methods -------------
# --------------------------------------------------------



class FileWithCallback(object):
    def __init__(self, filename, callback):
        self.file = open(filename, 'rb')
        self.callback = callback
        # the following attributes and methods are required
        self.len = os.path.getsize(filename)
        self.fileno = self.file.fileno
        self.tell = self.file.tell

    def read(self, size):
        if self.callback:
            self.callback(self.tell() * 100 // self.len)
        return self.file.read(size)

# --------------------------------------------------