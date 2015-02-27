'''
Created on 13.12.2014
'''

from urllib.request import FancyURLopener
import random 

from kiririn_main.web.ua import USER_AGENTS

from kiririn_main.main import Pause
from kiririn_main.main import color_text


def get_ua():
    return random.choice(USER_AGENTS)


class Opener(FancyURLopener):
    version = None
    
    def __init__(self):
        self.version = random.choice(USER_AGENTS)
        FancyURLopener.__init__(self)
#         FancyURLopener.__init__(self, proxies)


class URLopen(object):
    __opener = None
    __page = None
    __url = None
    
    __pause = None

    __pause_inc_factor = 1.7
    
    __N_attempts = None
    
    def __init__(self):
        self.__opener = Opener()
#         self.__opener = AnonymousClass(pythonfuckers)
        self.__pause = Pause(2, 4, 0.02, verbose=True)
        
        self.__N_attempts = 20
#         FancyURLopener.__init__(self)

    def __del__(self):
        try:
            self.__page.close()
        except AttributeError:
            pass

    def wait(self):
        self.__pause.wait()
        
    def connect(self, url=None):
        #print('URL:', url)
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
    
    def pause_inc(self):
        self.__pause.mul(self.__pause_inc_factor)

    def change_ua(self):
        '''
        change User-Agent
        '''
        self.__opener = Opener()
    
    def get_html(self):
        i = 0
        
        while i < self.__N_attempts:
            self.wait()
            i += 1
            try:
                text = self.__page.read()
            except ValueError:
                print(self.__url)
                self.pause_inc()
                self.change_ua()
                self.reconnect()
                
                err_msg = 'ERROR in %d st retry'%i 
                err_msg = color_text(err_msg, 'red')
                print(err_msg)
                print('retries left: %d'%(self.__N_attempts-i))
#                 sys.exit()
            else:
                print('URL:', self.__url)
                msg = 'OK %d st retry SUCCESS' % i
                if (i > 1) and (i < self.__N_attempts / 2.0):
                    msg = color_text(msg, 'green')
                if (i >= self.__N_attempts / 2.0):
                    msg = color_text(msg, 'yellow')                
                
                print(msg)

                # print('ERROR TEXT')
                # print(text[6860:6940])
                # return text.decode('utf-8', 'replace')
                return text.decode('utf-8')
            
        raise ValueError('None of retries left')

