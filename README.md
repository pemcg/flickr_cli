# flickr_cli
Command-line tool to simplify admin of newly uploaded photos. It’s very specifically customised for my usage, but anyone is free to use and adapt to their own use. My use case is mainly film photography. I have several cameras and lenses, and like the photo to be added to albums for the camera and lens that was used to take the shot. I also add the photo to a selection of film-related groups, as well as camera, lens, and film specific groups where appropriate. Other tags are added and groups selected depending on whether the image is colour or black and white, the film format (35mm or 120), aspect ratio (6x45, 6x6 etc), camera type (eg TLR), and square photo-specific groups if the pixel aspect ratio is exactly square.

## Authentication

When run the script opens a browser authentication window to enable you to login and authenticate the session.
All authentication keys are held in a separate file `flickr_api/keys.py`, with the following format:

```
FLICKR_API_KEY       = '...fc85c09e7b5...'
FLICKR_API_SECRET    = '...b8010...'
USER_ID              = '...9724@N0.''
HERE_APP_ID          = '...ZzL43zQf..'
HERE_API_KEY         = '...zmKzgUUvjH...'
```
## Command line Arguments

There are several command line arguments, grouped into various categories.

### Uploaded photo processing

The primary purpose of the tool is the adding of a newly uploaded photo to groups and albums, tagging, etc, as described.

#### --add

The `—add` argument does the main donkey work of adding a newly uploaded photo to relevant groups and albums, and adds tags. It must be used with the `—id` argument to specify the photo ID on which to perform the operation.

The procedure to use is:

1. Upload a photo using the Flickr uploader. The photo should have exif camera and lens data set that match corresponding album names, for example “Nikon F3” and "Nikkor 35mm f/2 Ai”.

2. Tag the photo with the film vendor name and type, for example "Kodak"  "Portra 800” or "Kentmere" "Kentmere 200"

3. Copy the new photo’s id from the page url

4. Add the id to the flickr_cli command line.

Example output:

```
./flickr_cli.py --id 54895067952 --add
127.0.0.1 - - [02/Nov/2025 09:22:06] "GET /?oauth_token=72157720957970510-fcbf9a79c156140a&oauth_verifier=1bf80e1e3fa7797b HTTP/1.1" 200 -
You are now authenticated as f/5.6ish
Getting photo exif data from Flickr...
Photo dimensions in pixels: [3852, 4158]
Getting user groups from Flickr...
-- Adding random set of core film groups --
Adding photo to group: /r/analog...
Adding photo to group: ALL ABOUT FILM...
Adding photo to group: Film film...
Adding photo to group: Film is Awesome!...
Adding photo to group: Film photography (best works)...
Adding photo to group: Film Vision...
Adding photo to group: FILM....
Adding photo to group: Good photo,good details--Film preferred...
Adding photo to group: I (still) shoot FILM...
Adding photo to group: I Hate Digital!...
Adding photo to group: I Shoot Film...
FlickrError (in add_photo_to_group): Error: 6: Your Photo has been added to the Pending Queue for this Pool
Adding photo to group: Shooting Film...
Adding photo to group: This is why I love Film...
Adding photo to group: Upgrade to Film...
Adding photo to group: We Use Film...
-- Adding core tags --
Adding tag "Film is Not Dead"...
Adding tag "Film Photography"...
Adding tag "Shooting Film"...
Adding tag "Believe In Film"...
Adding tag "Essential Film Holder"...
Adding tag "Analogue Toolbox for Capture One"...
Adding tag "Film"...
Adding tag "Analogue"...
-- Adding film-related groups and tags --
Adding photo to group: Lomography Films...
Getting albums from Flickr...
-- Adding camera-related groups and tags --
Adding photo to group: Hasselblad...
Adding photo to group: Hasselblad 500 Series - film only...
FlickrError (in add_photo_to_group): Error: 6: Your Photo has been added to the Pending Queue for this Pool
Adding tag "Hasselblad"...
Adding tag "Hasselblad 503cx"...
Adding photo to album: Hasselblad 503cx...
-- Adding lens-related groups and tags --
Adding photo to group: Hasselblad 50mm Zeiss Distagon...
Adding tag "50mm Lens"...
Adding photo to album: Carl Zeiss Distagon 50mm f/4 CF FLE...
-- Adding derived groups and tags --
Adding photo to group: 120...
Adding photo to group: Medium Format (120/220 film only)...
Adding photo to group: Why I Love Medium Format - Film Only...
FlickrError (in add_photo_to_group): Error: 6: Your Photo has been added to the Pending Queue for this Pool
Adding tag "120 Film"...
Adding tag "Medium Format"...
Adding tag "Medium Format Film"...
Adding photo to group: 6x6 COLOR film...
```

#### Optional arguments

There are several optional argument that can be used with `—add`.

##### --digital

The `—digital` argument that can be added to the command line which bypasses the adding of the photo to the film-specific groups. 

##### --monochrome

The `—monochrome` argument indicates that the photo is monochrome but the original film stock was colour, so don’t add any self-developed tags or groups.

(See also the geo-tagging options that can also be used in-line with `—add`).

### Utility functions

Some of the functions are useful when developing or extending the code base.

#### --get_groups

The list of groups to add the photo to is hard-coded in the files `core_groups.py` and `add_utils.py`. To find out the group IDs of the groups that you’re a member of, use the `--get_groups` argument.

Example output:
```
./flickr_cli.py --get_groups
127.0.0.1 - - [02/Nov/2025 21:15:41] "GET /?oauth_token=72157720958005856-3caed90c68ddf5fd&oauth_verifier=69843454e7c0c2c2 HTTP/1.1" 200 -
You are now authenticated as f/5.6ish
Getting user groups from Flickr...
Group: !nto the atmosphere, id: 52879335@N00
Group: &quot;I&#039;ll Be Your Mirror&quot;, id: 14747291@N22
Group: &#039;Black and White&#039;  Creative Images!, id: 1575512@N25
Group: * PERCEPTION *, id: 14904281@N22
Group: * YELLOW on film *, id: 14805456@N23
Group: ***Are You Experienced°°°Film Only***, id: 14715564@N23
Group: *The Moody Moodpepper* ( Admin invite only), id: 14607726@N25
Group: // The One-Eyed Poet, id: 2170622@N23
Group: /r/analog, id: 2154336@N24
Group: 100 Strangers, id: 342582@N20
...
```
#### --get_tags

The `—get_tags` argument retrieves the list of tags currently added to a photo. It must be used with the `—id` argument to specify the photo ID on which to perform the operation.

Example output:
```
./flickr_cli.py --id 54893586132 --get_tags
127.0.0.1 - - [02/Nov/2025 21:20:04] "GET /?oauth_token=72157720958006216-54dad7d7556a0656&oauth_verifier=5923a0ab7a68b909 HTTP/1.1" 200 -
You are now authenticated as f/5.6ish
tag: Hayling Island
tag: England
tag: United Kingdom
tag: Kodak
tag: UltraMax 400
tag: Film is Not Dead
tag: Film Photography
tag: Shooting Film
tag: Believe In Film
tag: Essential Film Holder
tag: Analogue Toolbox for Capture One
tag: Film
tag: Analogue
tag: Olympus
tag: Olympus OM-1
tag: 28mm Lens
tag: 35mm Photography
tag: 35mm Film
```
### Geo-tagging

There are 2 functions that can be used to geo-tag the photos in Flickr.

#### --location

The `—location` argument can be used to geo-tag the photo based on a text string such as "Winchester cathedral" or “Southampton”. This uses the Here API, and so requires a valid here API key in the `keys.py` file.

#### --coords

The `—coords` argument can be used to geo-tag the photo based on NSEW-based latitude and longitude. For example when copied from a dropped pin in Apple Maps: `—coords "51.06612° N, 1.38359° W”`.

Both must be used with the `—id` argument to specify the photo ID on which to perform the operation.

Example output:
```
./flickr_cli.py --id 54898585845 --coords "51.06971° N, 1.39455° W"
127.0.0.1 - - [03/Nov/2025 11:31:12] "GET /?oauth_token=72157720958037565-0e7a26c6bed859b6&oauth_verifier=7c767e90f27abacc HTTP/1.1" 200 -
You are now authenticated as f/5.6ish
Setting location...
```

Either of these arguments can also be used in-line with the `—add` command as well.

### File uploads

The tool can be used to upload a file if the Flickr uploader is not used.

#### --upload

The `—upload` switch can be used along with `—file`, `—title` and `—description` to upload a file to Flickr.

Example output:
```
./flickr_cli.py --upload --file "/Users/pemcg/Exports/XT504090.jpg" --title "Shaded" --description "Hasselblad 503cx, Carl Zeiss Distagon 50mm f/4 CF FLE, Lomography CN400"
127.0.0.1 - - [03/Nov/2025 13:07:03] "GET /?oauth_token=72157720958040870-b0209ceec2d28d4f&oauth_verifier=e3bebb3d3731511 HTTP/1.1" 200 -
You are now authenticated as f/5.6ish
New photo id: 54898932289
```

### Group admin related functionality

As I’m the admin of 3 groups, I wrote some functions to get me some insight into the groups that I'm managing.

#### --get_group_photos

This is an argument to help with group admin activity. It requires the `—group` (current hardcoded as ‘hp5+', ‘delta3200’, or ‘wearenotdeadyet’ as these are the groups for which I’m admin), and `—days` which is the number of days to look back over. It prints a summary of the photos added to the group in the time period.

Example output:
```
./flickr_cli.py --get_group_photos --group 'delta3200' --days 5
127.0.0.1 - - [03/Nov/2025 09:28:57] "GET /?oauth_token=72157720957958057-395b94493e333ba4&oauth_verifier=a38d0ae31c10321c HTTP/1.1" 200 -
You are now authenticated as f/5.6ish
******************************************************************************************

- Photo ID: 54897836639
- User: thedamnedsins
- Title: Silence Within the Darkness
- Description: In the hush of shadowed realms, where light dares not intrude, there exists a silence more profound than absence—a stillness that listens, that remembers. 「闇の中の静寂」 speaks not merely of quietude, but of the soul’s retreat into the unseen, the unspoken.
Darkness is not the enemy of truth, but its cradle. In its embrace, we confront the impermanence of form, the echo of forgotten selves, and the quiet dignity of things left unsaid. Silence within the darkness is not void—it is potential. It is the breath before revelation, the pause that holds eternity.

- Tags:
FlickrError (in get_photo_exif): Error: 2: Permission denied
******************************************************************************************

- Photo ID: 5161892320
- User: Dominic Skathanas
- Title: Delta 3200
- Description: Femme fatal of my murder photoseries to the tune of film noir. It culminated with a picture of me, dead, in a pool of red acrylic paint.
- Tags:
    delta3200
- Exif Camera: Nikon Nikon COOLSCAN V ED
******************************************************************************************

- Photo ID: 52909599156
- User: chetbak59
- Title: le premier jour, de tous les autres
- Description: m6 delta 3200
- Tags:
    argentique
    leica
    film
    noir
    analogique
    ilford
******************************************************************************************

- Photo ID: 54894291026
- User: mind-boggled
- Title: A place that does not welcome lingering
- Description: Ilford Delta 3200 shot with a Olympus Pen-FT, using a 20mm.
- Tags:
    ilford
    film
    analogue
    olympuspen
    olympus
    ominous
    creepy
    mall
    old
    atmosphere
    vintage
    liminal
    hall
    empty
    lifeless
    3200
    dark
    gloomy
    eerie
    monochrome
- Exif Camera: Plustek OpticFilm 8200i
******************************************************************************************
...
```
#### --get_user_groups_with_admin_activity

This function is useful to see which groups that you’re are a member of are administratively ‘dormant’, i.e. have had no activity from any group admin for a number of weeks/months/years. It iterates through all of your groups, look up the group admins, and looks to see of each admin has either posted or faved anything in the previous specified number of days. This argument requires the additional argument `—days`.

Example output:
```
./flickr_cli.py --get_user_groups_with_admin_activity --days 365
127.0.0.1 - - [03/Nov/2025 13:19:40] "GET /?oauth_token=72157720957965717-40fb01a03280687e&oauth_verifier=f3c980e3ae066114 HTTP/1.1" 200 -
You are now authenticated as f/5.6ish
Getting user groups from Flickr...
Group: !nto the atmosphere, id: 52879335@N00
    Admin id: 28371556@N06, name: pierre-vdm, last 365 day photo count: 12, last 365 day fave count: 50
    Admin id: 90463792@N00, name: ribena_wrath, last 365 day photo count: 0, last 365 day fave count: 0
Group: &quot;I&#039;ll Be Your Mirror&quot;, id: 14747291@N22
    Admin id: 8188344@N02, name: Gianni Mazzarelli, last 365 day photo count: 4, last 365 day fave count: 4478
    Admin id: 187315775@N03, name: gianni.mazzarelli, last 365 day photo count: 0, last 365 day fave count: 0
Group: &#039;Black and White&#039;  Creative Images!, id: 1575512@N25
    Admin id: 185379416@N07, name: Gentleman C.B., last 365 day photo count: 2, last 365 day fave count: 8
    Admin id: 164652074@N05, name: Cadence and Craig Abbot Creative Photography, last 365 day photo count: 9, last 365 day fave count: 340
    Admin id: 130128901@N07, name: Chatwick University Criminology Department, last 365 day photo count: 4, last 365 day fave count: 32
    Admin id: 55482661@N06, name: J-Mi & F (Josef & Josef@ K), last 365 day photo count: 0, last 365 day fave count: 0
    Admin id: 12349220@N00, name: jean sept, last 365 day photo count: 0, last 365 day fave count: 3
    Admin id: 36240071@N07, name: NormaN Tacchi, last 365 day photo count: 0, last 365 day fave count: 0
    Admin id: 62602097@N00, name: Novowyr, last 365 day photo count: 0, last 365 day fave count: 702
    Admin id: 149057579@N04, name: philippephotography1, last 365 day photo count: 0, last 365 day fave count: 3
    Admin id: 128363297@N02, name: Bernd Kretzer, last 365 day photo count: 0, last 365 day fave count: 793
    Admin id: 35968016@N03, name: Lux Ludos, last 365 day photo count: 41, last 365 day fave count: 1119
    Admin id: 138943594@N08, name: Sundance Photos, last 365 day photo count: 0, last 365 day fave count: 3
    Admin id: 138748223@N07, name: Rouge France, last 365 day photo count: 0, last 365 day fave count: 0
    Admin id: 125216791@N07, name: *ines_maria, last 365 day photo count: 5, last 365 day fave count: 7589
    Admin id: 70626035@N00, name: jacilluch, last 365 day photo count: 0, last 365 day fave count: 0
    Admin id: 49864218@N07, name: DirkBee, last 365 day photo count: 117, last 365 day fave count: 95
    Admin id: 58555558@N07, name: Jim Archer, last 365 day photo count: 0, last 365 day fave count: 0
...
```

#### --get_user_groups_with_no_admin_activity

This is a companion function to the above, but only lists groups (that you’re a member of) where none of the group admins have displayed any posting or fave activity in the specified number of days. This is useful in case you feel the need to contact Flickr admins and request a takeover of the admin role for the group.

Example output:
```
./flickr_cli.py --get_user_groups_with_no_admin_activity --days 365
127.0.0.1 - - [03/Nov/2025 13:16:53] "GET /?oauth_token=72157720958019914-2bab487931820bb5&oauth_verifier=5440ce2a58df5739 HTTP/1.1" 200 -
You are now authenticated as f/5.6ish
Getting user groups with no recent admin activity from Flickr...
Group: 28mm is my Favorite, id: 1175002@N21
 -- admin name: Alice Nggan
Group: 35mm blackandwhite, id: 57796404@N00
 -- admin name: timx
Group: 645 Medium Format, id: 304405@N25
 -- admin name: petros_canon
Group: Acros, id: 32685380@N00
 -- admin name: rich8155 (Richard Sintchak)
Group: ALL ABOUT FILM, id: 586170@N24
 -- admin name: The Dalai Lomo
Group: All Things Film, id: 1045471@N24
 -- admin name: omatix
Group: Analog Soul, id: 1086616@N22
 -- admin name: ledh
 -- admin name: supersteady
 -- admin name: porkscrew
Group: anti paradise, id: 1841895@N25
 -- admin name: amaiamolinet.com
Group: BelieveInFilm.com, id: 1690604@N25
 -- admin name: believeinfilm
Group: Berlin Analog, id: 12632627@N00
 -- admin name: tilde~
Group: Bessa R, id: 777631@N25
 -- admin name: p h o n g s [ Oิ']
```
#### --get_group_members_with_recent_activity

This function looks to see which of the group’s member are still active, i.e have posted or faved anything in the previous specified number of days. Useful to see if (for example) a group has 4000 members, but only 500 are active on Flickr.
This function takes a long time to run as it’s self-limiting to comply with the Flickr API guidelines for the number of API calls/hour made. The group names are hard-coded for my convenience and translated to their corresponding group ID in a hash.

Example output:
```
./flickr_cli.py --get_group_members_with_recent_activity --group 'wearenotdeadyet' --days 120
127.0.0.1 - - [03/Nov/2025 13:29:06] "GET /?oauth_token=72157720958041975-85564b11295ff675&oauth_verifier=b560734df0fd648b HTTP/1.1" 200 -
You are now authenticated as f/5.6ish
Getting group members with recent activity from Flickr, starting at 13:29:07...
Processed 30 members, found 24 active members so far... 13:30:49
Processed 60 members, found 52 active members so far... 13:32:11
Processed 90 members, found 73 active members so far... 13:33:31
Processed 120 members, found 93 active members so far... 13:34:50
...
```