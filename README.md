# Kiririn-grabber

Picture grabber for sites on Danbooru engine and other (see list below).

This is the very first "working" version. It still can't download pictures
(but create a .txt file with the direct links to pictures). You can use your
favorite download manager or even [DownThemAll](http://www.downthemall.net/) Firefox Extension (recommended).

## USAGE

CLI or Command Line Interface. Open a console in a folder with kiririn and 
type:

    kiririn.py -s %booru_name% -t %tag1% %tag2%

where %booru_name% - alias for booru (see [list](###Supported Booru List))
%tag1% %tag2% - tags you want to load.

Xaple usage:

    kiririn.py -s sankaku -t tag1 tag2 more_tag

Good for POSIX-linux, but on Windows there are some troubles with redirecting
command line arguments from Python interpreter to script. Use the kiririn.bat
instead:

    kiririn.bat -s sankaku -t tag1 tag2 more_tag

this will find pics on SankakuChannel for "tag1" and "tag" and "more_tag" tags
and create file:

     "sankaku_tag1_tag2_more_tag_PICS.txt"

with direct links to pics.

##KEYS

###Main

    -s, --site
Site where you want to find (and load) pics. If argument doesn't given it
print list of supported booru.

    -t, --tags
List of tags you want to load. Note that this must be the **last** key 
(everything after -t or --tags grabber will understand as tags).

###Optional

As i said before, these keys have to be typed before -t (--tags) key.

    -c, --continue
Continue processing the job. You can break/continue any time (search or posts
processing).

    -o, --original
Load original pics only (but not resized). By default, grabber load almost
all pics.

    -r, --resized
Load resized pics only (if any). By default, grabber load almost all pics.

    -l, --list-add
Append posts urls from .txt file and start process.
Example:
    kiririn.py -s sankaku -l posts_sankaku.txt

## OTHER

###Supported Booru List:

    Booru   |   Alias
    --------|---------
    [SankakuChannel](https://chan.sankakucomplex.com)  |   sankaku
    --------|---------
    [Konachan.com](https://konachan.com)    |   konachan

###Booru List:

Approximate list of booru kiririn can grab pics from
(it's only declared functionality, not implemented yet):

####Danbooru-like:

* SankakuChannel
* idol.sankakucomplex.com (yes, 3DPD)
* Danbooru
* Gelbooru (fucking ads)
* Safebooru
* Yande.re
* Konachan
* vocalo.booru.org
* Zerochan (some troubles with JS)

####Non-danbooru:

* shimmie.4chanhouse.org
* shimmie.katawa-shoujo.com

## REQUIREMENTS

There's no special platform or system requirements, but python3. Tested on
windows, possibly will work on linux.

