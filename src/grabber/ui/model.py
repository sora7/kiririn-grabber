from grabber.web.opener import *
from grabber.web.ua import USER_AGENTS

from grabber.parsers.sankaku import *

import threading
import queue

import pprint

import grabber.grabber_new



class Worker(threading.Thread):

    def __init__(self, work_queue):
        super(Worker, self).__init__()
        self.work_queue = work_queue

    def run(self):
        try:
            url = self.work_queue.get()
            self.process(url)
        finally:
            pass

    def process(self, url):
        download2(url)


# import pprint

def test():
    urls = (
        'https://chan.sankakucomplex.com/?tags=misaki_kurehito+swimsuit+1girl+blush&commit=Search',
        'https://chan.sankakucomplex.com/?tags=angelise_ikaruga_misurugi+official_art&commit=Search',
        'https://chan.sankakucomplex.com/?tags=misaki_kurehito+swimsuit+1girl+blush&commit=Search',
        'https://chan.sankakucomplex.com/?tags=angelise_ikaruga_misurugi+official_art&commit=Search',
        'https://chan.sankakucomplex.com/?tags=misaki_kurehito+swimsuit+1girl+blush&commit=Search',
        'https://chan.sankakucomplex.com/?tags=angelise_ikaruga_misurugi+official_art&commit=Search',
        'https://chan.sankakucomplex.com/?tags=misaki_kurehito+swimsuit+1girl+blush&commit=Search',
        'https://chan.sankakucomplex.com/?tags=angelise_ikaruga_misurugi+official_art&commit=Search'
    )

    i = 1
    for url in urls:
        fname = 'file_' + str(i) + '.html'
        download(url, fname)
        i += 1

def test_threads():
    url1 = 'https://cs.sankakucomplex.com/data/90/eb/90ebcb1c65390a24cb1f858c32157df3.png'
    url2 = 'https://cs.sankakucomplex.com/data/e1/6b/e16bf5fc49fad3befefbb054d013e07c.png'
    url3 = 'https://cs.sankakucomplex.com/data/6e/98/6e98bbea25b428522e2e23328ecc06c1.jpg'


    # download2(url1)
        # print('done 1')
        #
        # download2(url2)
        # print('done 2')
        #
        # download2(url3)
        # print('done 3')

    work_queue = queue.Queue()
    work_queue.put(url1)
    work_queue.put(url2)
    work_queue.put(url3)

    for i in range(3):
        worker = Worker(work_queue)
        worker.start()

    print('ALL DONE')


class KiririnModel(object):
    ui = None
    grabber = None

    def __init__(self, view):
        self.ui = view
        self.grabber = grabber.grabber_new.Grabber()
        self.ui.set_booru_list(self.grabber.get_supported_booru())

        self.def_options()

    def start(self):
        print('Baka Aniki!')

        # url = 'https://chan.sankakucomplex.com/?tags=angelise_ikaruga_misurugi+official_art&commit=Search'
        # url = 'https://chan.sankakucomplex.com/post/show/4269544'

        # download(url, 'search.html')

        # with open('search.html', encoding='utf-8') as f:
        #     text = f.read()
        #
        # parser = SearchParser()
        # parser.feed(text)
        # info = parser.parse()
        # pprint.pprint(info)
        # print(len(info['posts']))
        # flags = {
        #     'tags': True,
        #     'original': True,
        #     'resized': True,
        #     'rating': True,
        # }
        # res = parser.parse(flags)
        #
        # pprint.pprint(res)
        # self.def_options()
        # self.get_options()
        # test()

        opt = self.get_options()
        # pprint.pprint(opt)

        # self.grabber.add_job(opt)
        self.grabber.add_start(opt)
        # test()

    def def_options(self):
        self.ui.booru_var.set('Sankaku Channel')
        self.ui.tags_var.set('misaki_kurehito')
        self.ui.save_var.set('e:\\pics')

    def get_options(self):
        options = dict()

        options['site'] = self.ui.booru_var.get()
        tags_str = self.ui.tags_var.get()
        # print(tags_str)
        # tags = tags_str.split(' ')
        options['tags'] = tags_str
        options['savepath'] = self.ui.save_var.get()

        rating = []
        if bool(self.ui.checkboxes['rating_safe'].get()):
            rating.append(str(common.RATING_SAFE))
        if bool(self.ui.checkboxes['rating_questionable'].get()):
            rating.append(str(common.RATING_QUESTIONABLE))
        if bool(self.ui.checkboxes['rating_explicit'].get()):
            rating.append(str(common.RATING_EXPLICIT))
        options['rating'] = ''.join(rating)

        size = []
        if bool(self.ui.checkboxes['size_original'].get()):
            size.append(str(common.SIZE_ORIGINAL))
        if bool(self.ui.checkboxes['size_resized'].get()):
            size.append(str(common.SIZE_RESIZED))
        options['size'] = ''.join(size)

        ftype = []
        if bool(self.ui.checkboxes['type_jpg'].get()):
            ftype.append(str(common.TYPE_JPG))
        if bool(self.ui.checkboxes['type_png'].get()):
            ftype.append(str(common.TYPE_PNG))
        if bool(self.ui.checkboxes['type_gif'].get()):
            ftype.append(str(common.TYPE_GIF))
        if bool(self.ui.checkboxes['type_webm'].get()):
            ftype.append(str(common.TYPE_WEBM))
        options['filetypes'] = ''.join(ftype)

        options['filenames'] = '%orig%'
        options['try_max'] = 10

        # pprint.pprint(options)

        return options
