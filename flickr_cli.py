#!/usr/bin/env python3
# f/5.6ish

import argparse
import sys
import logging
sys.path.append('./flickr_cli')
import flickr_api
import get_utils
import add_utils
import group_utils
import globals

#-------------------------------------------------------------------------------------------------------------
def sanity_check_args(parser, args):
    #
    # No serverlist specified?
    #
    if args.add and not args.id:
        parser.error("Must specify the --id switch when using --add")
        return False
    #
    # -c & --copyfrom together?
    #
    if args.get_tags and not args.id:
        parser.error("Must specify the --id switch when using --get_tags")
        return False
    #
    # --copysrc without --copydest (or vice-versa)
    #
    # if (args.FilenameTo and not args.FileCopyDest) or\
    #     (args.FileCopyDest and not args.FilenameTo):
    #     parser.error("args --copysrc and --copydest must be used together")
    #     return False
    # #
    # # -f with --copysrc or --copydest (or vice-versa)
    # #
    # if (args.FilenameFrom and (args.FilenameTo or args.FileCopyDest)):
    #     parser.error("option --copyfrom with --copysrc and/or --copydest cannot be used together")
    #     return False
    # #
    # # -c with --copysrc or --copydest (or vice-versa)
    # #
    # if (args.Command and (args.FilenameTo or args.FileCopyDest)):
    #     parser.error("option -c with --copysrc and/or --copydest cannot be used together")
    #     return False
    # #
    # # -q with anything else
    # #
    # if (args.Query and (args.FilenameTo or args.FileCopyDest or args.Command)):
    #     parser.error("option -q with the copy commands and/or -c cannot be used together")
    #     return False
    # #
    # # --nowait without -c
    # #
    # if (args.NoWait and not args.Command):
    #     parser.error("option --nowait can only be used with the -c switch")
    #     return False
    #
    # Default
    #
    return True
#
# End of SanityCheckOptions
#-------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Add a photo to Flickr globals.groups.')
    parser.add_argument('--id', help='The ID of the photo or group to process', required=False)
    parser.add_argument('--get_groups', help='Get group list for photo or user', action='store_true')
    parser.add_argument('--get_group_admins', help='More details', action='store_true')
    parser.add_argument('--get_user_groups_with_admins', help='More details', action='store_true')
    parser.add_argument('--get_user_groups_with_admin_activity', help='More details', action='store_true')
    parser.add_argument('--get_user_groups_with_no_admin_activity', help='More details', action='store_true')
    parser.add_argument('--get_group_members_with_recent_activity', help='More details', action='store_true')
    parser.add_argument('--get_group_photos', help='Get groups photos', action='store_true')
    parser.add_argument('--group', help='Group name to operate on, "hp5+" or "delta3200"')
    parser.add_argument('--days', help='Days to get groups photos')
    parser.add_argument('--interactive', help='Promt for return to continue on long listings', action='store_true')
    parser.add_argument('--get_tags', help='Get tag list for photo', action='store_true')
    parser.add_argument('--add', help='Add photo to Flickr groups & albums, and add tags', action='store_true')
    parser.add_argument('--upload', help='Upload a photo to Flickr', action='store_true')
    parser.add_argument('--filename', help='The filename of the photo to upload to Flickr')
    parser.add_argument('--title', help='The title of the photo to upload to Flickr')
    parser.add_argument('--description', help='The description of the photo to upload to Flickr')
    parser.add_argument('--location', help='The name of the location where photo was taken (e.g. "Winchester")', required=False)
    parser.add_argument('--coords', help='The Apple Maps dropped pin string coordinates of location where photo was taken', required=False)
    parser.add_argument('--get_followers', help='Get a list of followers', action='store_true')
    parser.add_argument('--digital', help='Use to indicate that this is a digital image', action='store_true')
    parser.add_argument('--monochrome', help='Use to indicate that this is a monochrome image', action='store_true')
    args = parser.parse_args()

    #
    # Sanity check arguments and their combinations
    #
    if not sanity_check_args(parser, args):
        parser.print_help()
        sys.exit()
    #
    # set some global variables based on command line arguments
    #
    if args.digital:
        globals.is_digital = True
    if args.monochrome:
        globals.is_monochrome = True

    # logging.basicConfig(filename='flickr_cli.log', filemode='w', level=logging.DEBUG)
    # flickr_api.enable_debug_logging()

    flickr_client = flickr_api.authenticate()
    #
    # Photo-related arguments
    #
    if args.add:
        add_utils.add_groups_and_tags(flickr_client, args.id)
        if args.location:
            add_utils.add_geo_data_by_location(flickr_client, args.id, args.location)
        if args.coords:
            add_utils.add_geo_data_by_coords(flickr_client, args.id, args.coords)
    # elif args.get_groups:
    #     get_utils.get_photo_groups(flickr_client, args.id)
    elif args.get_tags:
        get_utils.get_tags(flickr_client, args.id, print_output=True)
    #
    # Location-related arguments
    #
    if not args.add:
        if args.location:
            add_utils.add_geo_data_by_location(flickr_client, args.id, args.location)
        if args.coords:
            add_utils.add_geo_data_by_coords(flickr_client, args.id, args.coords)
    #
    # Group-related arguments
    #
    if args.get_groups:
        get_utils.get_user_groups(flickr_client, print_output=True)
    elif args.get_group_admins:
        group_utils.get_group_admins(flickr_client)
    elif args.get_user_groups_with_admins:
        group_utils.get_user_groups_with_admins(flickr_client)
    elif args.get_user_groups_with_admin_activity:
        group_utils.get_user_groups_with_admin_activity(flickr_client, int(args.days))
    elif args.get_user_groups_with_no_admin_activity:
        group_utils.get_user_groups_with_no_admin_activity(flickr_client, int(args.days))
    elif args.get_group_photos:
        match args.group:
            case 'hp5+':
                group_id = '    '
            case 'delta3200':
                group_id = '55584695@N00'
            case 'wearenotdeadyet':
                group_id = '1318947@N25'
            case _:
                print("Need the group name for the get_group_photos argument")
                exit()
        group_utils.get_group_photos(flickr_client, group_id, int(args.days), args.interactive)
    elif args.get_group_members_with_recent_activity:
        match args.group:
            case 'hp5+':
                group_id = '342830@N20'
            case 'delta3200':
                group_id = '55584695@N00'
            case 'wearenotdeadyet':
                group_id = '1318947@N25'
            case _:
                print("Need the group name for the get_group_members_with_recent_activity argument")
                exit()
        group_utils.get_group_members_with_recent_activity(flickr_client, group_id, int(args.days))
    #
    # Upload-related arguments
    #
    if args.upload:
        new_photo_id = flickr_api.upload(flickr_client, args.filename, args.title, args.description)
        print("New photo id: %s" % new_photo_id)
        # utils.add_groups_and_tags(flickr_client, new_photo_id)
    #
    # Followers-related arguments
    #
    if args.get_followers:
        get_utils.get_followers(flickr_client, True)