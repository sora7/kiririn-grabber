#general
NAME = 'konachan'
DESCRIPTION = 'stub template for Konachan.com'

#query
QUERY_URL = 'https://chan.sankakucomplex.com/?tags='
# QUERY_URL = '/?tags=%s&commit=Search'
TAG_SEP = '+'

# search parse
DEL_REGEX = ''

NEXT_REGEX = ''
NEXT_PREFIX = ''

POST_REGEX = ''
POST_PREFIX = ''

#post parse
POST_ID_REGEX = ''
TAGS_REGEX = ''

POSTED_REGEX = ''
POSTED_AGO_REGEX = ''

PIC_RESIZE_REGEX = '<img alt=".*?" class="image" height="\d*?" id="image" large_height="\d*?" large_width="\d*?" src="(http://konachan.com/image/[a-z0-9]{32}/Konachan.com.*?.(?:jpg|png))" width="\d*?" />'

PIC_RESIZE_RES_REGEX = '<img alt=".*?" class="image" height="\d*?" id="image" large_height="\d*?" large_width="\d*?" src="(http://konachan.com/image/[a-z0-9]{32}/Konachan.com.*?.(?:jpg|png))" width="\d*?" />'
PIC_RESIZE_PREFIX = ''

PIC_ORIG_REGEX = ''
PIC_ORIG_RES_REGEX = ''
PIC_ORIG_SIZE_REGEX = ''
PIC_ORIG_PREFIX = ''

RATING_REGEX = '<li>Rating:\s([^ ]*?)</li>'



