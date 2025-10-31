# f/5.6ish

import re
import globals
import flickr_api
import json

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

def get_tags(flickr, photo_id, print_output=False):
	flickr_data = flickr_api.get_photo_info(flickr, photo_id)
	if print_output:
		for tag in flickr_data['photo']['tags']['tag']:
			print(f'tag: {tag["raw"]}')
	return flickr_data['photo']['tags']['tag']

# -------------------------------------------------

def get_albums(flickr):
	print("Getting albums from Flickr...")
	flickr_data = flickr_api.get_photosets(flickr)
	for album in flickr_data['photosets']['photoset']:
		globals.albums[album['title']['_content']] = album['id']
		globals.albums[album['id']] = album['title']['_content']

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

def get_camera_exif_data(flickr, photo_id):
	globals.exif_data = {}
	flickr_data = flickr_api.get_photo_exif(flickr, photo_id)
	if flickr_data:
		for tag in flickr_data['photo']['exif']:
			if tag['tagspace'] == 'IFD0':
				match tag['label']:
					case 'Make':
						globals.exif_data['camera_make'] = tag['raw']['_content']
					case 'Model':
						globals.exif_data['camera_model'] = tag['raw']['_content']
			elif tag['tagspace'] == 'ExifIFD':
				match tag['label']:
					case 'Lens Make':
						globals.exif_data['lens_make'] = tag['raw']['_content']
					case 'Lens Model':
						globals.exif_data['lens_model'] = tag['raw']['_content']
					case 'Focal Length':
						globals.exif_data['focal_length'] = re.search('(\d{1,3})\.*\d{0,1} mm', tag['raw']['_content'])[1] + "mm"

# -------------------------------------------------

def get_user_groups(flickr, print_output=False):
	print("Getting user groups from Flickr...")
	flickr_data = flickr_api.get_pool_groups(flickr)
	for group in flickr_data['groups']['group']:
		globals.groups[group['name']] = group['id']
		globals.groups[group['id']]   = group['name']
		if print_output:
			print(f'Group: {group["name"]}, id: {group["id"]}')

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
				globals.is_square = True
			return [size['width'], size['height']]

# -------------------------------------------------

def get_followers(flickr, print_output=False):
	flickr_data = flickr_api.get_followers(flickr)
	print(json.dumps(flickr_data, indent=4))

# -------------------------------------------------