'''
Created on 13.12.2014
'''

#general
NAME = 'sankaku'
DESCRIPTION = 'Sankaku Channel booru config'

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

PIC_RESIZE_REGEX = '<li>Resized: <a href="(//cs.sankakucomplex.com/data/sample/[^ ]{2}/[^ ]{2}/sample-[^ ]*?[.](?:jpg|png|gif))[?]\d+?" id=lowres>\d+?x\d+?</a></li>'
PIC_RESIZE_RES_REGEX = '<li>Resized: <a href="//cs.sankakucomplex.com/data/sample/[^ ]{2}/[^ ]{2}/sample-[^ ]*?[.](?:jpg|png|gif)[?]\d+?" id=lowres>(\d+?x\d+?)</a></li>'
PIC_RESIZE_PREFIX = 'https:'

PIC_ORIG_REGEX = '<li>Original: <a href="(//cs.sankakucomplex.com/data/[^ ]{2}/[^ ]{2}/[^ ]*?.(?:jpg|png|gif))\\?\d+?" id=highres itemprop=contentUrl title="[^ ].*?">[^ ].*?</a></li>'
PIC_ORIG_RES_REGEX = '<li>Original: <a href="//cs.sankakucomplex.com/data/[^ ]{2}/[^ ]{2}/[^ ]*?.(?:jpg|png|gif)\\?\d+?" id=highres itemprop=contentUrl title="[^ ].*?">([^ ].*?)</a></li>'
PIC_ORIG_SIZE_REGEX = '<li>Original: <a href="//cs.sankakucomplex.com/data/[^ ]{2}/[^ ]{2}/[^ ]*?.(?:jpg|png|gif)\\?\d+?" id=highres itemprop=contentUrl title="([^ ].*?)">[^ ].*?</a></li>'
PIC_ORIG_PREFIX = 'https:'

RATING_REGEX = '<li>Rating:\s([^ ]*?)</li>'

booru_data = {
    'QUERY_PREFIX' : 'https://chan.sankakucomplex.com/?tags=',
    'TAG_SEP' : '+',
    #search
    #if we want to del smtng before grab posts ('popular' section on sankakuclannel for example)
    'DEL_TEXT' : True,
    'DEL_REGEX' : '<div class=popular-preview-post>(.+?)</div>',

    'NEXT_REGEX' : '<div next-page-url="(/[?]next=.+)">',
    'NEXT_PREFIX' : 'https://chan.sankakucomplex.com',

    'POST_REGEX' : 'href="(/post/show/\d+)"',
    'POST_PREFIX' : 'https://chan.sankakucomplex.com',
    #post
    'POST_ID_REGEX' : '<h1 id=site-title><a href="/">Sankaku Channel</a>/<a href="/post/show/\d+?">Post (\d+?)</a>',
    'TAGS_REGEX' : '<li class=tag-type-[^ ]*?><a href="/[?]tags=([^ ]*?)"',

    'POSTED_REGEX' : 'Posted: <a href="/[?]tags=date%3A\d{4}-\d{2}-\d{2}" title="(.+?)">.+?</a>',
    'POSTED_AGO_REGEX' : 'Posted: <a href="/[?]tags=date%3A\d{4}-\d{2}-\d{2}" title=".+?">(.+?)</a>',

    'PIC_RESIZE_REGEX' : '<li>Resized: <a href="(//cs.sankakucomplex.com/data/sample/[^ ]{2}/[^ ]{2}/sample-[^ ]*?[.](?:jpg|png|gif))[?]\d+?" id=lowres>\d+?x\d+?</a></li>',
    'PIC_RESIZE_RES_REGEX' : '<li>Resized: <a href="//cs.sankakucomplex.com/data/sample/[^ ]{2}/[^ ]{2}/sample-[^ ]*?[.](?:jpg|png|gif)[?]\d+?" id=lowres>(\d+?x\d+?)</a></li>',
    'PIC_RESIZE_PREFIX' : 'https:',

    'PIC_ORIG_REGEX' : '<li>Original: <a href="(//cs.sankakucomplex.com/data/[^ ]{2}/[^ ]{2}/[^ ]*?.(?:jpg|png|gif))\\?\d+?" id=highres itemprop=contentUrl title="[^ ].*?">[^ ].*?</a></li>',
    'PIC_ORIG_RES_REGEX' : '<li>Original: <a href="//cs.sankakucomplex.com/data/[^ ]{2}/[^ ]{2}/[^ ]*?.(?:jpg|png|gif)\\?\d+?" id=highres itemprop=contentUrl title="[^ ].*?">([^ ].*?)</a></li>',
    'PIC_ORIG_SIZE_REGEX' : '<li>Original: <a href="//cs.sankakucomplex.com/data/[^ ]{2}/[^ ]{2}/[^ ]*?.(?:jpg|png|gif)\\?\d+?" id=highres itemprop=contentUrl title="([^ ].*?)">[^ ].*?</a></li>',
    'PIC_ORIG_PREFIX' : 'https:',

    'PIC_ORIG2' : False,
    'PIC_ORIG_REGEX2' : '',
    'PIC_ORIG_RES_REGEX2' : '',
    'PIC_ORIG_SIZE_REGEX2' : '',
    'PIC_ORIG_PREFIX2' : '',

    'RATING_REGEX' : '<li>Rating:\s([^ ]*?)</li>'
}

