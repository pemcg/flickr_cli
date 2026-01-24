# f/5.6ish

import flickr_api
import random
import core_groups
from globals import Globals

# -------------------------------------------------

def add_harman_groups_and_tags(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '2622163@N24') # Harman Film Technology
    flickr_api.add_tag_to_photo(flickr, photo_id, 'harmanphoto')

# -------------------------------------------------

def add_kentmere_groups_and_tags(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '2091972@N25') # Kentmere Film
    Globals.set_flag("is_monochrome", True)

# -------------------------------------------------

def add_ilford_groups_and_tags(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '90025665@N00') # Ilford
    flickr_api.add_photo_to_group(flickr, photo_id, '444964@N25')  # I Shoot Ilford Film
    Globals.set_flag("is_monochrome", True)

# -------------------------------------------------

def add_kodak_groups_and_tags(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '89218479@N00') # I Shoot Kodak Film

# -------------------------------------------------

def add_lomography_groups_and_tags(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '1007359@N22')  # Lomography Films

# -------------------------------------------------

def add_cinestill_groups_and_tags(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '2233440@N25')  # CineStillFilm

# -------------------------------------------------

def add_orwo_groups_and_tags(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '340428@N25') # ORWO Film

# -------------------------------------------------

def add_portra_160_groups_and_tags(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '1635005@N21')  # New Kodak Portra 160
    flickr_api.add_photo_to_group(flickr, photo_id, '31794144@N00') # Portra Films
    flickr_api.add_photo_to_photoset(flickr, photo_id, Globals.albums_by_name['Kodak Portra 160'])

# -------------------------------------------------

def add_portra_400_groups_and_tags(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '1499236@N20')  # New Kodak Portra 400
    flickr_api.add_photo_to_group(flickr, photo_id, '31794144@N00') # Portra Films
    flickr_api.add_photo_to_photoset(flickr, photo_id, Globals.albums_by_name['Kodak Portra 400'])

# -------------------------------------------------

def add_portra_800_groups_and_tags(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '31794144@N00') # Portra Films
    flickr_api.add_photo_to_photoset(flickr, photo_id, Globals.albums_by_name['Kodak Portra 800'])

# -------------------------------------------------

def add_gold_groups_and_tags(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '37682607@N00') # Kodak Gold
    flickr_api.add_photo_to_photoset(flickr, photo_id, Globals.albums_by_name['Kodak Gold 200'])

# -------------------------------------------------

def add_ultramax_groups_and_tags(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '1070587@N20')  # Kodak UltraMax
    flickr_api.add_photo_to_photoset(flickr, photo_id, Globals.albums_by_name['Kodak Ultramax 400'])

# -------------------------------------------------

def add_ektar_groups_and_tags(flickr, photo_id):
    flickr_api.add_photo_to_photoset(flickr, photo_id, Globals.albums_by_name['Kodak Ektar 400'])

# -------------------------------------------------

def add_phoenix_groups_and_tags(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '14828111@N25') # Harman Phoenix 200 film
    flickr_api.add_photo_to_photoset(flickr, photo_id, Globals.albums_by_name['Harman Phoenix 200'])

# -------------------------------------------------

def add_fp4_groups_and_tags(flickr, photo_id):
    flickr_api.add_photo_to_photoset(flickr, photo_id, Globals.albums_by_name['Ilford FP4+'])

# -------------------------------------------------

def add_hp5_groups_and_tags(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '342830@N20')  # Ilford HP5 Plus
    match Globals.exif_data['iso']:
        case '400':
            flickr_api.add_photo_to_photoset(flickr, photo_id, Globals.albums_by_name['Ilford HP5+ (box speed)'])
        case '800':
            flickr_api.add_photo_to_photoset(flickr, photo_id, Globals.albums_by_name['Ilford HP5+ @800 ISO'])
        case '1600':
            flickr_api.add_photo_to_photoset(flickr, photo_id, Globals.albums_by_name['Ilford HP5+ @1600 ISO'])

# -------------------------------------------------

def add_delta_400_groups_and_tags(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '42554446@N00') # Ilford Delta 400 b&w film
    flickr_api.add_photo_to_photoset(flickr, photo_id, Globals.albums_by_name['Ilford Delta 400'])

# -------------------------------------------------

def add_delta_3200_groups_and_tags(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '55584695@N00') # Ilford DELTA 3200 Professional b&w film
    flickr_api.add_photo_to_photoset(flickr, photo_id, Globals.albums_by_name['Ilford Delta 3200'])

# -------------------------------------------------

def add_kentmere_100_groups_and_tags(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '14783717@N20') # Kentmere 100
    flickr_api.add_photo_to_photoset(flickr, photo_id, Globals.albums_by_name['Kentmere 100'])

# -------------------------------------------------

def add_kentmere_200_groups_and_tags(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '14940565@N22') # Kentmere Pan 200
    flickr_api.add_photo_to_photoset(flickr, photo_id, Globals.albums_by_name['Kentmere 200'])

# -------------------------------------------------

def add_kentmere_400_groups_and_tags(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '3984266@N20') # Kentmere 400
    flickr_api.add_photo_to_photoset(flickr, photo_id, Globals.albums_by_name['Kentmere 400'])

# -------------------------------------------------

def add_acros_groups_and_tags(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '32685380@N00') # Acros
    flickr_api.add_photo_to_photoset(flickr, photo_id, Globals.albums_by_name['Fujifilm Neopan Acros II'])
    Globals.set_flag("is_monochrome", True)

# -------------------------------------------------

def add_core_film_groups(flickr, photo_id):
    print("-- Adding random set of core film groups --")
    for group in core_groups.core_film_groups:
        flip = random.randint(0, 1)
        if (flip == 0):
            flickr_api.add_photo_to_group(flickr, photo_id, group['id'])

# -------------------------------------------------

def add_core_film_tags(flickr, photo_id):
    print("-- Adding core tags --")
    flickr_api.add_tag_to_photo(flickr, photo_id, '"Film is Not Dead"')
    flickr_api.add_tag_to_photo(flickr, photo_id, '"Film Photography"')
    flickr_api.add_tag_to_photo(flickr, photo_id, '"Shooting Film"')
    flickr_api.add_tag_to_photo(flickr, photo_id, '"Believe In Film"')
    flickr_api.add_tag_to_photo(flickr, photo_id, '"Essential Film Holder"')
    flickr_api.add_tag_to_photo(flickr, photo_id, '"Analogue Toolbox for Capture One"')
    flickr_api.add_tag_to_photo(flickr, photo_id, 'Film')
    flickr_api.add_tag_to_photo(flickr, photo_id, 'Analogue')

