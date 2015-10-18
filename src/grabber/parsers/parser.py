# common parser interface classs



# from sankaku import SankakuParser
# from mishimmie import MishimmieParser

# class SiteParser(object):
#
#     def __init__(self):
#         pass
#
#     def query_url(self, tags):
#         # return a query url created from tags
#         pass
#
#     def parse_search(self, text):
#         # return list with post urls
#         pass
#
#     def parse_post(self, text):
#         # return pic info
#         pass

ALIAS = {
    'sankaku':        'sankaku',
    'sankakuchannel': 'sankaku',
    'sanchan':        'sankaku',

    'mishimmie':      'mishimmie',
    'katawa':         'mishimmie',

    'konachan':        'konachan',

    'safebooru':       'safebooru',
}

# list of available booru
BOORU_LIST = ALIAS.keys()


class SiteParser(object):
    __parser = None

    def __init__(self, site):
        site = ALIAS[site]

        if site == 'sankaku':
            # self.__parser = SankakuParser()
            pass
        if site == 'mishimmie':
            # self.__parser = MishimmieParser()
            pass

    def query_url(self, tags):
        return self.__parser.query_url(tags)

    def parse_search(self, search_text):
        return self.__parser.parse_search(search_text)

    def parse_post(self, post_text):
        return self.__parser.parse_post(post_text)
