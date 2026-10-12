# f/5.6ish

import re
import flickr_api
import get_utils
from globals import Globals

def cameras_by_film_type(flickr_client):
	all_cameras = {}
	all_lenses = {}

	camera_albums = get_utils.get_albums_in_collection(flickr_client, 'Cameras')
	for camera_album in camera_albums:
		all_cameras[camera_album['title']] = get_utils.get_photos_in_album(flickr_client, camera_album['id'])

	lens_albums = get_utils.get_albums_in_collection(flickr_client, 'Lenses')
	for lens_album in lens_albums:
		all_lenses[lens_album['title']] = get_utils.get_photos_in_album(flickr_client, lens_album['id'])

	film_albums = get_utils.get_albums_in_collection(flickr_client, 'Film Stocks')
	for film_album in film_albums:
		print(film_album['title'])
		photos_in_album = get_utils.get_photos_in_album(flickr_client, film_album['id'])
		camera_and_lens_count = {}

		for photo_id in photos_in_album:
			camera_type = ''
			lens_type = ''
			for camera in all_cameras.keys():
				if photo_id in all_cameras[camera]:
					camera_type = camera
			for lens in all_lenses.keys():
				if photo_id in all_lenses[lens]:
					lens_type = lens

			if lens_type != '':
				camera_and_lens = f"{camera_type} + {lens_type}: "
			else:
				camera_and_lens = f"{camera_type}: "
			if camera_and_lens in camera_and_lens_count:
				camera_and_lens_count[camera_and_lens] += 1
			else:
				camera_and_lens_count[camera_and_lens] = 1
		for camera_and_lens in sorted(camera_and_lens_count, key=camera_and_lens_count.get, reverse=True):
			print (camera_and_lens, camera_and_lens_count[camera_and_lens])
		print()

