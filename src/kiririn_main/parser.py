import re
import os
import configparser

from kiririn_main.containers import SearchInfo
from kiririn_main.containers import PostInfo



# BOORU_CONFIG_PATH = 'sites'
# BOORU_CONFIG_ENCODING = 'utf-8'
#
# class BooruParser0(object):
#     NAME = ''
#     DESCRIPTION = ''
#     QUERY_URL = ''
#     TAG_SEP = ''
#     DEL_REGEX = ''
#     NEXT_REGEX = ''
#     NEXT_PREFIX = ''
#     POST_REGEX = ''
#     POST_PREFIX = ''
#     POST_ID_REGEX = ''
#     TAGS_REGEX = ''
#     POSTED_REGEX = ''
#     POSTED_AGO_REGEX = ''
#     PIC_RESIZE_REGEX = ''
#     PIC_RESIZE_RES_REGEX = ''
#     PIC_RESIZE_PREFIX = ''
#     PIC_ORIG_REGEX = ''
#     PIC_ORIG_RES_REGEX = ''
#     PIC_ORIG_SIZE_REGEX = ''
#     PIC_ORIG_PREFIX = ''
#     RATING_REGEX = ''
#
#     def __init__(self, booru_config):
#         # try filename
#         config_path = os.path.join(BOORU_CONFIG_PATH, booru_config)
#
#         booru_ini = configparser.ConfigParser(interpolation=None)
#         booru_ini.read(booru_config, encoding=BOORU_CONFIG_ENCODING)
#         print('OK')
#         print(booru_config)
#
#         print(booru_ini['GENERAL']['NAME'])
#
#
#     def query_url(self, tags):
#         tags_str = self.__booru['TAG_SEP'].join(tags)
#         query = self.__booru['QUERY_URL'] + tags_str
#
#     def parse_search(self, text):
#         answer = SearchInfo()
#
#         # i'ts not my fault thats my posts aren't popular
#         # lets delete the popular section
#         p = re.compile(DEL_REGEX, re.DOTALL)
#         if p.search(text):
#             text = re.sub(p, '###UNPOPULAR###', text)
#
#         # find the next page url (if any)
#         p = re.compile(NEXT_REGEX)
#         if p.search(text):
#             next_page = p.findall(text)[0]
#
#             answer.has_next = True
#             answer.next = NEXT_PREFIX + next_page
#             # print(answer.next)
#         else:
#             answer.has_next = False
#
#         # find teh posts
#         p = re.compile(POST_REGEX)
#         if p.search(text):
#             posts_raw = p.findall(text)
#
#             posts = list(map(lambda item: POST_PREFIX + item, posts_raw))
#
#             answer.has_posts = True
#             answer.posts = posts
#         else:
#             answer.has_posts = False
#
#         return answer
#
#     def parse_post(self, text):
#         pass

class BooruParser(object):
    NAME = ''
    DESCRIPTION = ''
    QUERY_URL = ''
    TAG_SEP = ''
    DEL_REGEX = ''
    NEXT_REGEX = ''
    NEXT_PREFIX = ''
    POST_REGEX = ''
    POST_PREFIX = ''
    POST_ID_REGEX = ''
    TAGS_REGEX = ''
    POSTED_REGEX = ''
    POSTED_AGO_REGEX = ''
    PIC_RESIZE_REGEX = ''
    PIC_RESIZE_RES_REGEX = ''
    PIC_RESIZE_PREFIX = ''
    PIC_ORIG_REGEX = ''
    PIC_ORIG_RES_REGEX = ''
    PIC_ORIG_SIZE_REGEX = ''
    PIC_ORIG_PREFIX = ''
    RATING_REGEX = ''

    def __init__(self, booru_config):
        import kiririn_main.parsers.sankaku as module

        self.prepare(module)

    def prepare(self, module):
        self.NAME = module.NAME
        self.QUERY_URL = module.QUERY_URL
        self.TAG_SEP = module.TAG_SEP

        self.DEL_REGEX = re.compile(module.DEL_REGEX, re.DOTALL)
        self.NEXT_REGEX = re.compile(module.NEXT_REGEX)

        self.NEXT_PREFIX = module.NEXT_PREFIX

        self.POST_REGEX = re.compile(module.POST_REGEX)

        self.POST_PREFIX = module.POST_PREFIX

        self.POST_ID_REGEX = re.compile(module.POST_ID_REGEX)
        self.TAGS_REGEX = re.compile(module.TAGS_REGEX)
        self.POSTED_REGEX = re.compile(module.POSTED_REGEX)
        self.POSTED_AGO_REGEX = re.compile(module.POSTED_AGO_REGEX)
        self.PIC_RESIZE_REGEX = re.compile(module.PIC_RESIZE_REGEX)
        self.PIC_RESIZE_RES_REGEX = re.compile(module.PIC_RESIZE_RES_REGEX)

        self.PIC_RESIZE_PREFIX = re.compile(module.PIC_RESIZE_PREFIX)

        self.PIC_ORIG_REGEX = re.compile(module.PIC_ORIG_REGEX)
        self.PIC_ORIG_RES_REGEX = re.compile(module.PIC_ORIG_RES_REGEX)
        self.PIC_ORIG_SIZE_REGEX = re.compile(module.PIC_ORIG_SIZE_REGEX)
        self.PIC_ORIG_PREFIX = re.compile(module.PIC_ORIG_PREFIX)

        self.RATING_REGEX = re.compile(module.PIC_ORIG_PREFIX)

    def query_url(self, tags):
        tags_str = self.TAG_SEP.join(tags)
        query = self.QUERY_URL + tags_str

        return query

    def parse_search(self, text):
        answer = SearchInfo()

        # i'ts not my fault that's my posts aren't popular
        # lets delete the popular section
        if self.DEL_REGEX.search(text):
            text = re.sub(self.DEL_REGEX, '###UNPOPULAR###', text)

        # find the next page url (if any)
        if self.NEXT_REGEX.search(text):
            next_page = self.NEXT_REGEX.findall(text)[0]

            answer.has_next = True
            answer.next = self.NEXT_PREFIX + next_page
        else:
            answer.has_next = False

        # find teh posts
        if self.POST_REGEX.search(text):
            posts_raw = self.POST_REGEX.findall(text)

            # add prefix
            posts = list(map(lambda item: self.POST_PREFIX + item, posts_raw))

            answer.has_posts = True
            answer.posts = posts
        else:
            answer.has_posts = False

        return answer


    def parse_post(self, text):
        answer = PostInfo()

        # find post id
        if self.POST_ID_REGEX.search(text):
            post_id = self.POST_ID_REGEX.findall(text)[0]
            answer.post_id = post_id
        else:
            print('cannot find post id')

        # extract tags
        if self.TAGS_REGEX.search(text):
            tags = self.TAGS_REGEX.findall(text)
            answer.tags = tags
        else:
            print('fuck tags')

        # extract datetime when posted
        if self.POSTED_REGEX.search(text):
            posted = self.POSTED_REGEX.findall(text)[0]
            answer.posted = posted
        else:
            print('fuck dt')

        # extract how much time ago posted
        if self.POSTED_AGO_REGEX.search(text):
            posted_ago = self.POSTED_AGO_REGEX.findall(text)[0]
            answer.posted_ago = posted_ago
        else:
            print('fuck dt ago')

        # resized pic
        if self.PIC_RESIZE_REGEX.search(text):
            resized_link = self.PIC_RESIZE_REGEX.findall(text)[0]
            resized_link = self.PIC_RESIZE_PREFIX + resized_link
            answer.has_resized = True
            answer.resized_link = resized_link
        else:
            print('fuck res')

        # resized pic resolution
        if self.PIC_RESIZE_RES_REGEX.search(text):
            resized_res = self.PIC_RESIZE_RES_REGEX.findall(text)[0]
            answer.resized_res = resized_res
        else:
            print('fuck res res')

        # original pic
        if self.PIC_ORIG_REGEX.search(text):
            original_link = self.PIC_ORIG_REGEX.findall(text)[0]
            original_link = self.PIC_ORIG_PREFIX + original_link

            answer.has_original = True
            answer.original_link = original_link
        else:
            print('fuck orig')

        # original pic size
        if self.PIC_ORIG_SIZE_REGEX.search(text):
            original_size = self.PIC_ORIG_SIZE_REGEX.findall(text)[0]

            answer.original_size = original_size
        else:
            print('fuck orig size')

        # original pic resolution
        if self.PIC_ORIG_RES_REGEX.search(text):
            original_res = self.PIC_ORIG_RES_REGEX.findall(text)[0]

            answer.original_res = original_res
        else:
            print('fuck orig res')

        # rating
        if self.RATING_REGEX.search(text):
            rating = self.RATING_REGEX.findall(text)[0]

            answer.rating = rating
        else:
            print('fuck rating')

        return answer