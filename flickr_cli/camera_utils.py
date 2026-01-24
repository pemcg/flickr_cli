# f/5.6ish

from globals import Globals
import flickr_api

# -------------------------------------------------

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

# -------------------------------------------------

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
            Globals.set_flag("is_rangefinder", True)
        case 'iiif':
            flickr_api.add_photo_to_group(flickr, photo_id, '63875550@N00') # Leica IIIf
            Globals.set_flag("is_rangefinder", True)
        case 'Mini II':
            flickr_api.add_photo_to_group(flickr, photo_id, '1412184@N21')  # Leica Mini
        case 'Rollei 35':
            flickr_api.add_photo_to_group(flickr, photo_id, '60539930@N00') # Rollei 35
            Globals.set_flag("is_35mm", True)
        case 'PowerShot S120':
            flickr_api.add_photo_to_group(flickr, photo_id, '2372297@N21') # Canon Powershot S120
            Globals.set_flag("is_vintage_lens", False)
            Globals.set_flag("is_vintage_digital", True)
        case 'Bessa R':
            flickr_api.add_photo_to_group(flickr, photo_id, '777631@N25')   # Bessa R
            Globals.set_flag("is_35mm", True)
            Globals.set_flag("is_rangefinder", True)
        case 'GS645S':
            flickr_api.add_photo_to_group(flickr, photo_id, '2897798@N24')  # Fujica GS645
            Globals.set_flag("is_120", True)
            Globals.set_flag("is_6x45", True)
            Globals.set_flag("is_rangefinder", True)
            Globals.set_flag("is_Fuji_rangefinder", True)
        case 'GW690':
            flickr_api.add_photo_to_group(flickr, photo_id, '980734@N22')  # Fuji GW 690
            Globals.set_flag("is_120", True)
            Globals.set_flag("is_6x9", True)
            Globals.set_flag("is_rangefinder", True)
            Globals.set_flag("is_Fuji_rangefinder", True)
        case 'ETRSi':
            flickr_api.add_photo_to_group(flickr, photo_id, '765812@N25')   # ETRS
            Globals.set_flag("is_6x45", True)
        case 'GS-1':
            Globals.set_flag("is_6x7", True)
        case 'Rolleicord Vb':
            flickr_api.add_photo_to_group(flickr, photo_id, '87036574@N00') # Rolleicord
            Globals.set_flag("is_120", True)
            Globals.set_flag("is_6x6", True)
            Globals.set_flag("is_TLR", True)

# -------------------------------------------------

def add_leica_m6_groups(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '12985286@N00') # M6 & MP LEICA
    flickr_api.add_photo_to_group(flickr, photo_id, '2636468@N20')  # LEICA M ANALOG

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

def add_fuji_rangefinder_groups_and_tags(flickr, photo_id):
    flickr_api.add_tag_to_photo(flickr, photo_id, '"Fuji Rangefinder"')
    flickr_api.add_photo_to_group(flickr, photo_id, '762957@N22') # FUJI RANGEFINDER FILM CAMERAS

    