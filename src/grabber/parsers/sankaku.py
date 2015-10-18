import re

test_page = url = 'https://chan.sankakucomplex.com/?tags=angelise_ikaruga_misurugi+official_art&commit=Search'

import grabber.parsers.common as common


# from pprint import pprint



class SankakuParser(object):

    def __init__(self):
        pass

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


class SearchParser(object):
    __text = None

    __del_regex = None

    def __init__(self):
        self.__text = None

        self.__del_regex = re.compile(DEL_REGEX, re.DOTALL)
        self.__post_regex = re.compile(POST_REGEX)
        self.__next_regex = re.compile(NEXT_REGEX)

    def make_query(self, tags):
        # trim tags according to limit
        tags_ = tags[0:TAG_MAX]
        tags_str = TAG_SEP.join(tags_)

        result_str = QUERY_PREFIX + tags_str + QUERY_SUFFIX
        return result_str

    def feed(self, text):
        # its not my fault, thats my posts aren't popular
        # delete POLULAER section
        if self.__del_regex.search(text):
            text_clear = re.sub(self.__del_regex, '###UNPOPULAR###', text)
            self.__text = text_clear
        else:
            self.__text = text

    def parse(self):
        result = {
            'posts': [],
            'next': None
        }

        if self.__next_regex.search(self.__text):
            next_page = self.__next_regex.findall(self.__text)[0]
            result['next'] = 'https://chan.sankakucomplex.com' + next_page

        if self.__post_regex.search(self.__text):
            posts = self.__post_regex.findall(self.__text)

            header_posts = list(
                map(lambda u: 'https://chan.sankakucomplex.com' + u, posts)
            )

            result['posts'] = header_posts

        return result


TAGS_REGEX = '<li class=tag-type-[^ ]*?><a href="/[?]tags=([^ ]*?)"'
PIC_ORIG_REGEX = '<li>Original: <a href="(//cs.sankakucomplex.com/data/[^ ]{2}/[^ ]{2}/[^ ]*?.(?:jpg|png|gif|webm))\\?\d+?" id=highres itemprop=contentUrl title="[^ ].*?">[^ ].*?</a></li>'
PIC_RESIZE_REGEX = '<li>Resized: <a href="(//cs.sankakucomplex.com/data/sample/[^ ]{2}/[^ ]{2}/sample-[^ ]*?[.](?:jpg|png|gif))[?]\d+?" id=lowres>\d+?x\d+?</a></li>'
RATING_REGEX = '<li>Rating:\s([^ ]*?)</li>'


class PostParser(object):
    __text = None

    __tags_re = None
    __original_re = None
    __resized_re = None
    __rating_re = None

    def __compile_regex(self):
        self.__tags_re = re.compile(TAGS_REGEX)
        self.__original_re = re.compile(PIC_ORIG_REGEX)
        self.__resized_re = re.compile(PIC_RESIZE_REGEX)
        self.__rating_re = re.compile(RATING_REGEX)

    def __init__(self):
        self.__text = None
        self.__compile_regex()

    def feed(self, text):
        self.__text = text

    def parse(self, flags=None):
        if flags == None:
            flags = {
                'tags': True,
                'original': True,
                'resized': True,
                'rating': True,
            }

        result = {}

        if flags['tags']:
            if self.__tags_re.search(self.__text):
                tags = self.__tags_re.findall(self.__text)
                result['tags'] = tags
            else:
                result['tags'] = None

        result['pics'] = []
        if flags['original']:
            if self.__original_re.search(self.__text):
                orig = self.__original_re.findall(self.__text)[0]
                orig = 'https:' + orig
                result['pics'].append(orig)

        if flags['resized']:
            if self.__resized_re.search(self.__text):
                res = self.__resized_re.findall(self.__text)[0]
                res = 'https:' + res
                result['pics'].append(res)

        if flags['rating']:
            if self.__rating_re.search(self.__text):
                rating = self.__rating_re.findall(self.__text)[0]
                if rating == 'Safe':
                    result['rating'] = common.RATING_SAFE
                elif rating == 'Questionable':
                    result['rating'] = common.RATING_QUESTIONABLE
                elif rating == 'Explicit':
                    result['rating'] = common.RATING_EXPLICIT
            else:
                result['rating'] = None
        return result

# GENERAL
NAME = 'sankaku'
DESCRIPTION = 'Sankaku Channel booru config'





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


