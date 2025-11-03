#!/usr/bin/env python3
# f/5.6ish      

exif_data           = {}
albums              = {}
groups              = {}
is_square           = False
is_digital          = False
is_monochrome       = False
is_mono_from_colour = False
is_35mm             = False
is_120              = False
is_6x6              = False
is_6x45             = False
is_Leica            = False
is_Nikon            = False
is_NikonF           = False
is_Olympus          = False
is_Pentax           = False
is_Bronica          = False
is_Hasselblad       = False
is_TLR              = False
is_pc_lens          = False
is_vintage_digital  = False
is_vintage_lens     = True  # default to true as most lenses are vintage

GROUP_MEMBER        = 2
GROUP_MODERATOR     = 3
GROUP_ADMIN         = 4