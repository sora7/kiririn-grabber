import grabber.parsers.sankaku

import sqlite3
import os


class Job(object):
    __db_file = 'grabber_jobs.db'

    def __init__(self):
        self.check_db()

    def make_db(self):
        with sqlite3.connect(self.__db_file) as connect:
            cursor = connect.cursor()
            cursor.execute('CREATE TABLE jobs (' +
                           'id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,'
                           'site TEXT NOT NULL,' +
                           'tags TEXT NOT NULL,' +
                           'done INTEGER NOT NULL,' +
                           'rating INTEGER,' +
                           'size INTEGER NOT NULL,' +
                           'search_done INTEGER NOT NULL,' +
                           'posts_done INTEGER NOT NULL,' +
                           'time_add INTEGER NOT NULL,' +
                           'time_start INTEGER NOT NULL,' +
                           'time_last INTEGER NOT NULL,' +
                           'filenames TEXT NOT NULL,' +
                           'filetypes INTEGER NOT NULL,' +
                           'try_max INTEGER NOT NULL' +
                           ');'
                        )
            connect.commit()
            cursor = connect.cursor()
            cursor.execute('CREATE TABLE search (' +
                           'id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,' +
                           'job_id INTEGER NOT NULL,' +
                           'url TEXT NOT NULL,' +
                           'done INTEGER NOT NULL,' +
                           'try INTEGER NOT NULL' +
                           ');'
                           )
            connect.commit()
            cursor = connect.cursor()
            cursor.execute('CREATE TABLE posts (' +
                           'id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,' +
                           'job_id INTEGER NOT NULL,' +
                           'url TEXT NOT NULL,' +
                           'done INTEGER NOT NULL,' +
                           'try INTEGER NOT NULL,' +
                           'rating INTEGER,' +
                           'tags TEXT' +
                           ');'
                           )
            connect.commit()
            cursor = connect.cursor()
            cursor.execute('CREATE TABLE pics (' +
                           'id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,' +
                           'url TEXT NOT NULL,' +
                           'done INTEGER NOT NULL,' +
                           'job_id INTEGER NOT NULL ,' +
                           'try INTEGER NOT NULL,' +
                           'post_id INTEGER NOT NULL,' +
                           'filename TEXT NOT NULL' +
                           ');'
                           )
            connect.commit()


    def check_db(self):
        if not os.path.exists(self.__db_file):
            self.make_db()


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
        pass