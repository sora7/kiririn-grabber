'''
Created on 27.01.2015
'''

import configparser
import datetime
import os
import sys

CONFIG_ENCODING = 'ascii'

class Job(object):
    __instance = None
    __config = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Job, cls).__new__(cls, *args, **kwargs)
        return cls.__instance


    def __init__(self):
        self.__filepath = 'job.ini'

        # disable the interpolation (symbol '%' used in url (e.g. %20 is '+'))
        self.__config = configparser.ConfigParser(interpolation=None)

        if os.path.exists(self.__filepath):
            self.__flush('r')
            # pprint(self.__config.keys())
        else:
            self.__default_config()
            self.__flush('w')

    def __default_config(self):
        self.__config['GENERAL'] = {}
        self.__config['GENERAL']['site'] = ''
        self.__config['GENERAL']['tags'] = ''

        self.__config['GENERAL']['load_resized'] = 'true'
        self.__config['GENERAL']['load_original'] = 'true'

        dt = datetime.datetime.now()
        self.__config['GENERAL']['start'] = dt.strftime('%d.%m.%Y %H:%M:%S')
        self.__config['GENERAL']['last_run'] = ''

        self.__config['SEARCH'] = {}
        self.__config['SEARCH']['next'] = ''
        self.__config['SEARCH']['done'] = 'false'

        self.__config['POSTS'] = {}
        self.__config['POSTS']['post_count'] = '0'
        self.__config['POSTS']['post_last'] = '0'

        self.__config['PICS'] = {}
        self.__config['PICS']['pic_count'] = '0'


    # flush, (or refresh config with job ini file)
    def __flush(self, mode):
        if mode == 'r':
            self.__config.read(self.__filepath, encoding=CONFIG_ENCODING)
        if mode == 'w':
            with open(self.__filepath, 'w', encoding=CONFIG_ENCODING) as cfgfile:
                self.__config.write(cfgfile)

    # update last_time field
    def __upd_time(self):
        dt = datetime.datetime.now()
        self.__config['GENERAL']['last_run'] = dt.strftime('%d.%m.%Y %H:%M:%S')

    # remove prev job file
    def clear(self):
        if os.path.exists(self.__filepath):
            os.remove(self.__filepath)

    @property
    def site(self):
        return self.__config['GENERAL']['site']

    @site.setter
    def site(self, value):
        self.__config['GENERAL']['site'] = value
        self.__upd_time()
        self.__flush('w')

    @property
    def tags(self):
        return self.__config['GENERAL']['tags'].split(' ')

    @tags.setter
    def tags(self, value):
        self.__config['GENERAL']['tags'] = ' '.join(value)
        self.__upd_time()
        self.__flush('w')

    @property
    def load_mode(self):
        return None

    @load_mode.setter
    def load_mode(self, mode):
        self.__config['GENERAL']['load_resized'] = 'false'
        self.__config['GENERAL']['load_original'] = 'false'

        if mode['original']:
            self.__config['GENERAL']['load_original'] = 'true'
            print('LOAD ORIGINAL')

        if mode['resized']:
            self.__config['GENERAL']['load_resized'] = 'true'
            print('LOAD RESIZED')

        self.__upd_time()
        self.__flush('w')

    @property
    def load_resized(self):
        if self.__config['GENERAL']['load_resized'] == 'true':
            return True
        else:
            return False

    @property
    def load_original(self):
        if self.__config['GENERAL']['load_original'] == 'true':
            return True
        else:
            return False

    @property
    def next(self):
        return self.__config['SEARCH']['next']

    @next.setter
    def next(self, value):
        self.__config['SEARCH']['next'] = value
        self.__upd_time()
        self.__flush('w')

    @property
    def search_done(self):
        done = self.__config['SEARCH']['done']
        if done == 'true':
            return True
        else:
            return False

    @search_done.setter
    def search_done(self, value):
        if value:
            done = 'true'
        else:
            done = 'false'
        self.__config['SEARCH']['done'] = done
        self.__upd_time()
        self.__flush('w')

    @property
    def post_count(self):
         return int(self.__config['POSTS']['post_count'])

    @property
    def last_post(self):
        last = int(self.__config['POSTS']['post_last'])
        return last

    @last_post.setter
    def last_post(self, value):
        self.__config['POSTS']['post_last'] = str(value)
        self.__upd_time()
        self.__flush('w')

    def write_posts(self, posts):
        post_count = int(self.__config['POSTS']['post_count'])
        for post_url in posts:
            self.__config['POSTS'][str(post_count)] = post_url
            post_count += 1
            self.__config['POSTS']['post_count'] = str(post_count)
        self.__upd_time()
        self.__flush('w')

    def read_posts(self):
        # self.__flush('r')
        post_count = int(self.__config['POSTS']['post_count'])
        posts = []
        for i in range(post_count):
            post = self.__config['POSTS'][str(i)]
            posts.append(post)
        return posts

    def add_posts(self, posts_file):
        with open(posts_file, 'r') as posts_fh:
            posts = posts_fh.readlines()
        self.write_posts(posts)

    def __add_pic_url(self, pic_url):
        pic_count = int(self.__config['PICS']['pic_count'])
        self.__config['PICS'][str(pic_count)] = pic_url
        pic_count += 1
        self.__config['PICS']['pic_count'] = str(pic_count)

    def write_pic(self, pic_info):
        original = self.load_original
        resized = self.load_resized

        if resized:
            if pic_info.has_resized:
                self.__add_pic_url(pic_info.resized_link)
            else:
                pass

        if original:
            if pic_info.has_original:
                self.__add_pic_url(pic_info.original_link)
            else:
                # have no original?
                pass

        self.__upd_time()
        self.__flush('w')

    def extract_pics(self):
        pic_filename = self.site + '_' + '_'.join(self.tags) + '.txt'
        with open(pic_filename, 'w') as pic_file:
            pic_count = int(self.__config['PICS']['pic_count'])
            for i in range(pic_count):
                pic = self.__config['PICS'][str(i)] + os.linesep
                pic_file.write(pic)