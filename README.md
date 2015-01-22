# kiririn-grabber

Picture grabber for sites on Danbooru engine and other

This is the very first "working" version. It can parse tag results from only
one site (chan.sankakucomplex.com aka SankakuChannel), and can't download files
(but create a .txt file with the direct links to pictures). You can use your
favorite download manager or even DownThemAll Firefox Extension (recommended).

Xample usage:

    kiririn.py -s sankaku -t tag1 tag2 more_tag

Good for POSIX-linux, but on Windows there are some troubles with redirecting
command line arguments from Python interpreter to script. Use the kiririn.bat
instead:

    kiririn.bat -s sankaku -t tag1 tag2 more_tag

this will find pics on SankakuChannel for "tag1" and "tag" and "more_tag" tags
and create file:

     "sankaku_tag1_tag2_more_tag.txt"

with direct links to pics.

Nesessary keys:
-------

    -s, --site
Site where you want to find (and load) pics

    -t, --tags
List of tags you want to load. Note that this must be the LAST key

Optional keys:
-------

    -c, --continue
Continue processing the job. You can break/continue any time (search or posts
processing).

    -o, --original
Load original pics only (but not resized). By default, grabber load almost all
pics.

    -r, --resized
Load resized pics only (if any). By default, grabber load almost all pics.

Other info:

Approximate list of booru kiririn can grab pics from:

SankakuChannel

Danbooru

Gelbooru (fucking ads)

Safebooru

Yande.re

Konachan

vocalo.booru.org

Zerochan (some troubles with JS)

idol.sankakucomplex.com (yes, 3DPD)

Requirements
-------

There's no special platform or system requirements, but python3. Tested on
windows, possibly will work on linux.

