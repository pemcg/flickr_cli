# f/5.6ish

import re
from globals import Globals
import core_groups
import flickr_api
import here_api
import get_utils
import random

def add_core_film_groups(flickr, photo_id):
    print("-- Adding random set of core film groups --")
    for group in core_groups.core_film_groups:
        flip = random.randint(0, 1)
        if (flip == 0):
            flickr_api.add_photo_to_group(flickr, photo_id, group['id'])

# -------------------------------------------------

def add_core_digital_groups(flickr, photo_id):
    print("-- Adding random set of core digital groups --")

# -------------------------------------------------

def add_nikon_groups_and_tags(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '1006613@N25') # Nikon Analogue
    flickr_api.add_photo_to_group(flickr, photo_id, '1691203@N23') # Nikon Film Photography
    flickr_api.add_photo_to_group(flickr, photo_id, '32237332@N00') # Nikon Film Cameras
    flickr_api.add_tag_to_photo(flickr, photo_id, '"Nikon"')

# -------------------------------------------------

def add_pentax_groups_and_tags(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '752144@N22') # Pentax Film Cameras
    flickr_api.add_tag_to_photo(flickr, photo_id, '"Pentax"')

# -------------------------------------------------

def add_olympus_groups_and_tags(flickr, photo_id):
    flickr_api.add_tag_to_photo(flickr, photo_id, '"Olympus"')

# -------------------------------------------------

def add_leica_groups_and_tags(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '2515979@N21') # Leica film Camera
    flickr_api.add_tag_to_photo(flickr, photo_id, '"Leica"')

# -------------------------------------------------

def add_leica_monochrome_groups_and_tags(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '1574526@N20') # Leica B&W (Film Only!)

# -------------------------------------------------

def add_hasselblad_groups_and_tags(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '32208033@N00') # Hasselblad
    flickr_api.add_photo_to_group(flickr, photo_id, '1270524@N23') # Hasselblad 500 Series - film only
    flickr_api.add_tag_to_photo(flickr, photo_id, '"Hasselblad"')

# -------------------------------------------------

def add_bronica_groups_and_tags(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '65011843@N00') # Bronica
    flickr_api.add_tag_to_photo(flickr, photo_id, '"Bronica"')

# -------------------------------------------------

def add_square_groups_and_tags(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '484329@N25') # B Square
    flickr_api.add_photo_to_group(flickr, photo_id, '1536844@N23') # Flair and Square
    flickr_api.add_photo_to_group(flickr, photo_id, '17449586@N00') # square (don't post the not square photo)
    flickr_api.add_tag_to_photo(flickr, photo_id, '"Square"')

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

def add_645_groups_and_tags(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '304405@N25') # 645 Medium Format
    flickr_api.add_tag_to_photo(flickr, photo_id, '"645 Medium Format"')

# -------------------------------------------------

def add_tlr_groups_and_tags(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '568502@N20') # TLR
    flickr_api.add_photo_to_group(flickr, photo_id, '35034355476@N01') # Twin Lens Reflex
    flickr_api.add_tag_to_photo(flickr, photo_id, '"Twin Lens Reflex"')
    flickr_api.add_tag_to_photo(flickr, photo_id, '"TLR"')

# -------------------------------------------------

def add_pc_lens_groups_and_tags(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '97236268@N00') # Tilt Shift
    flickr_api.add_tag_to_photo(flickr, photo_id, '"Perspective Control"')
    flickr_api.add_tag_to_photo(flickr, photo_id, '"Shift Lens"')

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

# -------------------------------------------------

def isBlank(myString):
    return not (myString and myString.strip())

# -------------------------------------------------

def add_camera_related_groups_and_tags_from_exif(flickr, photo_id):
    print("-- Adding camera-related groups and tags --")

    if 'camera_make' in Globals.exif_data:
        camera_make = Globals.exif_data['camera_make']
        handle_camera_make(camera_make, flickr, photo_id)
        camera_make_and_model = f"{camera_make} {Globals.exif_data['camera_model']}"
    else:
        camera_make_and_model = Globals.exif_data['camera_model']

    flickr_api.add_tag_to_photo(flickr, photo_id, f'"{camera_make_and_model}"')
    
    try:
        flickr_api.add_photo_to_photoset(flickr, photo_id, Globals.albums_by_name[camera_make_and_model])
    except KeyError:
        print(f"Album '{camera_make_and_model}' doesn't exist")
    
    handle_camera_model(Globals.exif_data['camera_model'], flickr, photo_id)

def handle_camera_make(camera_make, flickr, photo_id):
    match camera_make:
        case 'Nikon':
            if not Globals.get_flag("is_digital"):
                add_nikon_groups_and_tags(flickr, photo_id)
                Globals.set_flag("is_35mm", True)
            Globals.set_flag("is_Nikon", True)
        case 'Pentax':
            add_pentax_groups_and_tags(flickr, photo_id)
            Globals.set_flag("is_35mm", True)
            Globals.set_flag("is_Pentax", True)
        case 'Hasselblad':
            add_hasselblad_groups_and_tags(flickr, photo_id)
            Globals.set_flag("is_120", True)
            Globals.set_flag("is_6x6", True)
            Globals.set_flag("is_Hasselblad", True)
        case 'Bronica':
            add_bronica_groups_and_tags(flickr, photo_id)
            Globals.set_flag("is_120", True)
            Globals.set_flag("is_Bronica", True)
        case 'Leica':
            add_leica_groups_and_tags(flickr, photo_id)
            Globals.set_flag("is_35mm", True)
            Globals.set_flag("is_Leica", True)
        case 'Olympus':
            add_olympus_groups_and_tags(flickr, photo_id)
            Globals.set_flag("is_35mm", True)
            Globals.set_flag("is_Olympus", True)

def handle_camera_model(camera_model, flickr, photo_id):
    match camera_model:
        case 'F':
            Globals.set_flag("is_NikonF", True)
        case 'F2':
            flickr_api.add_photo_to_group(flickr, photo_id, '33461219@N00')  # Nikon F2
            Globals.set_flag("is_NikonF", True)
        case 'F3':
            flickr_api.add_photo_to_group(flickr, photo_id, '18787520@N00')  # Nikon F3
            Globals.set_flag("is_NikonF", True)
        case 'F4':
            flickr_api.add_photo_to_group(flickr, photo_id, '685310@N22')   # Nikon F4
            Globals.set_flag("is_NikonF", True)
        case 'FE2':
            flickr_api.add_photo_to_group(flickr, photo_id, '60376222@N00') # Nikon FE2
        case 'FM' | 'FM2':
            flickr_api.add_photo_to_group(flickr, photo_id, '95263654@N00') # Nikon FM series
        case 'Df':
            flickr_api.add_photo_to_group(flickr, photo_id, '2377061@N20')  # Nikon Df - Official
            Globals.set_flag("is_vintage_digital", True)
        case 'MX':
            flickr_api.add_photo_to_group(flickr, photo_id, '32373122@N00') # Pentax MX
        case 'OM-2n':
            flickr_api.add_photo_to_group(flickr, photo_id, '478168@N24') # Olympus OM-2 (Please read the TAG rules)
        case 'M6':
            add_leica_m6_groups(flickr, photo_id)
        case 'iiif':
            flickr_api.add_photo_to_group(flickr, photo_id, '63875550@N00') # Leica IIIf
        case 'Mini II':
            flickr_api.add_photo_to_group(flickr, photo_id, '1412184@N21')  # Leica Mini
        case 'Rollei 35':
            flickr_api.add_photo_to_group(flickr, photo_id, '60539930@N00') # Rollei 35
            Globals.set_flag("is_35mm", True)
        case 'Bessa R':
            flickr_api.add_photo_to_group(flickr, photo_id, '777631@N25')   # Bessa R
            Globals.set_flag("is_35mm", True)
        case 'GS645S':
            flickr_api.add_photo_to_group(flickr, photo_id, '2897798@N24')  # Fujica GS645
            Globals.set_flag("is_120", True)
            Globals.set_flag("is_6x45", True)
        case 'ETRSi':
            flickr_api.add_photo_to_group(flickr, photo_id, '765812@N25')   # ETRS
            Globals.set_flag("is_6x45", True)
        case 'Rolleicord Vb':
            flickr_api.add_photo_to_group(flickr, photo_id, '87036574@N00') # Rolleicord
            Globals.set_flag("is_120", True)
            Globals.set_flag("is_6x6", True)
            Globals.set_flag("is_TLR", True)

def add_leica_m6_groups(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '12985286@N00') # M6 & MP LEICA
    flickr_api.add_photo_to_group(flickr, photo_id, '2636468@N20')  # LEICA M ANALOG

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
        handle_tag(tag, flickr, photo_id)

def handle_tag(tag, flickr, photo_id):
    match tag:
        case 'CineStill':
            handle_cinestill(flickr, photo_id)
        case 'BwXX':
            Globals.set_flag("is_monochrome", True)
        case 'Lomography':
            handle_lomography(flickr, photo_id)
        case 'Kodak':
            handle_kodak(flickr, photo_id)
        case 'Portra 160':
            handle_portra_160(flickr, photo_id)
        case 'Portra 400':
            handle_portra_400(flickr, photo_id)
        case 'Portra 800':
            handle_portra_800(flickr, photo_id)
        case 'UltraMax 400':
            handle_ultramax(flickr, photo_id)
        case 'Ektar 400':
            handle_ektar(flickr, photo_id)
        case 'Ilford':
            handle_ilford(flickr, photo_id)
        case 'FP4+':
            handle_fp4(flickr, photo_id)
        case 'HP5+':
            handle_hp5(flickr, photo_id)
        case 'Phoenix' | 'Phoenix II':
            handle_phoenix(flickr, photo_id)
        case 'Delta 400':
            handle_delta_400(flickr, photo_id)
        case 'Delta 3200':
            handle_delta_3200(flickr, photo_id)
        case 'Kentmere':
            handle_kentmere(flickr, photo_id)
        case 'Harman':
            handle_harman(flickr, photo_id)
        case 'Kentmere 100':
            handle_kentmere_100(flickr, photo_id)
        case 'Kentmere 200':
            handle_kentmere_200(flickr, photo_id)
        case 'Kentmere 400':
            handle_kentmere_400(flickr, photo_id)
        case 'Orwo':
            handle_orwo(flickr, photo_id)
        case 'Neopan Acros II':
            handle_acros(flickr, photo_id)
        case 'Monochrome':
            handle_monochrome()

def handle_harman(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '2622163@N24') # Harman Film Technology
    flickr_api.add_tag_to_photo(flickr, photo_id, 'harmanphoto')

def handle_kentmere(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '2091972@N25') # Kentmere Film
    Globals.set_flag("is_monochrome", True)

def handle_ilford(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '90025665@N00') # Ilford
    flickr_api.add_photo_to_group(flickr, photo_id, '444964@N25')  # I Shoot Ilford Film
    Globals.set_flag("is_monochrome", True)

def handle_kodak(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '89218479@N00') # I Shoot Kodak Film

def handle_lomography(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '1007359@N22')  # Lomography Films

def handle_cinestill(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '2233440@N25')  # CineStillFilm

def handle_orwo(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '340428@N25') # ORWO Film

def handle_portra_160(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '1635005@N21')  # New Kodak Portra 160
    flickr_api.add_photo_to_group(flickr, photo_id, '31794144@N00') # Portra Films
    flickr_api.add_photo_to_photoset(flickr, photo_id, Globals.albums_by_name['Kodak Portra 160'])

def handle_portra_400(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '1499236@N20')  # New Kodak Portra 400
    flickr_api.add_photo_to_group(flickr, photo_id, '31794144@N00') # Portra Films
    flickr_api.add_photo_to_photoset(flickr, photo_id, Globals.albums_by_name['Kodak Portra 400'])

def handle_portra_800(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '31794144@N00') # Portra Films
    flickr_api.add_photo_to_photoset(flickr, photo_id, Globals.albums_by_name['Kodak Portra 800'])

def handle_ultramax(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '1070587@N20')  # Kodak UltraMax
    flickr_api.add_photo_to_photoset(flickr, photo_id, Globals.albums_by_name['Kodak Ultramax 400'])

def handle_ektar(flickr, photo_id):
    flickr_api.add_photo_to_photoset(flickr, photo_id, Globals.albums_by_name['Kodak Ektar 400'])

def handle_phoenix(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '14828111@N25') # Harman Phoenix 200 film
    flickr_api.add_photo_to_photoset(flickr, photo_id, Globals.albums_by_name['Harman Phoenix 200'])

def handle_fp4(flickr, photo_id):
    flickr_api.add_photo_to_photoset(flickr, photo_id, Globals.albums_by_name['Ilford FP4+'])

def handle_hp5(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '342830@N20')  # Ilford HP5 Plus
    match Globals.exif_data['iso']:
        case '400':
            flickr_api.add_photo_to_photoset(flickr, photo_id, Globals.albums_by_name['Ilford HP5+ (box speed)'])
        case '800':
            flickr_api.add_photo_to_photoset(flickr, photo_id, Globals.albums_by_name['Ilford HP5+ @800 ISO'])
        case '1600':
            flickr_api.add_photo_to_photoset(flickr, photo_id, Globals.albums_by_name['Ilford HP5+ @1600 ISO'])

def handle_delta_400(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '42554446@N00') # Ilford Delta 400 b&w film
    flickr_api.add_photo_to_photoset(flickr, photo_id, Globals.albums_by_name['Ilford Delta 400'])

def handle_delta_3200(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '55584695@N00') # Ilford DELTA 3200 Professional b&w film
    flickr_api.add_photo_to_photoset(flickr, photo_id, Globals.albums_by_name['Ilford Delta 3200'])

def handle_kentmere_100(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '14783717@N20') # Kentmere 100
    flickr_api.add_photo_to_photoset(flickr, photo_id, Globals.albums_by_name['Kentmere 100'])

def handle_kentmere_200(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '14940565@N22') # Kentmere Pan 200
    flickr_api.add_photo_to_photoset(flickr, photo_id, Globals.albums_by_name['Kentmere 200'])

def handle_kentmere_400(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '3984266@N20') # Kentmere 400
    flickr_api.add_photo_to_photoset(flickr, photo_id, Globals.albums_by_name['Kentmere 400'])

def handle_acros(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '32685380@N00') # Acros
    flickr_api.add_photo_to_photoset(flickr, photo_id, Globals.albums_by_name['Fujifilm Neopan Acros II'])
    Globals.set_flag("is_monochrome", True)
    
def handle_monochrome():
    Globals.set_flag("is_monochrome", True)
    Globals.set_flag("is_mono_from_colour", True)

# -------------------------------------------------

def add_lens_related_groups_and_tags_from_exif(flickr, photo_id):
    print("-- Adding lens-related groups and tags --")
    
    lens_model = Globals.exif_data['lens_model']
    focal_length = Globals.exif_data['focal_length']
    lens_make = Globals.exif_data['lens_make']

    # Handle lens make cases
    match lens_make:
        case 'Carl Zeiss':
            handle_carl_zeiss_lenses(lens_model, flickr, photo_id)
        case 'Leitz' | '':
            handle_leitz_lenses(lens_model, flickr, photo_id)
        case 'Nikon':
            handle_nikon_lenses(lens_model, flickr, photo_id)
        case 'Pentax' | 'Asahi Opt.':
            handle_pentax_lenses(lens_model, flickr, photo_id)
        case 'Vivitar':
            flickr_api.add_photo_to_group(flickr, photo_id, '59032833@N00') # Vivitar Maniacs
        case 'KMZ':
            flickr_api.add_photo_to_group(flickr, photo_id, '1060957@N23') # Jupiter 8 50mm 2.0
        case 'Voigtländer':
            handle_voigtlander_lenses(lens_model, flickr, photo_id)

    # Handle focal length cases
    if focal_length == '28mm':
        flickr_api.add_photo_to_group(flickr, photo_id, '1175002@N21') # 28mm is my Favorite

    # Add tag and handle albums
    flickr_api.add_tag_to_photo(flickr, photo_id, f'"{focal_length} Lens"')
    
    try:
        flickr_api.add_photo_to_photoset(flickr, photo_id, Globals.albums_by_name[lens_model])
    except KeyError:
        print(f"Album '{lens_model}' doesn't exist")

def handle_carl_zeiss_lenses(lens_model, flickr, photo_id):
    if re.search('C-Sonnar T\\* 50mm f/1.5', lens_model):
        flickr_api.add_photo_to_group(flickr, photo_id, '26443211@N00') # ZM C Sonnar 50mm
    elif re.search('Planar 2.8/80 T\\*', lens_model):
        flickr_api.add_photo_to_group(flickr, photo_id, '1230318@N20') # Hasselblad 80mm (FILM and 80mm ONLY)
    elif re.search('Distagon 50mm f/4 CF FLE', lens_model):
        flickr_api.add_photo_to_group(flickr, photo_id, '1065377@N25') # Hasselblad 50mm Zeiss Distagon

def handle_leitz_lenses(lens_model, flickr, photo_id):
    if re.search('Summicron', lens_model):
        flickr_api.add_photo_to_group(flickr, photo_id, '63445765@N00') # Leica Summicron-M 50mm
    if re.search('Elmar 50mm', lens_model):
        flickr_api.add_photo_to_group(flickr, photo_id, '87628977@N00') # Leica Elmar 50

def handle_nikon_lenses(lens_model, flickr, photo_id):
    if re.search('Nikkor 24mm f/2.8', lens_model):
        flickr_api.add_photo_to_group(flickr, photo_id, '892155@N23') # Nikkor 24 mm f/2.8
    elif re.search('Nikkor 28mm f/2.8', lens_model):
        flickr_api.add_photo_to_group(flickr, photo_id, '401700@N21') # Nikkor 28mm f/2.8 lens
    elif re.search('PC-Nikkor 28mm f/3.5', lens_model):
        flickr_api.add_photo_to_group(flickr, photo_id, '1184925@N22') # PC-Nikkor 28mm F3.5
        Globals.set_flag("is_pc_lens", True)
    elif re.search('PC-Nikkor 35mm f/2.8', lens_model):
        Globals.set_flag("is_pc_lens", True)
    elif re.search(r'\bNikkor 35mm f/2\b', lens_model):
        flickr_api.add_photo_to_group(flickr, photo_id, '946552@N23') # Nikkor 35mm f/2
    elif re.search('Nikkor 50mm f/1.4', lens_model):
        flickr_api.add_photo_to_group(flickr, photo_id, '35771367@N00') # Nikkor 50mm 1.4
    elif re.search('Nikkor 50mm f/1.8', lens_model):
        flickr_api.add_photo_to_group(flickr, photo_id, '79414467@N00') # Nikkor 50mm 1.8

def handle_pentax_lenses(lens_model, flickr, photo_id):
    if re.search('Pentax-M 50mm f/1.7', lens_model):
        flickr_api.add_photo_to_group(flickr, photo_id, '1843361@N21') # Pentax SMC 50mm f/1.7
    elif re.search('Pentax-M 40mm f/2.8', lens_model):
        flickr_api.add_photo_to_group(flickr, photo_id, '2354873@N25') # SMC Pentax-M 40mm 1:2.8

def handle_voigtlander_lenses(lens_model, flickr, photo_id):
    globals.is_vintage_lens = False
    flickr_api.add_photo_to_group(flickr, photo_id, '51035603760@N01') # Voigtlander
    if re.search('Color Skopar 28mm f/2.8', lens_model):
        flickr_api.add_photo_to_group(flickr, photo_id, '2065317@N20') # Voigtländer Color Skopar 28mm SLII
    elif re.search('Ultron 40mm f/2', lens_model):
        flickr_api.add_photo_to_group(flickr, photo_id, '935447@N23') # Voigtländer Ultron 40mm f2.0
    elif re.search('Ultron VM 28mm f/2', lens_model):
        flickr_api.add_photo_to_group(flickr, photo_id, '14777249@N24') # Voigtlander 28mm F2 Ultron II (Vintage Line)
    elif re.search('Ultron VM 35mm f/2', lens_model):
        flickr_api.add_photo_to_group(flickr, photo_id, '4585520@N20') # Voigtländer Ultron 35mm f/2 Aspherical M-Mount
    elif re.search('Nokton 58mm f/1.4', lens_model):
        flickr_api.add_photo_to_group(flickr, photo_id, '924032@N21') # Voigtlander Nokton 58mm f/1.4 SL II

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

        if Globals.get_flag("is_6x45"):
            add_645_groups_and_tags(flickr, photo_id)

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
                add_leica_monochrome_groups_and_tags(flickr, photo_id)

    if Globals.get_flag("is_NikonF"):
        flickr_api.add_photo_to_group(flickr, photo_id, '1192730@N21')

    if Globals.get_flag("is_pc_lens"):
        add_pc_lens_groups_and_tags(flickr, photo_id)

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
        add_core_film_groups(flickr, photo_id)
        add_core_film_tags(flickr, photo_id)
        add_film_related_groups_and_tags_from_tags(flickr, photo_id)

    add_camera_related_groups_and_tags_from_exif(flickr, photo_id)
    add_lens_related_groups_and_tags_from_exif(flickr, photo_id)
    add_derived_groups_and_tags(flickr, photo_id)
