# GENERAL
NAME = 'konachan'
DESCRIPTION = 'Konachan booru config'

# QUERY
QUERY_PREFIX = 'http://konachan.com/post?tags='
TAG_SEP = '+'
QUERY_SUFFIX = ''
TAG_MAX = 6

# SEARCH
#if we want to del smtng before grab posts ('popular' section on sankakuclannel for example)
DEL_TEXT = False
DEL_REGEX = ''

NEXT_REGEX = ''
NEXT_PREFIX = ''

POST_REGEX = ''
POST_PREFIX = ''

# POST
POST_ID_REGEX = '<li>Id: (\d*?)</li>'
TAGS_REGEX = '<li class="tag-link tag-type.*?" data-name="(.*?)" data-type=".*?"'

# <li>Posted: <a href="/post?tags=date%3A2014-08-26" title="Tue Aug 26 06:53:57 2014">6 months ago</a> by <a href="/user/show/73493">kamenitza</a></li>
# <li>Posted: <a href="/post?tags=date%3A2014-04-26" title="Sat Apr 26 13:10:36 2014">10 months ago</a> by <a href="/user/show/20645">Wiresetc</a></li>

POSTED_REGEX = '<li>Posted: <a href=".*?" title="(.*?)">.*?</a> by <a href="/user/show/\d*?">.*?</a></li>'
POSTED_AGO_REGEX = '<li>Posted: <a href=".*?" title=".*?">(.*?)</a> by <a href="/user/show/\d*?">.*?</a></li>'

PIC_RESIZE_REGEX = '<img alt=".*?".*?class="image".*?id="image".*?src="(http://konachan.com/.*?/Konachan.com.*?[.].{3})".*?>'
PIC_RESIZE_RES_REGEX = ''

PIC_RESIZE_PREFIX = ''

PIC_ORIG_REGEX = '<li><a class="original-file-changed" href="(http://konachan.com/[^ ]*?/[^ ]*?)" id="highres">Download larger version [(].*? [KM]B.*?[)]</a>'
PIC_ORIG_RES_REGEX = ''
PIC_ORIG_SIZE_REGEX = '<li><a class="original-file-changed" href="http://konachan.com/[^ ]*?/[^ ]*?" id="highres">Download larger version [(](.*? [KM]B).*?[)]</a>'
PIC_ORIG_PREFIX = ''

PIC_ORIG2 = True
PIC_ORIG2_REGEX = '<li><a class="original-file-unchanged" href="(http://konachan.com/image/[^ ]*?/[^ ]*?)".*?[(].*? [KM]B.*?[)]</a>'
PIC_ORIG2_RES_REGEX = ''
PIC_ORIG2_SIZE_REGEX = '<li><a class="original-file-unchanged" href="http://konachan.com/image/[^ ]*?/[^ ]*?".*?[(](.*? [KM]B).*?[)]</a>'
PIC_ORIG2_PREFIX = ''

RATING_REGEX = '<li>Rating: ([^ ]*?) <span class="vote-desc"></span></li>'

