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
from globals import Globals
from typing import List, Dict, Set, Optional

#-------------------------------------------------------------------------------------------------------------

def sanity_check_arguments(args: argparse.Namespace) -> bool:
    """
    Template function to validate command line arguments for mutual exclusivity
    and required argument dependencies.
    
    Args:
        args: Parsed arguments from argparse
        
    Returns:
        bool: True if all checks pass, False otherwise
        
    Raises:
        SystemExit: If validation fails (calls sys.exit())
    """
    
    # Define mutually exclusive argument groups
    # Each tuple contains arguments that cannot be used together
    MUTUALLY_EXCLUSIVE_GROUPS = [
        ('add', 'upload', 'get_tags', 'get_groups'),  # Example: action arguments
        ('verbose', 'quiet'),            # Example: output level arguments
    ]
    
    # Define argument dependencies
    # Key: argument that requires dependencies
    # Value: list of required arguments when key is present
    ARGUMENT_DEPENDENCIES = {
        'add': ['id'],           # create requires target and name
        'get_tags': ['id'],                   # delete requires target
        'get_group_photos': ['group', 'days'],
        'get_user_groups_with_admin_activity': ['days'],
        'get_group_members_with_recent_activity': ['group', 'days'],
    }
    
    # Define conditional dependencies (at least one required)
    # Key: argument that requires at least one from the list
    # Value: list of arguments where at least one must be present
    AT_LEAST_ONE_REQUIRED = {
        'upload': ['filename', 'title', 'description'],
    }
    
    errors = []
    
    # Check for mutually exclusive arguments
    for exclusive_group in MUTUALLY_EXCLUSIVE_GROUPS:
        present_args = [arg for arg in exclusive_group if getattr(args, arg, None)]
        if len(present_args) > 1:
            errors.append(f"Mutually exclusive arguments provided: {', '.join(present_args)}")
    
    # Check argument dependencies
    for main_arg, required_args in ARGUMENT_DEPENDENCIES.items():
        if getattr(args, main_arg, None):  # If main argument is present
            missing_deps = []
            for req_arg in required_args:
                if not getattr(args, req_arg, None):
                    missing_deps.append(req_arg)
            
            if missing_deps:
                errors.append(f"Argument '{main_arg}' requires: {', '.join(missing_deps)}")
    
    # Check "at least one required" dependencies
    for main_arg, option_args in AT_LEAST_ONE_REQUIRED.items():
        if getattr(args, main_arg, None):  # If main argument is present
            present_options = [arg for arg in option_args if getattr(args, arg, None)]
            if not present_options:
                errors.append(f"Argument '{main_arg}' requires at least one of: {', '.join(option_args)}")
    
   
    if hasattr(args, 'days') and args.days:
        if int(args.days) < 0:
            errors.append(f"days count must be positive, got: {args.days}")
    
    # Report errors and exit if any found
    if errors:
        print("❌ Argument validation errors:", file=sys.stderr)
        for i, error in enumerate(errors, 1):
            print(f"  {i}. {error}", file=sys.stderr)
        print("\nUse --help for usage information.", file=sys.stderr)
        sys.exit(1)
    
    return

#-------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Add a photo to Flickr globals.groups.')
    parser.add_argument('--id', help='The ID of the photo or group to process', required=False)
    parser.add_argument('--get_groups', help='Get group list for photo or user', action='store_true')
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
    sanity_check_arguments(args)

    #
    # set some global variables based on command line arguments
    #


    # Uncomment for debugging
    # logging.basicConfig(filename='flickr_cli.log', filemode='w', level=logging.DEBUG)
    # flickr_api.enable_debug_logging()

    flickr_client = flickr_api.authenticate()

    if hasattr(args, 'id'):
        Globals.initialize(flickr_client, args.id)
    else:
        Globals.initialize(flickr_client)

    # Set global flags
    if args.digital:
        Globals.set_flag("is_digital", True)
    if args.monochrome:
        Globals.set_flag("is_monochrome", True)

    def get_group_id(group_name: str, action_name: str) -> str:
        """Get group ID for the specified group name."""
        if group_name not in Globals.GROUP_IDS:
            print(f"Need a valid group name for the {action_name} argument")
            print(f"Available groups: {', '.join(Globals.GROUP_IDS.keys())}")
            sys.exit(1)
        return Globals.GROUP_IDS[group_name]

    def handle_photo_operations():
        """Handle photo-related operations."""
        if args.add:
            add_utils.add_groups_and_tags(flickr_client, args.id)
            handle_location_operations()
        elif args.get_tags:
            get_utils.get_tags()

    def handle_location_operations():
        """Handle location-related operations."""
        if args.location:
            add_utils.add_geo_data_by_location(flickr_client, args.id, args.location)
        if args.coords:
            add_utils.add_geo_data_by_coords(flickr_client, args.id, args.coords)

    def handle_group_operations():
        """Handle group-related operations."""
        if args.get_groups:
            get_utils.get_user_groups(flickr_client)
        elif args.get_user_groups_with_admin_activity:
            group_utils.get_user_groups_with_admin_activity(flickr_client, int(args.days))
        elif args.get_user_groups_with_no_admin_activity:
            group_utils.get_user_groups_with_no_admin_activity(flickr_client, int(args.days))
        elif args.get_group_photos:
            group_id = get_group_id(args.group, 'get_group_photos')
            group_utils.get_group_photos(flickr_client, group_id, int(args.days), args.interactive)
        elif args.get_group_members_with_recent_activity:
            group_id = get_group_id(args.group, 'get_group_members_with_recent_activity')
            group_utils.get_group_members_with_recent_activity(flickr_client, group_id, int(args.days))

    def handle_upload_operations():
        """Handle upload-related operations."""
        if args.upload:
            new_photo_id = flickr_api.upload(flickr_client, args.filename, args.title, args.description)
            print(f"New photo id: {new_photo_id}")
            # add_utils.add_groups_and_tags(flickr_client, new_photo_id)  # Uncomment if needed

    def handle_follower_operations():
        """Handle follower-related operations."""
        if args.get_followers:
            get_utils.get_followers(flickr_client, True)

    # Execute operations
    handle_photo_operations()

    # Handle standalone location operations (when not part of add)
    if not args.add:
        handle_location_operations()

    handle_group_operations()
    handle_upload_operations()
    handle_follower_operations()
