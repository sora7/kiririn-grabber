'''
Created on 13.12.2014
'''

import random
import time

import sys

SYSTEM_OS = sys.platform

COLOR_MAP = {
    'darkgrey'  : '\033[90m',
    'red'       : '\033[91m',
    'green'     : '\033[92m',
    'yellow'    : '\033[93m',
    'blue'      : '\033[94m',
    'purple'    : '\033[95m',
    'lightblue' : '\033[96m',
    'white'     : '\033[97m',
    'grey'      : '\033[98m'
}
COLOR_MAP_END = '\033[0m'


def color_text(text, color):
    '''
    make colored text in linux terminal
    '''
    if SYSTEM_OS == 'linux2':
        try:
            return '%s%s%s'%(COLOR_MAP[color], text, COLOR_MAP_END)
        except KeyError:
            return text
    else:
        return text


def drange(a, b, step):
    '''
    like range(), but for double
    '''
    r = a
    while r < b:
            yield r
            r += step


class Pause(object):
    '''
    we have to pause post or search processing
    '''
    __wait_time = []
    __verbose = False
    
    def __init__(self, begin=1, end=5, step=0.1, verbose=False):
        '''
        from 1 to 5 means we go to bed for a some time bigger than 1 second and 
        less 5, for example 4.2 seconds
        '''
        self.__wait_time = [float('%g'%i) for i in drange(begin, end, step)]
        self.__verbose = verbose
                
    def wait(self):
        t = random.choice(self.__wait_time)
        if self.__verbose:
            print('pause for %f sec.'%(t))
        time.sleep(t)
        
    def mul(self, factor):
        '''
        multiplying sleep interval        
        '''
        self.__wait_time = list(map(lambda x: x * factor, self.__wait_time))


