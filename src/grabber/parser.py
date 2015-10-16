import re
import os
import configparser

import sys
from pprint import pprint

from grabber.containers import SearchInfo, PostInfo


class BooruParser_(object):

    def __init__(self, booru):
        if booru == 'sankaku':
            import grabber.parsers.sankaku as booru_module
            # from kiririn_main.parsers.sankaku import booru_data
        elif booru == 'konachan':
            import grabber.parsers.konachan as booru_module

        self.import_booru_data(booru_module)
        self.compile_regex()

    def import_booru_data(self, module):
        # import module

        booru_data = {
            'NAME': module.NAME,
            'DESCRIPTION': module.DESCRIPTION,

            'QUERY_PREFIX': module.QUERY_PREFIX,
            'TAG_SEP': module.TAG_SEP,
            'QUERY_SUFFIX': module.QUERY_SUFFIX,
            'TAG_MAX': int(module.TAG_MAX),

            'DEL_TEXT': module.DEL_TEXT,
            'DEL_REGEX': module.DEL_REGEX,

            'NEXT_REGEX': module.NEXT_REGEX,
            'NEXT_PREFIX': module.NEXT_PREFIX,

            'POST_REGEX': module.POST_REGEX,
            'POST_PREFIX': module.POST_PREFIX,

            'POST_ID_REGEX': module.POST_ID_REGEX,
            'TAGS_REGEX': module.TAGS_REGEX,

            'POSTED_REGEX': module.POSTED_REGEX,
            'POSTED_AGO_REGEX': module.POSTED_AGO_REGEX,

            'PIC_RESIZE_REGEX': module.PIC_RESIZE_REGEX,
            'PIC_RESIZE_RES_REGEX': module.PIC_RESIZE_RES_REGEX,
            'PIC_RESIZE_PREFIX': module.PIC_RESIZE_PREFIX,

            'PIC_ORIG_REGEX': module.PIC_ORIG_REGEX,
            'PIC_ORIG_RES_REGEX': module.PIC_ORIG_RES_REGEX,
            'PIC_ORIG_SIZE_REGEX': module.PIC_ORIG_SIZE_REGEX,
            'PIC_ORIG_PREFIX': module.PIC_ORIG_PREFIX,

            'PIC_ORIG2': module.PIC_ORIG2,
            'PIC_ORIG2_REGEX': module.PIC_ORIG2_REGEX,
            'PIC_ORIG2_RES_REGEX': module.PIC_ORIG2_RES_REGEX,
            'PIC_ORIG2_SIZE_REGEX': module.PIC_ORIG2_SIZE_REGEX,
            'PIC_ORIG2_PREFIX': module.PIC_ORIG2_PREFIX,

            'RATING_REGEX': module.RATING_REGEX
        }

        self.data = booru_data

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
        if len(tags) > self.data['TAG_MAX']:
            print('% supports only %s tags' % (self.data['NAME'], self.data['TAG_MAX']))
            print('tag list will be trimmed')
            tags = tags[:self.data['TAG_MAX']]

        tags_str = self.data['TAG_SEP'].join(tags)

        query = self.data['QUERY_PREFIX'] + tags_str + self.data['QUERY_SUFFIX']

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

    @staticmethod
    def __get_by_regex(text, regex=None, prefix=None, name=''):
        if regex.search(text):
            info = regex.findall(text)[0]
            if prefix is not None:
                return '%s%s'%(prefix, info)
            else:
                return info
        else:
            print('cannot find %s'%(name))
            return None

    def get_id(self, text):
        # return self.__get_by_regex(text, regex=self.data['POST_ID_REGEX'], name='post id')
        # find post id
        if self.data['POST_ID_REGEX'].search(text):
            post_id = self.data['POST_ID_REGEX'].findall(text)[0]
            return post_id
        else:
            print('cannot find post id')
            return None

    def get_tags(self, text):
        # extract tags
        if self.data['TAGS_REGEX'].search(text):
            tags = self.data['TAGS_REGEX'].findall(text)
            return tags
        else:
            print('cannot find tags')
            return None

    def get_posted_datetime(self, text):
        # extract datetime when posted
        if self.data['POSTED_REGEX'].search(text):
            posted = self.data['POSTED_REGEX'].findall(text)[0]
            return posted
        else:
            print('cannot find datetime')
            return None

    def get_posted_ago(self, text):
        # extract how much time ago posted
        if self.data['POSTED_AGO_REGEX'].search(text):
            posted_ago = self.data['POSTED_AGO_REGEX'].findall(text)[0]
            return posted_ago
        else:
            print('cannot find datetime ago')
            return None

    def get_resized_pic(self, text):
        # resized pic
        if self.data['PIC_RESIZE_REGEX'].search(text):
            # print('OK')
            resized_link = self.data['PIC_RESIZE_REGEX'].findall(text)[0]
            resized_link = self.data['PIC_RESIZE_PREFIX'] + resized_link
            return (True, resized_link)
        else:
            print('cannot find resized pic')
            return (False, None)

    def get_resized_res(self, text):
        # resized pic resolution
        if self.data['PIC_RESIZE_RES_REGEX'].search(text):
            resized_res = self.data['PIC_RESIZE_RES_REGEX'].findall(text)[0]
            return resized_res
        else:
            print('cannot find resized resolution')
            return None

    def get_original_pic(self, text):
        # original pic
        if self.data['PIC_ORIG_REGEX'].search(text):
            original_link = self.data['PIC_ORIG_REGEX'].findall(text)[0]
            original_link = self.data['PIC_ORIG_PREFIX'] + original_link
            return (True, original_link)
        else:
            print('cannot find original pic')
            return (False, None)

    def get_original_size(self, text):
        # original pic size
        if self.data['PIC_ORIG_SIZE_REGEX'].search(text):
            original_size = self.data['PIC_ORIG_SIZE_REGEX'].findall(text)[0]
            return original_size
        else:
            print('cannot find original size')
            return None

    def get_original_res(self, text):
        # original pic resolution
        if self.data['PIC_ORIG_RES_REGEX'].search(text):
            original_res = self.data['PIC_ORIG_RES_REGEX'].findall(text)[0]
            return original_res
        else:
            print('cannot find original resolution')
            return None

    def get_original_pic2(self, text):
        # original pic
        if self.data['PIC_ORIG2_REGEX'].search(text):
            original_link = self.data['PIC_ORIG2_REGEX'].findall(text)[0]
            original_link = self.data['PIC_ORIG2_PREFIX'] + original_link
            return (True, original_link)
        else:
            print('cannot find original pic')
            return (False, None)

    def get_original_size2(self, text):
        # original pic size
        if self.data['PIC_ORIG2_SIZE_REGEX'].search(text):
            original_size = self.data['PIC_ORIG2_SIZE_REGEX'].findall(text)[0]
            return original_size
        else:
            print('cannot find original size')
            return None

    def get_original_res2(self, text):
        # original pic resolution
        if self.data['PIC_ORIG2_RES_REGEX'].search(text):
            original_res = self.data['PIC_ORIG2_RES_REGEX'].findall(text)[0]
            return original_res
        else:
            print('cannot find original resolution')
            return None

    def get_rating(self, text):
        # rating
        if self.data['RATING_REGEX'].search(text):
            rating = self.data['RATING_REGEX'].findall(text)[0]
            return rating
        else:
            print('cannot find rating')
            return None

    def parse_post(self, text):
        answer = PostInfo()

        answer.post_id = self.get_id(text)
        answer.tags = self.get_tags(text)
        answer.posted = self.get_posted_datetime(text)
        answer.posted_ago = self.get_posted_ago(text)

        (answer.has_resized, answer.resized_link) = self.get_resized_pic(text)
        answer.resized_res = self.get_resized_res(text)
        (answer.has_original, answer.original_link) = self.get_original_pic(text)

        answer.original_size = self.get_original_size(text)
        answer.original_res = self.get_original_size(text)

        if self.data['PIC_ORIG2']:
            (answer.has_original2, answer.original_link2) = self.get_original_pic2(text)

            answer.original_size2 = self.get_original_size2(text)
            answer.original_res2 = self.get_original_size2(text)

        answer.rating = self.get_rating(text)

        return answer

# hide some methods))
class BooruParser(object):
    __parser = None

    def __init__(self, booru):
        self.__parser = BooruParser_(booru)

    def query_url(self, tags):
        return self.__parser.query_url(tags)

    def parse_search(self, text):
        return self.__parser.parse_search(text)

    def parse_post(self, text):
        return self.__parser.parse_post(text)

