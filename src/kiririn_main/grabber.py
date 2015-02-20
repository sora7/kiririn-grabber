from kiririn_main.job import Job
from kiririn_main.parser import BooruParser
from kiririn_main.web.opener import URLopen


class Grabber(object):
    __job = None
    __opener = None
    __parser = None

    def __init__(self):
        self.__job = Job()

    def search(self, site, tags, mode):
        pass

    def cont_search(self):
        pass

    def find_posts(self):
        pass

    def process_posts(self):
        pass



