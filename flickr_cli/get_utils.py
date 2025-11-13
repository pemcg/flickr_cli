# f/5.6ish

import re
from globals import Globals
import flickr_api
import json
import pprint

# -------------------------------------------------

def get_geo_coordinates_from_coord_string(coord_string):

	#  Example coordinate string from dropped pin in Apple Maps: "51.06612° N, 1.38359° W", 
	#  Target output: {'lat': 51.06612, 'lon': -1.38359}

	REGEX = "(\d{1,3}\.\d{1,6}). ([NS]), (\d{1,3}\.\d{1,6}). ([EW])"
	m = re.search(REGEX, coord_string)

	if m.group(2) == "S":
		lat = "-" + m.group(1)
	else:
		lat = m.group(1)
	if m.group(4) == "W":
		lon = "-" + m.group(3)
	else:
		lon = m.group(3)
	return {'lat': lat, 'lon': lon}

# -------------------------------------------------

def get_tags():
	for tag in Globals.tags:
		print(f'tag: {tag}')

# -------------------------------------------------

def get_photo_groups(flickr, photo_id):
	flickr_data = flickr_api.get_photo_contexts(flickr, photo_id)
	for group in flickr_data["pool"]:
		print(f'Group: {group["title"]}, id: {group["id"]}')

# -------------------------------------------------

def get_user_photo_count_for_recent_period(flickr, user_id, days):
	flickr_data = flickr_api.get_user_photo_count(flickr, user_id, days)
	return flickr_data["photos"]["total"]

# -------------------------------------------------

def get_user_faves_count_for_recent_period(flickr, user_id, days):
	flickr_data = flickr_api.get_user_faves_count(flickr, user_id, days)
	return flickr_data["photos"]["total"]

# -------------------------------------------------

def get_user_groups(flickr):
	for group, id in Globals.groups_by_name.items():
		print(f'Group: {group}, id: {id}')

# -------------------------------------------------

def get_photo_description(flickr, photo_id):
	flickr_data = flickr_api.get_photo_info(flickr, photo_id)
	return flickr_data['photo']['description']['_content']

# -------------------------------------------------

def get_photo_title(flickr, photo_id):
	flickr_data = flickr_api.get_photo_info(flickr, photo_id)
	return flickr_data['photo']['title']['_content']

# -------------------------------------------------

def get_photo_sizes(flickr, photo_id):
	flickr_data = flickr_api.get_photo_sizes(flickr, photo_id)
	for size in flickr_data['sizes']['size']:
		if size['label'] == 'Original':
			if size['width'] == size['height']:
				Globals.set_flag("is_square", True)
			return [size['width'], size['height']]

# -------------------------------------------------

def get_followers(flickr, print_output=False):
	flickr_data = flickr_api.get_followers(flickr)
	print(json.dumps(flickr_data, indent=4))

# -------------------------------------------------