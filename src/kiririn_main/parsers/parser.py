import re
import os
import configparser

from kiririn_main.containers import SearchInfo
from kiririn_main.containers import PostInfo

from kiririn_main.parsers.sankaku import *


def query_url(tags):
    tags_str = TAG_SEP.join(tags)
    query = QUERY_URL + tags_str

    return query

def parse_search(text):
    answer = SearchInfo()

    # i'ts not my fault thats my posts aren't popular
    # lets delete the popular section
    p = re.compile(DEL_REGEX, re.DOTALL)
    if p.search(text):
        text = re.sub(p, '###UNPOPULAR###', text)

    # find the next page url (if any)
    p = re.compile(NEXT_REGEX)
    if p.search(text):
        next_page = p.findall(text)[0]

        answer.has_next = True
        answer.next = NEXT_PREFIX + next_page
        # print(answer.next)
    else:
        answer.has_next = False

    # find teh posts
    p = re.compile(POST_REGEX)
    if p.search(text):
        posts_raw = p.findall(text)

        posts = list(map(lambda item: POST_PREFIX + item, posts_raw))

        answer.has_posts = True
        answer.posts = posts
    else:
        answer.has_posts = False

    return answer


def parse_post(text):
    answer = PostInfo()

    # find post id
    p = re.compile(POST_ID_REGEX)
    if p.search(text):
        post_id = p.findall(text)[0]
        answer.post_id = post_id
    else:
        print('fuck id')

    # extract tags
    p = re.compile(TAGS_REGEX)
    if p.search(text):
        tags = p.findall(text)
        answer.tags = tags
    else:
        print('fuck tags')

    # extract datetime when posted
    p = re.compile(POSTED_REGEX)
    if p.search(text):
        posted = p.findall(text)[0]
        answer.posted = posted
    else:
        print('fuck dt')

    p = re.compile(POSTED_AGO_REGEX)
    if p.search(text):
        posted_ago = p.findall(text)[0]
        answer.posted_ago = posted_ago
    else:
        print('fuck dt ago')

    # extract resized pic and info
    p = re.compile(PIC_RESIZE_REGEX)
# <li>Resized: <a href="//cs.sankakucomplex.com/data/sample/23/cd/sample-23cdac5ea491397b448a301e5a36dee9.jpg?3586117" id=lowres>705x1000</a></li>
#     '<li>Resized: <a href="(//cs.sankakucomplex.com/data/sample/\d{2}/\d{2}/sample-[^ ]*?[.](?:jpg|png))[?]\d+?" id=lowres>\d+?x\d+?</a></li>'
#     p = re.compile('<li>Resized: <a href="(//cs.sankakucomplex.com/data/sample/[^ ]{2}/[^ ]{2}/sample-[^ ]*?[.](?:jpg|png))[?]\d+?" id=lowres>\d+?x\d+?</a></li>')
    if p.search(text):
        resized_link = p.findall(text)[0]
        resized_link = PIC_RESIZE_PREFIX + resized_link
        answer.has_resized = True
        answer.resized_link = resized_link
    else:
        print('fuck res')

    p = re.compile(PIC_RESIZE_RES_REGEX)
    if p.search(text):
        resized_res = p.findall(text)[0]
        answer.resized_res = resized_res
    else:
        print('fuck res res')

    p = re.compile(PIC_ORIG_REGEX)
    if p.search(text):
        original_link = p.findall(text)[0]
        original_link = PIC_ORIG_PREFIX + original_link

        answer.has_original = True

        answer.original_link = original_link
    else:
        print('fuck orig')

    p = re.compile(PIC_ORIG_SIZE_REGEX)
    if p.search(text):
        original_size = p.findall(text)[0]

        answer.original_size = original_size
    else:
        print('fuck orig size')

    p = re.compile(PIC_ORIG_RES_REGEX)
    if p.search(text):
        original_res = p.findall(text)[0]

        answer.original_res = original_res
    else:
        print('fuck orig res')

    # rating
    p = re.compile(RATING_REGEX)
    if p.search(text):
        rating = p.findall(text)[0]

        answer.rating = rating
    else:
        print('fuck rating')

    # print(answer)
    return answer