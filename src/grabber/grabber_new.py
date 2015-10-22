import sqlite3
import time
import os
# --------DEBUG----------
import sys
from pprint import pprint
# -----------------------
import grabber.parsers.sankaku
import grabber.web.opener

JOB_OPTIONS = {
    'site': '',
    'tags': '',
    'savepath': '',
    'rating': '',
    'size': '',
    'filetypes': '',
    'filenames': '',
    'try_max': 0,
}


class PicLoader(object):
    __concurrent = None
    __save_path = None

    __loader = None

    def __init__(self, save_path, concurrent=1):
        self.__save_path = save_path
        if not os.path.exists(self.__save_path):
            os.mkdir(self.__save_path)

        self.__concurrent = concurrent

        self.__loader = grabber.web.opener.Loader()

    def get_concurrent(self):
        return self.__concurrent

    def load(self, url, filename):
        file_body = self.__loader.get_file(url)
        file_fullpath = os.path.join(self.__save_path, filename)

        with open(file_fullpath, 'wb') as file_to_write:
            file_to_write.write(file_body)


class Job(object):
    __db_file = 'grabber_jobs.db'

    def __init__(self):
        self.check_db()

    @staticmethod
    def get_time():
        return int(time.time())

    def make_db(self):
        with sqlite3.connect(self.__db_file) as conn:
            curs = conn.cursor()
            curs.execute('CREATE TABLE jobs (' +
                         'id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,' +
                         'site TEXT NOT NULL,' +
                         'tags TEXT NOT NULL,' +
                         'size INTEGER NOT NULL,' +
                         'rating INTEGER,' +
                         'save_path TEXT NOT NULL,' +
                         'filetypes INTEGER NOT NULL,' +
                         'filenames TEXT NOT NULL,' +
                         'try_max INTEGER NOT NULL,' +
                         'time_add INTEGER NOT NULL,' +
                         'time_start INTEGER,' +
                         'time_last INTEGER NOT NULL,' +
                         'done INTEGER NOT NULL,' +
                         'search_done INTEGER NOT NULL,' +
                         'posts_done INTEGER NOT NULL' +
                         ');'
                         )
            conn.commit()
            curs = conn.cursor()
            curs.execute('CREATE TABLE search (' +
                         'id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,' +
                         'job_id INTEGER NOT NULL,' +
                         'url TEXT NOT NULL,' +
                         'done INTEGER NOT NULL,' +
                         'try INTEGER NOT NULL' +
                         ');'
                         )
            conn.commit()
            curs = conn.cursor()
            curs.execute('CREATE TABLE posts (' +
                         'id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,' +
                         'job_id INTEGER NOT NULL,' +
                         'url TEXT NOT NULL,' +
                         'done INTEGER NOT NULL,' +
                         'try INTEGER NOT NULL,' +
                         'rating INTEGER,' +
                         'tags TEXT' +
                         ');'
                         )
            conn.commit()
            curs = conn.cursor()
            curs.execute('CREATE TABLE pics (' +
                         'id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,' +
                         'url TEXT NOT NULL,' +
                         'done INTEGER NOT NULL,' +
                         'job_id INTEGER NOT NULL ,' +
                         'try INTEGER NOT NULL,' +
                         'post_id INTEGER NOT NULL,' +
                         'filename TEXT NOT NULL' +
                         ');'
                         )
            conn.commit()

    def check_db(self):
        if not os.path.exists(self.__db_file):
            self.make_db()

    def add_job(self, options):
        with sqlite3.connect(self.__db_file) as conn:
            curs = conn.cursor()

            time_add = self.get_time()
            # time_start = None
            time_last = time_add

            job_tuple = (
                options['site'],
                options['tags'],
                options['size'],
                options['rating'],
                options['savepath'],
                options['filetypes'],
                options['filenames'],
                options['try_max'],
                time_add,
                # time_start,
                time_last,
                '0',  # job done
                '0',  # search done
                '0'   # posts done
            )

            curs.execute('INSERT INTO jobs VALUES ' +
                         '(NULL,?,?,?,?,?,?,?,?,?,NULL,?,?,?,?)',
                         job_tuple
                         )
            conn.commit()

    def get_job(self, job_id=0, last=False):
        with sqlite3.connect(self.__db_file) as conn:
            curs = conn.cursor()
            if last:
                curs.execute('SELECT id, site, tags, size, rating, ' +
                             'save_path, filetypes, filenames, try_max, '
                             'done, search_done, posts_done ' +
                             'FROM jobs ' +
                             'ORDER BY id DESC ' +
                             'LIMIT 1;'
                             )
            else:
                curs.execute('SELECT id, site, tags, size, rating, ' +
                             'save_path, filetypes, filenames, try_max, ' +
                             'done, search_done, posts_done ' +
                             'FROM jobs ' +
                             'WHERE id=%s' % job_id
                             )
            data = curs.fetchall()
            # (job_id, site, tags, size, rating, save_path, filetypes, filenames, try_max, done, search_done, posts_done)
            # print(data)
        line = data[0]
        options = {}
        fields = (
                'job_id',
                'site',
                'tags',
                'size',
                'rating',
                'save_path',
                'filetypes',
                'filenames',
                'try_max',
                'done',
                'search_done',
                'posts_done'
        )
        # print(len(fields), len(line))
        for i in range(len(line)):
            options[fields[i]] = line[i]
        options['rating'] = str(options['rating'])
        options['size'] = str(options['size'])
        options['filetypes'] = str(options['filetypes'])
        # print('PRINT OPTIONS')
        # pprint(options)
        return options

    def job_upd(self, job_id, search_done=False, posts_done=False, job_done=False):
        with sqlite3.connect(self.__db_file) as conn:
            curs = conn.cursor()
            time_last = self.get_time()

            sql_query = ['UPDATE jobs ', 'SET time_last=%s' % time_last]

            if search_done:
                sql_query.append(', ')
                sql_query.append('search_done=1')
            if posts_done:
                sql_query.append(', ')
                sql_query.append('posts_done=1')
            if job_done:
                sql_query.append(', ')
                sql_query.append('done=1')

            sql_query.append(' WHERE id=%s ' % job_id)

            # print(''.join(sql_query))
            curs.execute(''.join(sql_query))

    def job_start_time(self, job_id):
        with sqlite3.connect(self.__db_file) as conn:
            curs = conn.cursor()
            time_start = self.get_time()
            curs.execute('UPDATE jobs ' +
                         'SET time_start=%s, ' % time_start +
                         'time_last=%s ' % time_start +
                         'WHERE id=%s ' % job_id
                         )

    def get_search(self, job_id):
        with sqlite3.connect(self.__db_file) as conn:
            curs = conn.cursor()
            curs.execute('SELECT id, url, try ' +
                         'FROM search ' +
                         'WHERE job_id=%s and done=0 ' % job_id +
                         'LIMIT 1;'
                         )
            data = curs.fetchall()
            # print(data)
            # sys.exit(-1)
            return data

    def add_search(self, job_id, url):
        with sqlite3.connect(self.__db_file) as conn:
            curs = conn.cursor()
            search_init = (job_id, url, 0, 0)
            curs.execute('INSERT INTO search VALUES ' +
                         '(NULL,?,?,?,?)', search_init
                         )
            conn.commit()

    def upd_search(self, search_id, done, try_count):
        with sqlite3.connect(self.__db_file) as conn:
            curs = conn.cursor()
            curs.execute('UPDATE search ' +
                         'SET done=%s, ' % int(done) +
                         'try=%s ' % try_count +
                         'WHERE id=%s ' % search_id
                         )
            conn.commit()

    def add_posts(self, job_id, posts):
        with sqlite3.connect(self.__db_file) as conn:
            curs = conn.cursor()
            for post_url in posts:
                posts_tuple = (job_id, post_url, 0, 0)
                curs.execute('INSERT INTO posts VALUES ' +
                             '(NULL,?,?,?,?,NULL,NULL)', posts_tuple
                             )
            conn.commit()
            time_last = self.get_time()
            curs.execute('UPDATE jobs ' +
                         'SET time_last=%s ' % time_last +
                         'WHERE id=%s ' % job_id
                         )

    def get_posts(self, job_id):
        with sqlite3.connect(self.__db_file) as conn:
            curs = conn.cursor()
            curs.execute('SELECT id, url, try ' +
                         'FROM posts ' +
                         'WHERE job_id=%s and done=0' % job_id
                         )
            data = curs.fetchall()
            # print(data)
            return data

    def upd_posts(self, post_id, try_count, rating, tags, done=True):
        with sqlite3.connect(self.__db_file) as conn:
            curs = conn.cursor()
            curs.execute('UPDATE posts ' +
                         'SET done=%s, ' % int(done) +
                         'try=%s, ' % try_count +
                         'rating=%s, ' % rating +
                         "tags='%s' " % ' '.join(tags) +
                         'WHERE id=%s ' % post_id
                         )
            conn.commit()

    def add_pics(self, job_id, post_id, pics):
        with sqlite3.connect(self.__db_file) as conn:
            curs = conn.cursor()
            for url, filename in pics:
                pics_tuple = (url, 0, job_id, 0, post_id, filename)
                curs.execute('INSERT INTO pics VALUES ' +
                             '(NULL,?,?,?,?,?,?)', pics_tuple
                             )
            conn.commit()
            time_last = self.get_time()
            curs.execute('UPDATE jobs ' +
                         'SET time_last=%s ' % time_last +
                         'WHERE id=%s ' % job_id
                         )

    def get_pics(self, job_id):
        with sqlite3.connect(self.__db_file) as conn:
            curs = conn.cursor()
            curs.execute('SELECT id, url, try, filename ' +
                         'FROM pics ' +
                         'WHERE job_id=%s and done=0' % job_id
                         )
            data = curs.fetchall()
            # print(data)
            return data
        # options = self.job.get_job(job_id)

    def upd_pics(self, pic_id, try_count=1, done=True):
        with sqlite3.connect(self.__db_file) as conn:
            curs = conn.cursor()
            curs.execute('UPDATE pics ' +
                         'SET done=%s, ' % int(done) +
                         'try=%s ' % try_count +
                         'WHERE id=%s ' % pic_id
                         )
            conn.commit()


class PicNamer(object):
    __pattern = None

    def __init__(self, pattern):
        self.__pattern = pattern

    def gen(self, url, tags=[]):
        if self.__pattern == '%orig%':
            fname_orig = url.split('/')[-1]
            return fname_orig


class Grabber(object):
    job = None

    search_parser = None
    post_parser = None

    loader = None

    pic_namer = None

    pics_loader = None

    def __init__(self):
        self.job = Job()

        self.loader = grabber.web.opener.Loader()

    @staticmethod
    def get_supported_booru():
        lst = (
            'Sankaku Channel',
            'Konachan',
            'Danbooru',
            'Gelbooru',
            'Safebooru'
        )
        return lst

    def add_job(self, opt):
        self.job.add_job(opt)

    def add_start(self, opt):
        #
        #
        #
        #
        #
        # self.add_job(opt)
        self.start_last_job()

    def start_last_job(self):
        options = self.job.get_job(last=True)
        self.start_job(options['job_id'])

    def start_job(self, job_id):
        options = self.job.get_job(job_id)
        self.job.job_start_time(options['job_id'])

        self.load_parsers(options['site'])
        self.pic_namer = PicNamer(options['filenames'])
        self.pics_loader = PicLoader(options['save_path'])

        if not options['search_done']:
            # search processing
            search_data = self.job.get_search(options['job_id'])
            if len(search_data) == 0:
                # no search started yet
                self.search_start(options)
            else:
                # continue processing search
                self.search_process(options['job_id'])
        else:
            if not options['posts_done']:
                # posts processing
                self.post_process(options['job_id'])
            else:
                self.load_pics(options['job_id'])

    def load_parsers(self, site):
        if site == 'Sankaku Channel':
            self.search_parser = grabber.parsers.sankaku.SearchParser()
            self.post_parser = grabber.parsers.sankaku.PostParser()
        elif site == 'Konachan':
            pass

    def search_start(self, options):
        # print('SEARCH START')
        tags = options['tags']
        init_url = self.search_parser.make_query(tags)
        # print(init_url)
        self.job.add_search(options['job_id'], init_url)
        self.search_process(options['job_id'])

    def search_process(self, job_id):
        search_data = self.job.get_search(job_id)

        print('SEARCH')
        if len(search_data) > 0:
            search_id, url, try_count = search_data[0]
            search_text = self.loader.get_html(url)

            self.search_parser.feed(search_text)
            search_info = self.search_parser.parse()

            if len(search_info['posts']) > 0:
                print('%s posts extracted' % len(search_info['posts']))
                self.job.add_posts(job_id, search_info['posts'])
            if bool(search_info['next']):
                print('next search page: %s' % search_info['next'])
                self.job.add_search(job_id, search_info['next'])

            self.job.upd_search(search_id, done=True, try_count=1)

            self.search_process(job_id)
        else:
            print('Search processing done')
            # next step
            self.job.job_upd(job_id, search_done=True)
            self.post_process(job_id)

        # for search_id, url, try_count in search_data:
        #     search_text = self.loader.get_html(url)
        #
        #     self.search_parser.feed(search_text)
        #     search_info = self.search_parser.parse()
        #
        #     self.job.add_posts(job_id, search_info['posts'])
        #     if bool(search_info['next']):
        #         self.job.search_add(job_id, search_info['next'])
        #
        #     self.job.search_upd(search_id, done=True, try_count=1)
        #
        #     self.search_process(job_id)
        # # next step
        # self.job.job_upd(job_id, search_done=True)
        # self.post_process(job_id)

    @staticmethod
    def check_filetypes(url, ftypes):
        u = url.lower()
        if u.endswith('jpg') or u.endswith('jpeg'):
            if '1' in ftypes:
                return True
        if u.endswith('png'):
            if '2' in ftypes:
                return True
        if u.endswith('gif'):
            if '3' in ftypes:
                return True
        if u.endswith('webm'):
            if '4' in ftypes:
                return True
            return False

    def post_process(self, job_id):
        posts_data = self.job.get_posts(job_id)
        options = self.job.get_job(job_id)

        for post_id, post_url, try_count in posts_data:
            # print(post_id, url, try_count)
            post_text = self.loader.get_html(post_url)

            self.post_parser.feed(post_text)
            post_info = self.post_parser.parse()

            # pprint(options)
            pprint(post_info['pics'])

            if post_info['rating'] in options['rating']:
                # rating ok
                tags = post_info['tags']
                pics = []

                for size, pic_url in post_info['pics']:
                    if size in options['size'] and pic_url:
                        if self.check_filetypes(pic_url, options['filetypes']):
                            filename = self.pic_namer.gen(pic_url, tags)
                            pics.append((pic_url, filename))

                self.job.add_pics(job_id, post_id, pics)
            try_max = 1
            self.job.upd_posts(post_id,
                               try_max,
                               post_info['rating'],
                               post_info['tags'])

        self.job.job_upd(job_id, posts_done=True)
        self.load_pics(job_id)

    def load_pics(self, job_id):
        pics_data = self.job.get_pics(job_id)
        for pic_id, url, try_count, filename in pics_data:
            self.pics_loader.load(url, filename)
            print('DONE: %s' % filename)
            self.job.upd_pics(pic_id, try_count=1, done=True)
        self.job.job_upd(job_id, job_done=True)
#

