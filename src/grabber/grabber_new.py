import grabber.parsers.sankaku

import sqlite3
import time
import os

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


class Job(object):
    __db_file = 'grabber_jobs.db'

    def __init__(self):
        self.check_db()

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

            time_add = int(time.time())
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

    def get_job(self, job_id):
        pass


class Grabber(object):
    job = None

    def __init__(self):
        self.job = Job()

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

    def add_start(self, opt):
        self.add_job(opt)

        self.start_job()

    def start_job(self, job_id):
        pass

    def add_job(self, opt):
        self.job.add_job(opt)