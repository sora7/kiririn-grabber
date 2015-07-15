class SankakuParser(object):

    def __init__(self):
        pass

# GENERAL
NAME = 'sankaku'
DESCRIPTION = 'Sankaku Channel booru config'

# QUERY
QUERY_PREFIX = 'https://chan.sankakucomplex.com/?tags='
TAG_SEP = '+'
QUERY_SUFFIX = '&commit=Search'
TAG_MAX = 4

# SEARCH
# if we want to del smtng before grab posts ('popular' section on sankakuclannel for example)
DEL_TEXT = True
DEL_REGEX = '<div class=popular-preview-post>(.+?)</div>.</div>.</div>'
# *nesessary
NEXT_REGEX = '<div next-page-url="(/[?](?:next=\d*?(?:&|&amp;)){0,1}tags=.*?(?:&|&amp;)page=\d*?)">'
NEXT_PREFIX = 'https://chan.sankakucomplex.com'
# *nesessary
POST_REGEX = 'href="(/post/show/\d+)"'
POST_PREFIX = 'https://chan.sankakucomplex.com'

# POST
POST_ID_REGEX = '<h1 id=site-title><a href="/">Sankaku Channel</a>/<a href="/post/show/\d+?">Post (\d+?)</a>'
TAGS_REGEX = '<li class=tag-type-[^ ]*?><a href="/[?]tags=([^ ]*?)"'

POSTED_REGEX = 'Posted: <a href="/[?]tags=date%3A\d{4}-\d{2}-\d{2}" title="(.+?)">.+?</a>'
POSTED_AGO_REGEX = 'Posted: <a href="/[?]tags=date%3A\d{4}-\d{2}-\d{2}" title=".+?">(.+?)</a>'

# *nesessary
PIC_RESIZE_REGEX = '<li>Resized: <a href="(//cs.sankakucomplex.com/data/sample/[^ ]{2}/[^ ]{2}/sample-[^ ]*?[.](?:jpg|png|gif))[?]\d+?" id=lowres>\d+?x\d+?</a></li>'
PIC_RESIZE_RES_REGEX = '<li>Resized: <a href="//cs.sankakucomplex.com/data/sample/[^ ]{2}/[^ ]{2}/sample-[^ ]*?[.](?:jpg|png|gif)[?]\d+?" id=lowres>(\d+?x\d+?)</a></li>'
# *nesessary
PIC_RESIZE_PREFIX = 'https:'

# *nesessary
PIC_ORIG_REGEX = '<li>Original: <a href="(//cs.sankakucomplex.com/data/[^ ]{2}/[^ ]{2}/[^ ]*?.(?:jpg|png|gif))\\?\d+?" id=highres itemprop=contentUrl title="[^ ].*?">[^ ].*?</a></li>'
PIC_ORIG_RES_REGEX = '<li>Original: <a href="//cs.sankakucomplex.com/data/[^ ]{2}/[^ ]{2}/[^ ]*?.(?:jpg|png|gif)\\?\d+?" id=highres itemprop=contentUrl title="[^ ].*?">([^ ].*?)</a></li>'
PIC_ORIG_SIZE_REGEX = '<li>Original: <a href="//cs.sankakucomplex.com/data/[^ ]{2}/[^ ]{2}/[^ ]*?.(?:jpg|png|gif)\\?\d+?" id=highres itemprop=contentUrl title="([^ ].*?)">[^ ].*?</a></li>'
# *nesessary
PIC_ORIG_PREFIX = 'https:'

# some booru (konachan) have 2 original pictures (png and jpg)
PIC_ORIG2 = False
# *nesessary
PIC_ORIG2_REGEX = ''
PIC_ORIG2_RES_REGEX = ''
PIC_ORIG2_SIZE_REGEX = ''
# *nesessary
PIC_ORIG2_PREFIX = ''

RATING_REGEX = '<li>Rating:\s([^ ]*?)</li>'


