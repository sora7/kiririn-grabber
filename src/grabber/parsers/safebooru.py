#general
NAME = 'safebooru'
DESCRIPTION = 'stub template for Safebooru'

#query
QUERY_URL = 'https://chan.sankakucomplex.com/?tags='
# QUERY_URL = '/?tags=%s&commit=Search'
TAG_SEP = '+'

# search parse
DEL_REGEX = '<div class=popular-preview-post>(.+?)</div>'

NEXT_REGEX = '<div next-page-url="(/[?]next=.+)">'
NEXT_PREFIX = 'https://chan.sankakucomplex.com'

POST_REGEX = 'href="(/post/show/\d+)"'
POST_PREFIX = 'https://chan.sankakucomplex.com'

#post parse
POST_ID_REGEX = '<h1 id=site-title><a href="/">Sankaku Channel</a>/<a href="/post/show/\d+?">Post (\d+?)</a>'
TAGS_REGEX = '<li class=tag-type-[^ ]*?><a href="/[?]tags=([^ ]*?)"'

POSTED_REGEX = 'Posted: <a href="/[?]tags=date%3A\d{4}-\d{2}-\d{2}" title="(.+?)">.+?</a>'
POSTED_AGO_REGEX = 'Posted: <a href="/[?]tags=date%3A\d{4}-\d{2}-\d{2}" title=".+?">(.+?)</a>'

PIC_RESIZE_REGEX = '<li>Resized: <a href="(//cs.sankakucomplex.com/data/sample/[^ ]{2}/[^ ]{2}/sample-[^ ]*?[.](?:jpg|png))[?]\d+?" id=lowres>\d+?x\d+?</a></li>'
PIC_RESIZE_RES_REGEX = '<li>Resized: <a href="//cs.sankakucomplex.com/data/sample/[^ ]{2}/[^ ]{2}/sample-[^ ]*?[.](?:jpg|png)[?]\d+?" id=lowres>(\d+?x\d+?)</a></li>'
PIC_RESIZE_PREFIX = 'https:'

PIC_ORIG_REGEX = '<li>Original: <a href="(//cs.sankakucomplex.com/data/[^ ]{2}/[^ ]{2}/[^ ]*?.(?:jpg|png))\\?\d+?" id=highres itemprop=contentUrl title="[^ ].*?">[^ ].*?</a></li>'
PIC_ORIG_RES_REGEX = '<li>Original: <a href="//cs.sankakucomplex.com/data/[^ ]{2}/[^ ]{2}/[^ ]*?.(?:jpg|png)\\?\d+?" id=highres itemprop=contentUrl title="[^ ].*?">([^ ].*?)</a></li>'
PIC_ORIG_SIZE_REGEX = '<li>Original: <a href="//cs.sankakucomplex.com/data/[^ ]{2}/[^ ]{2}/[^ ]*?.(?:jpg|png)\\?\d+?" id=highres itemprop=contentUrl title="([^ ].*?)">[^ ].*?</a></li>'
PIC_ORIG_PREFIX = 'https:'

RATING_REGEX = '<li>Rating:\s([^ ]*?)</li>'



