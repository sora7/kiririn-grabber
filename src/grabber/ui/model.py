from grabber.web.opener import *
from grabber.web.ua import USER_AGENTS

import urllib.request

# import socket


class KiririnModel(object):
    ui = None

    def __init__(self, view):
        self.ui = view

    def say(self):
        print('Baka Aniki!')
        lst = ['Sankaku Channel', 'Konachan', 'Danbooru', 'Gelbooru', 'Safebooru']
        self.ui.set_booru_list(lst)


