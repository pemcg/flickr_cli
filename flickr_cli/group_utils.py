# f/5.6ish

import re
import globals
import flickr_api
import get_utils
import time
from datetime import datetime



# -------------------------------------------------

def get_group_members(flickr, group_id, membertypes):

# {
#     "members": {
#         "page": 1,
#         "pages": 32,
#         "perpage": 100,
#         "total": 3134,
#         "member": [

	all_members = []
	flickr_data = flickr_api.get_group_members(flickr, group_id, membertypes)
	pages = flickr_data['members']['pages']
	for member in flickr_data['members']['member']:
		all_members.append(member)
	for page in range(2, pages):
		flickr_data = flickr_api.get_group_members(flickr, group_id, membertypes, page=page)
		for member in flickr_data['members']['member']:
			all_members.append(member)
	return all_members

# -------------------------------------------------

def get_group_photo_ids(flickr, group_id, days):
	photo_ids = []
	group_photos = flickr_api.get_group_photos(flickr, group_id, days)
	for photo in group_photos:
		photo_ids.append(photo['id'])
	return photo_ids

# -------------------------------------------------

def get_group_photos(flickr, group_id, days, interactive=False):
	print("******************************************************************************************")
	for photo in flickr_api.get_group_photos(flickr, group_id, days):
		print("")
		print(f'- Photo ID: {photo["id"]}')
		print(f'- User: {photo["ownername"]}')
		print(f'- Title: {photo["title"]}')
		print(f'- Description: {photo["description"]["_content"]}')
		print('- Tags:')
		for tag in photo["tags"].split():
			print(f'    {tag}')
		get_utils.get_camera_exif_data(flickr, photo["id"])
		if 'camera_make' in globals.exif_data and 'camera_model' in globals.exif_data:
			print("- Exif Camera: %s %s" % (globals.exif_data['camera_make'],globals.exif_data['camera_model']))
		print("******************************************************************************************")
		if interactive:
			input("Press Enter to continue...")

# -------------------------------------------------

def get_user_groups_with_admins(flickr):
	print("Getting user groups from Flickr...")
	flickr_data = flickr_api.get_pool_groups(flickr)
	for group in flickr_data['groups']['group']:
		admin_list = ""
		admins = get_group_members(flickr, group['id'], globals.GROUP_ADMIN)
		for admin in admins:
			admin_list = admin_list + f' {admin["nsid"]} ,'
		print(f'Group: {group["name"]}, id: {group["id"]}, {admin_list}')

 # -------------------------------------------------

def get_user_groups_with_admin_activity(flickr, days):
	print("Getting user groups from Flickr...")
	flickr_data = flickr_api.get_pool_groups(flickr)
	for group in flickr_data['groups']['group']:
		print(f'Group: {group["name"]}, id: {group["id"]}')
		admins = get_group_members(flickr, group['id'], globals.GROUP_ADMIN)
		for admin in admins:
			photo_count = get_utils.get_user_photo_count_for_recent_period(flickr, admin['nsid'], days)
			fave_count = get_utils.get_user_faves_count_for_recent_period(flickr, admin['nsid'], days)
			print(f'    Admin id: {admin["nsid"]}, name: {admin["username"]}, last {days} day photo count: {photo_count}, last {days} day fave count: {fave_count}')

 # -------------------------------------------------

def get_user_groups_with_no_admin_activity(flickr, days):
	print("Getting user groups with no recent admin activity from Flickr...")
	flickr_data = flickr_api.get_pool_groups(flickr)
	for group in flickr_data['groups']['group']:
		group_has_no_active_admin = True
		admins = get_group_members(flickr, group['id'], globals.GROUP_ADMIN)
		for admin in admins:
			photo_count = get_utils.get_user_photo_count_for_recent_period(flickr, admin['nsid'], days)
			fave_count = get_utils.get_user_faves_count_for_recent_period(flickr, admin['nsid'], days)
			if photo_count > 0 or fave_count > 0:
				group_has_no_active_admin = False
				break
		if group_has_no_active_admin:
			print(f'Group: {group["name"]}, id: {group["id"]}')
			for admin in admins:
				print(f' -- admin name: {admin["username"]}')

 # -------------------------------------------------

def get_group_members_with_recent_activity(flickr, group_id, days):
	member_count = 0
	active_members = 0
	print(f'Getting group members with recent activity from Flickr, starting at {datetime.now().strftime("%H:%M:%S")}...')
	members = get_group_members(flickr, group_id, globals.GROUP_MEMBER)
	for member in members:
		time.sleep(2)
		member_count += 1
		if member_count % 30 == 0:
			print(f'Processed {member_count} members, found {active_members} active members so far... {datetime.now().strftime("%H:%M:%S")}')
		photo_count = get_utils.get_user_photo_count_for_recent_period(flickr, member['nsid'], days)
		fave_count = get_utils.get_user_faves_count_for_recent_period(flickr, member['nsid'], days)
		if photo_count > 0 or fave_count > 0:
			active_members += 1 
	print(f'The group has {active_members} active members')

