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
    def __init__(self, booru):
        if booru == 'sankaku':
            from kiririn_main.parsers.sankaku import booru_data
        elif booru == 'konachan':
            from kiririn_main.parsers.konachan import booru_data

        self.data = booru_data
        self.compile_regex()

    def compile_regex(self):
        # compiling regex
        if self.data['DEL_TEXT']:
            self.data['DEL_REGEX'] = re.compile(self.data['DEL_REGEX'], re.DOTALL)

        self.data['NEXT_REGEX'] = re.compile(self.data['NEXT_REGEX'])
        self.data['POST_REGEX'] = re.compile(self.data['POST_REGEX'])

        self.data['POST_ID_REGEX'] = re.compile(self.data['POST_ID_REGEX'])
        self.data['TAGS_REGEX'] = re.compile(self.data['TAGS_REGEX'])
        self.data['POSTED_REGEX'] = re.compile(self.data['POSTED_REGEX'])
        self.data['POSTED_AGO_REGEX'] = re.compile(self.data['POSTED_AGO_REGEX'])

        self.data['PIC_RESIZE_REGEX'] = re.compile(self.data['PIC_RESIZE_REGEX'])
        self.data['PIC_RESIZE_RES_REGEX'] = re.compile(self.data['PIC_RESIZE_RES_REGEX'])

        self.data['PIC_ORIG_REGEX'] = re.compile(self.data['PIC_ORIG_REGEX'])
        self.data['PIC_ORIG_RES_REGEX'] = re.compile(self.data['PIC_ORIG_RES_REGEX'])
        self.data['PIC_ORIG_SIZE_REGEX'] = re.compile(self.data['PIC_ORIG_SIZE_REGEX'])

        if self.data['PIC_ORIG2']:
            self.data['PIC_ORIG2_REGEX'] = re.compile(self.data['PIC_ORIG2_REGEX'])
            self.data['PIC_ORIG2_RES_REGEX'] = re.compile(self.data['PIC_ORIG2_RES_REGEX'])
            self.data['PIC_ORIG2_SIZE_REGEX'] = re.compile(self.data['PIC_ORIG2_SIZE_REGEX'])

        self.data['RATING_REGEX'] = re.compile(self.data['RATING_REGEX'])

    def query_url(self, tags):
        tags_str = self.data['TAG_SEP'].join(tags)
        query = self.data['QUERY_PREFIX'] + tags_str

        return query

    def parse_search(self, text):
        answer = SearchInfo()

        if self.data['DEL_TEXT']:
            # i'ts not my fault that's my posts aren't popular
            # lets delete the popular section
            if self.data['DEL_REGEX'].search(text):
                text = re.sub(self.data['DEL_REGEX'], '###UNPOPULAR###', text)

        # find the next page url (if any)
        if self.data['NEXT_REGEX'].search(text):
            next_page = self.data['NEXT_REGEX'].findall(text)[0]

            answer.has_next = True
            answer.next = self.data['NEXT_PREFIX'] + next_page
        else:
            answer.has_next = False

        # find teh posts
        if self.data['POST_REGEX'].search(text):
            posts_raw = self.data['POST_REGEX'].findall(text)

            # add prefix
            posts = list(map(lambda item: self.data['POST_PREFIX'] + item, posts_raw))

            answer.has_posts = True
            answer.posts = posts
        else:
            answer.has_posts = False

        return answer

    def parse_post(self, text):
        answer = PostInfo()

        # find post id
        if self.data['POST_ID_REGEX'].search(text):
            post_id = self.data['POST_ID_REGEX'].findall(text)[0]
            answer.post_id = post_id
        else:
            print('cannot find post id')

        # extract tags
        if self.data['TAGS_REGEX'].search(text):
            tags = self.data['TAGS_REGEX'].findall(text)
            answer.tags = tags
        else:
            print('cannot find tags')

        # extract datetime when posted
        if self.data['POSTED_REGEX'].search(text):
            posted = self.data['POSTED_REGEX'].findall(text)[0]
            answer.posted = posted
        else:
            print('cannot find datetime')

        # extract how much time ago posted
        if self.data['POSTED_AGO_REGEX'].search(text):
            posted_ago = self.data['POSTED_AGO_REGEX'].findall(text)[0]
            answer.posted_ago = posted_ago
        else:
            print('cannot find datetime ago')

        # resized pic
        if self.data['PIC_RESIZE_REGEX'].search(text):
            print('OK')
            resized_link = self.data['PIC_RESIZE_REGEX'].findall(text)[0]
            resized_link = self.data['PIC_RESIZE_PREFIX'] + resized_link
            answer.has_resized = True
            answer.resized_link = resized_link
        else:
            print('cannot find resized')


        # resized pic resolution
        if self.data['PIC_RESIZE_RES_REGEX'].search(text):
            resized_res = self.data['PIC_RESIZE_RES_REGEX'].findall(text)[0]
            answer.resized_res = resized_res
        else:
            print('cannot find resized resolution')

        # original pic
        if self.data['PIC_ORIG_REGEX'].search(text):
            original_link = self.data['PIC_ORIG_REGEX'].findall(text)[0]
            original_link = self.data['PIC_ORIG_PREFIX'] + original_link

            answer.has_original = True
            answer.original_link = original_link
        else:
            print('cannot find orig')

        # original pic size
        if self.data['PIC_ORIG_SIZE_REGEX'].search(text):
            original_size = self.data['PIC_ORIG_SIZE_REGEX'].findall(text)[0]

            answer.original_size = original_size
        else:
            print('cannot find orig size')

        # original pic resolution
        if self.data['PIC_ORIG_RES_REGEX'].search(text):
            original_res = self.data['PIC_ORIG_RES_REGEX'].findall(text)[0]

            answer.original_res = original_res
        else:
            print('cannot find orig resolution')

        if self.data['PIC_ORIG2']:
            # original pic2
            if self.data['PIC_ORIG2_REGEX'].search(text):
                original_link = self.data['PIC_ORIG2_REGEX'].findall(text)[0]
                original_link = self.data['PIC_ORIG2_PREFIX'] + original_link

                answer.has_original2 = True
                answer.original_link2 = original_link
            else:
                print('cannot find orig2')

            # original pic size
            if self.data['PIC_ORIG2_SIZE_REGEX'].search(text):
                original_size = self.data['PIC_ORIG2_SIZE_REGEX'].findall(text)[0]

                answer.original_size2 = original_size
            else:
                print('cannot find orig2 size')

            # original pic resolution
            if self.data['PIC_ORIG2_RES_REGEX'].search(text):
                original_res = self.data['PIC_ORIG2_RES_REGEX'].findall(text)[0]

                answer.original_res2 = original_res
            else:
                print('cannot find orig2 resolution')


        # rating
        if self.data['RATING_REGEX'].search(text):
            rating = self.data['RATING_REGEX'].findall(text)[0]

            answer.rating = rating
        else:
            print('cannot find rating')

        return answer


class BooruParser2(object):
    booru = {}
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
        if booru_config == 'sankaku':
            import kiririn_main.parsers.sankaku as module
        elif booru_config == 'konachan':
            import kiririn_main.parsers.konachan as module

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
            print('OK')
            resized_link = self.PIC_RESIZE_REGEX.findall(text)[0]
            print('RES:', resized_link)
            return 0
            resized_link = self.PIC_RESIZE_PREFIX + resized_link
            answer.has_resized = True
            answer.resized_link = resized_link
        else:
            print('fuck res')

        return 0

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