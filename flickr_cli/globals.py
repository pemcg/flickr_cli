#!/usr/bin/env python3
# f/5.6ish   

import flickr_api
import pprint
import re

class Globals:   

	exif_data      = {}
	albums_by_name = {}
	albums_by_id   = {}
	groups_by_name = {}
	groups_by_id   = {}
	tags           = []

	flags = {
		"is_square"           : False,
		"is_digital"          : False,
		"is_monochrome"       : False,
		"is_mono_from_colour" : False,
		"is_35mm"             : False,
		"is_120"              : False,
		"is_6x9"              : False,
		"is_6x6"              : False,
		"is_6x45"             : False,
		"is_Leica"            : False,
		"is_Nikon"            : False,
		"is_NikonF"           : False,
		"is_Olympus"          : False,
		"is_Pentax"           : False,
		"is_Bronica"          : False,
		"is_Hasselblad"       : False,
		"is_TLR"              : False,
		"is_Fuji_rangefinder" : False,
		"is_pc_lens"          : False,
		"is_vintage_digital"  : False,
		"is_vintage_lens"     : True  # default to true as most lenses are vintage
	}

	GROUP_MEMBER        = 2
	GROUP_MODERATOR     = 3
	GROUP_ADMIN         = 4

    # Group ID mapping
	GROUP_IDS = {
        'hp5+': '342830@N20',
        'delta3200': '55584695@N00',
        'wearenotdeadyet': '1318947@N25'
	}

	@classmethod
	def initialize(cls, flickr, photo_id=None):
		cls.populate_albums(flickr)
		cls.populate_groups(flickr)
		if photo_id is not None:
			cls.populate_exif_data(flickr, photo_id)
			cls.populate_tags(flickr, photo_id)

	@classmethod
	def populate_groups(cls, flickr):
		print("Getting user groups from Flickr...")
		flickr_data = flickr_api.get_pool_groups(flickr)
		for group in flickr_data['groups']['group']:
			cls.groups_by_name[group['name']] = group['id']
			cls.groups_by_id[group['id']] = group['name']
		# pprint.pprint(cls.groups_by_name)

	@classmethod
	def populate_albums(cls, flickr):
		print("Getting albums from Flickr...")
		flickr_data = flickr_api.get_photosets(flickr)
		for album in flickr_data['photosets']['photoset']:
			cls.albums_by_name[album['title']['_content']] = album['id']
			cls.albums_by_id[album['id']] = album['title']['_content']
		# pprint.pprint(cls.albums_by_name)

	@classmethod
	def populate_exif_data(cls, flickr, photo_id):
		print("Getting photo exif data from Flickr...")
		flickr_data = flickr_api.get_photo_exif(flickr, photo_id)
		if flickr_data:
			for tag in flickr_data['photo']['exif']:
				if tag['tagspace'] == 'IFD0':
					match tag['label']:
						case 'Make':
							cls.exif_data['camera_make'] = tag['raw']['_content']
						case 'Model':
							cls.exif_data['camera_model'] = tag['raw']['_content']
				elif tag['tagspace'] == 'ExifIFD':
					match tag['label']:
						case 'Lens Make':
							cls.exif_data['lens_make'] = tag['raw']['_content']
						case 'Lens Model':
							cls.exif_data['lens_model'] = tag['raw']['_content']
						case 'Focal Length':
							cls.exif_data['focal_length'] = re.search('(\d{1,3})\.*\d{0,1} mm', tag['raw']['_content'])[1] + "mm"
						case 'ISO Speed':
							cls.exif_data['iso'] = tag['raw']['_content']
		# pprint.pprint(cls.exif_data)

	@classmethod
	def populate_tags(cls, flickr, photo_id):
		print("Getting photo tags from Flickr...")
		flickr_data = flickr_api.get_photo_info(flickr, photo_id)
		for tag in flickr_data['photo']['tags']['tag']:
			cls.tags.append(tag["raw"])
		# pprint.pprint(cls.tags)

	@classmethod
	def set_flag(cls, key, value):
		"""Set a flag's value"""
		cls.flags[key] = value
    
	@classmethod
	def get_flag(cls, key, default=None):
		"""Get a flag value"""
		return cls.flags.get(key, default)

