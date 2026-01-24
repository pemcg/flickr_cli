# f/5.6ish

from globals import Globals
import flickr_api
import here_api
import get_utils
import film_utils
import lens_utils
import camera_utils

# -------------------------------------------------

def add_core_digital_groups(flickr, photo_id):
    print("-- Adding random set of core digital groups --")

# -------------------------------------------------

def add_rangefinder_groups_and_tags(flickr, photo_id):
    flickr_api.add_tag_to_photo(flickr, photo_id, '"Rangefinder"')
    flickr_api.add_photo_to_group(flickr, photo_id, '12949565@N00') # Rangefinders

# -------------------------------------------------

def add_square_groups_and_tags(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '484329@N25') # B Square
    flickr_api.add_photo_to_group(flickr, photo_id, '1536844@N23') # Flair and Square
    flickr_api.add_photo_to_group(flickr, photo_id, '17449586@N00') # square (don't post the not square photo)
    flickr_api.add_tag_to_photo(flickr, photo_id, '"Square"')
    flickr_api.add_tag_to_photo(flickr, photo_id, '"Square Format"')

# -------------------------------------------------

def add_35mm_groups_and_tags(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '2162153@N23') # 35mm Photographer
    flickr_api.add_tag_to_photo(flickr, photo_id, '"35mm Photography"')
    flickr_api.add_tag_to_photo(flickr, photo_id, '"35mm Film"')

# -------------------------------------------------

def add_120_groups_and_tags(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '73798317@N00') # 120
    flickr_api.add_photo_to_group(flickr, photo_id, '79333178@N00') # Medium Format (120/220 film only)
    flickr_api.add_photo_to_group(flickr, photo_id, '1311107@N20') # Why I Love Medium Format - Film Only
    flickr_api.add_tag_to_photo(flickr, photo_id, '"120 Film"')
    flickr_api.add_tag_to_photo(flickr, photo_id, '"Medium Format"')
    flickr_api.add_tag_to_photo(flickr, photo_id, '"Medium Format Film"')

# -------------------------------------------------

def add_6x45_groups_and_tags(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '304405@N25') # 645 Medium Format
    flickr_api.add_tag_to_photo(flickr, photo_id, '"6x45 Medium Format"')

# -------------------------------------------------

def add_6x6_groups_and_tags(flickr, photo_id):
    flickr_api.add_tag_to_photo(flickr, photo_id, '"6x6 Medium Format"')

# -------------------------------------------------

def add_6x7_groups_and_tags(flickr, photo_id):
    flickr_api.add_tag_to_photo(flickr, photo_id, '"6x7 Medium Format"')

# -------------------------------------------------

def add_6x9_groups_and_tags(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '31284338@N00') # 6x9 Photography - not for changeable backs/lenses
    flickr_api.add_tag_to_photo(flickr, photo_id, '"6x9 Medium Format"')

# -------------------------------------------------

def add_tlr_groups_and_tags(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '568502@N20') # TLR
    flickr_api.add_photo_to_group(flickr, photo_id, '35034355476@N01') # Twin Lens Reflex
    flickr_api.add_tag_to_photo(flickr, photo_id, '"Twin Lens Reflex"')
    flickr_api.add_tag_to_photo(flickr, photo_id, '"TLR"')

# -------------------------------------------------

def add_vintage_digital_groups_and_tags(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '14730048@N25') # Vintage Digital Photography
    flickr_api.add_tag_to_photo(flickr, photo_id, '"Vintage Digital"')
    flickr_api.add_tag_to_photo(flickr, photo_id, '"Decade-old Digital"')

# -------------------------------------------------

def add_monochrome_groups_and_tags(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '52239733174@N01') # B&W
    flickr_api.add_photo_to_group(flickr, photo_id, '44093380@N00') # B&W Gallery
    flickr_api.add_photo_to_group(flickr, photo_id, '1575512@N25') # Black and White Creative Images!
    flickr_api.add_tag_to_photo(flickr, photo_id, '"Black and White"')
    flickr_api.add_tag_to_photo(flickr, photo_id, 'BW')
    flickr_api.add_tag_to_photo(flickr, photo_id, 'Monochrome')

# -------------------------------------------------

def add_monochrome_film_groups_and_tags(flickr, photo_id):
    add_monochrome_groups_and_tags(flickr, photo_id)
    flickr_api.add_photo_to_group(flickr, photo_id, '99542567@N00') # Black and White Film
    flickr_api.add_photo_to_group(flickr, photo_id, '1375913@N24') # Black and White Film Photography (bwfp)
    flickr_api.add_photo_to_group(flickr, photo_id, '72295300@N00') # Classic Black & White  ( Film Only)
    flickr_api.add_photo_to_group(flickr, photo_id, '737780@N25') # B/W_Analog
    if Globals.get_flag("is_mono_from_colour"):
        flickr_api.add_tag_to_photo(flickr, photo_id, '"Monochrome from Colour"')
    else:
        flickr_api.add_photo_to_group(flickr, photo_id, '693115@N20') # Self Developed Photographs
        flickr_api.add_tag_to_photo(flickr, photo_id, '"Ilfotec DD-X"')
    if Globals.get_flag("is_35mm"):
        flickr_api.add_photo_to_group(flickr, photo_id, '57796404@N00') # 35mm blackandwhite

# -------------------------------------------------

def isBlank(myString):
    return not (myString and myString.strip())

# -------------------------------------------------

def add_camera_related_groups_and_tags_from_exif(flickr, photo_id):
    print("-- Adding camera-related groups and tags --")

    if 'camera_make' in Globals.exif_data:
        camera_make = Globals.exif_data['camera_make']
        camera_utils.handle_camera_make(camera_make, flickr, photo_id)
        camera_make_and_model = f"{camera_make} {Globals.exif_data['camera_model']}"
    else:
        camera_make_and_model = Globals.exif_data['camera_model']

    flickr_api.add_tag_to_photo(flickr, photo_id, f'"{camera_make_and_model}"')
    
    try:
        flickr_api.add_photo_to_photoset(flickr, photo_id, Globals.albums_by_name[camera_make_and_model])
    except KeyError:
        print(f"Album '{camera_make_and_model}' doesn't exist")
    
    camera_utils.handle_camera_model(Globals.exif_data['camera_model'], flickr, photo_id)

# -------------------------------------------------

def add_geo_data_by_location(flickr, photo_id, location):
    coords = here_api.get_geo_coordinates_from_location(location)
    flickr_api.set_photo_location(flickr, photo_id, coords['lat'], coords['lon'], flickr_api.GEO_ACCURACY_CITY, flickr_api.GEO_CONTEXT_OUTDOORS)

# -------------------------------------------------

def add_geo_data_by_coords(flickr, photo_id, coord_string):
    coords = get_utils.get_geo_coordinates_from_coord_string(coord_string)
    flickr_api.set_photo_location(flickr, photo_id, coords['lat'], coords['lon'], flickr_api.GEO_ACCURACY_STREET, flickr_api.GEO_CONTEXT_OUTDOORS)

# -------------------------------------------------

def add_film_related_groups_and_tags_from_tags(flickr, photo_id):
    print("-- Adding film-related groups and tags --")

    for tag in Globals.tags:
        match tag:
            case 'CineStill':
                film_utils.add_cinestill_groups_and_tags(flickr, photo_id)
            case 'BwXX':
                Globals.set_flag("is_monochrome", True)
            case 'Lomography':
                film_utils.add_lomography_groups_and_tags(flickr, photo_id)
            case 'Kodak':
                film_utils.add_kodak_groups_and_tags(flickr, photo_id)
            case 'Portra 160':
                film_utils.add_portra_160_groups_and_tags(flickr, photo_id)
            case 'Portra 400':
                film_utils.add_portra_400_groups_and_tags(flickr, photo_id)
            case 'Portra 800':
                film_utils.add_portra_800_groups_and_tags(flickr, photo_id)
            case 'UltraMax 400':
                film_utils.add_ultramax_groups_and_tags(flickr, photo_id)
            case 'Gold 200':
                film_utils.add_gold_groups_and_tags(flickr, photo_id)
            case 'Ektar 100':
                film_utils.add_ektar_groups_and_tags(flickr, photo_id)
            case 'Ilford':
                film_utils.add_ilford_groups_and_tags(flickr, photo_id)
            case 'FP4+':
                film_utils.add_fp4_groups_and_tags(flickr, photo_id)
            case 'HP5+':
                film_utils.add_hp5_groups_and_tags(flickr, photo_id)
            case 'Phoenix' | 'Phoenix II':
                film_utils.add_phoenix_groups_and_tags(flickr, photo_id)
            case 'Delta 400':
                film_utils.add_delta_400_groups_and_tags(flickr, photo_id)
            case 'Delta 3200':
                film_utils.add_delta_3200_groups_and_tags(flickr, photo_id)
            case 'Kentmere':
                film_utils.add_kentmere_groups_and_tags(flickr, photo_id)
            case 'Harman':
                film_utils.add_harman_groups_and_tags(flickr, photo_id)
            case 'Kentmere 100':
                film_utils.add_kentmere_100_groups_and_tags(flickr, photo_id)
            case 'Kentmere 200':
                film_utils.add_kentmere_200_groups_and_tags(flickr, photo_id)
            case 'Kentmere 400':
                film_utils.add_kentmere_400_groups_and_tags(flickr, photo_id)
            case 'Orwo':
                film_utils.add_orwo_groups_and_tags(flickr, photo_id)
            case 'Neopan Acros II':
                film_utils.add_acros_groups_and_tags(flickr, photo_id)
            case 'Monochrome':
                add_monochrome_groups_and_tags()
    
def add_monochrome_groups_and_tags():
    Globals.set_flag("is_monochrome", True)
    Globals.set_flag("is_mono_from_colour", True)

# -------------------------------------------------

def add_lens_related_groups_and_tags_from_exif(flickr, photo_id):
    print("-- Adding lens-related groups and tags --")
    
    lens_model = Globals.exif_data['lens_model']
    focal_length = Globals.exif_data['focal_length']
    if 'lens_make' in Globals.exif_data:
        lens_make = Globals.exif_data['lens_make']
    else:
        lens_make = ''

    # Handle lens make cases
    match lens_make:
        case 'Carl Zeiss':
            lens_utils.handle_carl_zeiss_lenses(lens_model, flickr, photo_id)
        case 'Leitz' | '':
            lens_utils.handle_leitz_lenses(lens_model, flickr, photo_id)
        case 'Nikon':
            lens_utils.handle_nikon_lenses(lens_model, flickr, photo_id)
        case 'Pentax' | 'Asahi Opt.':
            lens_utils.handle_pentax_lenses(lens_model, flickr, photo_id)
        case 'Vivitar':
            flickr_api.add_photo_to_group(flickr, photo_id, '59032833@N00') # Vivitar Maniacs
        case 'KMZ':
            flickr_api.add_photo_to_group(flickr, photo_id, '1060957@N23') # Jupiter 8 50mm 2.0
        case 'Voigtländer':
            lens_utils.handle_voigtlander_lenses(lens_model, flickr, photo_id)

    # Handle focal length cases
    if focal_length == '28mm':
        flickr_api.add_photo_to_group(flickr, photo_id, '1175002@N21') # 28mm is my Favorite

    # Add tag and handle albums
    flickr_api.add_tag_to_photo(flickr, photo_id, f'"{focal_length} Lens"')
    
    try:
        flickr_api.add_photo_to_photoset(flickr, photo_id, Globals.albums_by_name[lens_model])
    except KeyError:
        print(f"Album '{lens_model}' doesn't exist")


# -------------------------------------------------

def add_derived_groups_and_tags(flickr, photo_id):
    print("-- Adding derived groups and tags --")

    if Globals.get_flag("is_35mm"):
        add_35mm_groups_and_tags(flickr, photo_id)

    if Globals.get_flag("is_120"):
        add_120_groups_and_tags(flickr, photo_id)

        if Globals.get_flag("is_6x6"):
            group_id = '38457755@N00' if Globals.get_flag("is_monochrome") else '514022@N22'
            flickr_api.add_photo_to_group(flickr, photo_id, group_id)
            add_6x6_groups_and_tags(flickr, photo_id)

        if Globals.get_flag("is_6x45"):
            add_6x45_groups_and_tags(flickr, photo_id)

        if Globals.get_flag("is_6x7"):
            add_6x7_groups_and_tags(flickr, photo_id)

        if Globals.get_flag("is_6x9"):
            add_6x9_groups_and_tags(flickr, photo_id)

        if Globals.get_flag("is_TLR"):
            add_tlr_groups_and_tags(flickr, photo_id)

    if Globals.get_flag("is_square"):
        add_square_groups_and_tags(flickr, photo_id)

    if Globals.get_flag("is_monochrome"):
        if Globals.get_flag("is_digital"):
            add_monochrome_groups_and_tags(flickr, photo_id)
        else:
            add_monochrome_film_groups_and_tags(flickr, photo_id)

            if Globals.get_flag("is_Leica"):
                camera_utils.add_leica_monochrome_groups_and_tags(flickr, photo_id)

    if Globals.get_flag("is_NikonF"):
        flickr_api.add_photo_to_group(flickr, photo_id, '1192730@N21')

    if Globals.get_flag("is_rangefinder"):
        add_rangefinder_groups_and_tags(flickr, photo_id)

    if Globals.get_flag("is_Fuji_rangefinder"):
        camera_utils.add_fuji_rangefinder_groups_and_tags(flickr, photo_id)

    if Globals.get_flag("is_pc_lens"):
        lens_utils.add_pc_lens_groups_and_tags(flickr, photo_id)

    if Globals.get_flag("is_vintage_digital"):
        add_vintage_digital_groups_and_tags(flickr, photo_id)

    if Globals.get_flag("is_digital") and Globals.get_flag("is_vintage_lens"):
        flickr_api.add_photo_to_group(flickr, photo_id, '1513273@N23')

# -------------------------------------------------  

def callback(progress):
    # print(progress)
    print(' Uploading File: [%d%%]\r'%progress, end="")

# -------------------------------------------------  

def add_groups_and_tags(flickr, photo_id):
    print("Photo dimensions in pixels: %s" % get_utils.get_photo_sizes(flickr, photo_id))

    if Globals.get_flag("is_digital"):
        add_core_digital_groups(flickr, photo_id)
    else:
        film_utils.add_core_film_groups(flickr, photo_id)
        film_utils.add_core_film_tags(flickr, photo_id)
        add_film_related_groups_and_tags_from_tags(flickr, photo_id)

    add_camera_related_groups_and_tags_from_exif(flickr, photo_id)
    add_lens_related_groups_and_tags_from_exif(flickr, photo_id)
    add_derived_groups_and_tags(flickr, photo_id)
