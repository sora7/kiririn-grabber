'''
Created on 13.12.2014
'''

# from urllib.request import FancyURLopener
import urllib.request
import random

from grabber.web.ua import USER_AGENTS
from grabber.main import Pause
from grabber.main import color_text


def get_ua():
    return random.choice(USER_AGENTS)


class Opener(urllib.request.FancyURLopener):
    version = None
    
    def __init__(self):
        self.version = random.choice(USER_AGENTS)
        urllib.request.FancyURLopener.__init__(self)
#         FancyURLopener.__init__(self, proxies)


class URLopen(object):
    __opener = None
    __page = None
    __url = None
    
    __pause = None

    __pause_inc_factor = 1.7
    
    __Ntries = None
    
    def __init__(self, tries=10):
        self.__opener = Opener()
#         self.__opener = AnonymousClass(pythonfuckers)
        self.__pause = Pause(1, 2, 0.02, verbose=True)
        
        self.__Ntries = tries
#         FancyURLopener.__init__(self)

    def __del__(self):
        try:
            self.__page.close()
        except AttributeError:
            pass

    def wait(self):
        self.__pause.wait()
        
    def connect(self, url=None):
        # print('URL:', url)
        self.__url = url
        try:
            self.__page.close()
        except AttributeError:
            pass
        else:
            print('connection closed')
        
        self.__page = self.__opener.open(self.__url)
        # print('connected')

    def reconnect(self):
        self.connect(self.__url)
    
    def __pause_inc(self):
        self.__pause.mul(self.__pause_inc_factor)

    def change_ua(self):
        '''
        change User-Agent
        '''
        self.__opener = Opener()

    def get_file(self):
        pass

    def get_html(self):
        i = 0
        
        while i < self.__Ntries:
            self.wait()
            i += 1
            try:
                text = self.__page.read()
            except ValueError:
                print(self.__url)
                self.__pause_inc()
                self.change_ua()
                self.reconnect()
                
                err_msg = 'ERROR in %d st retry' % i
                err_msg = color_text(err_msg, 'red')
                print(err_msg)
                print('retries left: %d' % (self.__Ntries-i))
#                 sys.exit()
            else:
                print('URL:', self.__url)
                msg = 'OK %d st retry SUCCESS' % i
                # if (i > 1) and (i < self.__Ntries / 2.0):
                #     msg = color_text(msg, 'green')
                # if (i >= self.__Ntries / 2.0):
                #     msg = color_text(msg, 'yellow')
                
                print(msg)

                # print('ERROR TEXT')
                # print(text[6860:6940])
                # return text.decode('utf-8', 'replace')
                return text.decode('utf-8')
            
        raise ValueError('None of retries left')


def download2(url):
    filename = url.split('/')[-1]
    download(url, filename)


def download(url, dst):
    req = urllib.request.Request(url)

    ua = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:44.0) Gecko/20100101 Firefox/44.0'
    accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    accept_lang = 'en-US,en;q=0.5'

    req.add_header('User-Agent', ua)
    req.add_header('Accept', accept)
    req.add_header('Accept-Language', accept_lang)

    # gelbooru can raise HTTP 403 (Forbidden) error
    # when we try load pic without Referer
    try:
        page = urllib.request.urlopen(req, None, timeout=5)
    except urllib.error.HTTPError:
        print('403 ERROR')
        # send some food
        req.add_header('Referer', url)
        page = urllib.request.urlopen(req, None, timeout=5)

    file_body = page.read()
    with open(dst, 'wb') as f:
        f.write(file_body)
        print('OK')