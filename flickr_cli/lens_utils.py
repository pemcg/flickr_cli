# f/5.6ish

import re
import flickr_api
from globals import Globals

# -------------------------------------------------

def handle_carl_zeiss_lenses(lens_model, flickr, photo_id):
    if re.search('C-Sonnar T\\* 50mm f/1.5', lens_model):
        flickr_api.add_photo_to_group(flickr, photo_id, '26443211@N00') # ZM C Sonnar 50mm
    elif re.search('Planar 2.8/80 T\\*', lens_model):
        flickr_api.add_photo_to_group(flickr, photo_id, '1230318@N20') # Hasselblad 80mm (FILM and 80mm ONLY)
    elif re.search('Distagon 50mm f/4 CF FLE', lens_model):
        flickr_api.add_photo_to_group(flickr, photo_id, '1065377@N25') # Hasselblad 50mm Zeiss Distagon

# -------------------------------------------------

def handle_leitz_lenses(lens_model, flickr, photo_id):
    if re.search('Summicron', lens_model):
        flickr_api.add_photo_to_group(flickr, photo_id, '63445765@N00') # Leica Summicron-M 50mm
    if re.search('Elmar 50mm', lens_model):
        flickr_api.add_photo_to_group(flickr, photo_id, '87628977@N00') # Leica Elmar 50

# -------------------------------------------------

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

# -------------------------------------------------

def handle_pentax_lenses(lens_model, flickr, photo_id):
    if re.search('Pentax-M 50mm f/1.7', lens_model):
        flickr_api.add_photo_to_group(flickr, photo_id, '1843361@N21') # Pentax SMC 50mm f/1.7
    elif re.search('Pentax-M 40mm f/2.8', lens_model):
        flickr_api.add_photo_to_group(flickr, photo_id, '2354873@N25') # SMC Pentax-M 40mm 1:2.8

# -------------------------------------------------

def handle_voigtlander_lenses(lens_model, flickr, photo_id):
    Globals.set_flag("is_vintage_lens", False)
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

def add_pc_lens_groups_and_tags(flickr, photo_id):
    flickr_api.add_photo_to_group(flickr, photo_id, '97236268@N00') # Tilt Shift
    flickr_api.add_tag_to_photo(flickr, photo_id, '"Perspective Control"')
    flickr_api.add_tag_to_photo(flickr, photo_id, '"Shift Lens"')