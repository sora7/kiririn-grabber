# Kiririn-grabber

Picture grabber for sites on Danbooru engine and other (see [list](#booru_supported) below).

## USAGE

###GUI


###CLI
Or Command Line Interface. Open a console in a folder with kiririn and
type:

    kiririn-cli.py -s %booru_name% -t %tag1% %tag2%

where: 
* %booru_name% - alias for booru (see [list](#booru_supported))
* %tag1% %tag2% - tags you want to load.

Xample usage:

    kiririn-cli.py -s sankaku -t tag1 tag2 more_tag

Good for POSIX-linux, but on Windows there are some troubles with redirecting
command line arguments from Python interpreter to script. Use the kiririn.bat
instead:

    kiririn-cli.bat -s sankaku -t tag1 tag2 more_tag

this will find pics on SankakuChannel for "tag1" and "tag" and "more_tag" tags
and download them.

##KEYS

###Main

    -s, --site
Site where you want to find (and load) pics. If argument doesn't given it
print [list](#booru_supported) of supported booru.

    -t, --tags
List of tags you want to load. Note that this must be the **last** key 
(everything after -t or --tags grabber will understand as tags). Every booru
has restrictions in maximum tag count (for anonymous mode), overlimit tags 
will be discarded.

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

## OTHER

###Supported Booru List: <a id="booru_supported"></a>

Booru                                             |Alias   |Original|Resized|Tag limit 
--------------------------------------------------|--------|--------|-------|----------
[SankakuChannel](https://chan.sankakucomplex.com) |sankaku |yes     |yes    |4

###Booru List:

Approximate list of booru kiririn can grab pics from
(it's only declared functionality, not implemented yet):

Booru                                             |Original|Resized|Tag limit|Comment 
--------------------------------------------------|--------|-------|---------|--------
[SankakuChannel](https://chan.sankakucomplex.com) |yes     |yes    |4        |
[SankakuIdol](https://idol.sankakucomplex.com)    |yes     |yes    |4        |yes, 3DPD
[Danbooru](https://danbooru.donmai.us/)           |yes     |yes    |2        |
[Gelbooru](http://gelbooru.com/)                  |yes     |yes    |inf      |fucking ads
[Safebooru](http://safebooru.org/)                |yes     |yes    |inf      |
[Yande.re](https://yande.re)                      |yes*    |yes    |6        |
[Konachan](http://konachan.com/)                  |yes*    |yes    |6        |
[Zerochan](http://www.zerochan.net/)              |yes     |yes    |inf      |some troubles with JS
[Vocaloid and Utau](http://vocalo.booru.org)      |yes     |no     |inf      |
[4chanhouse.org](http://shimmie.4chanhouse.org/)  |yes     |no     |inf      |     
[katawa-shoujo](http://shimmie.katawa-shoujo.com/)|yes     |no     |inf      |

*2 original pictures in PNG and JPG

###Future features:

* [DONE] graphical user interface (using Tk or ttk)


## REQUIREMENTS

There's no special platform or system requirements, but python3. Tested on
windows, possibly will work on linux.

