#!/usr/bin/env python3

'''
Created on 13.12.2014
'''

import sys
import argparse
import kiririn_main.search
from kiririn_main.search import search, cont_search, print_sites, add_posts, BOORU_AWAILABLE
from kiririn_main.grabber import Grabber

from pprint import pprint

def main():
    print('Kiririn Booru Grabber')
    args = parse_args()

    if args['continue']:
        cont_search()
    else:
        if args['site'] is None:
            # -s --site without args:
            # print supported booru
            print_sites()
        else:
            if (args['site']) not in BOORU_AWAILABLE:
                print('Sorry, this site not supported yet...')
            else:
                # if mode don't touched we gonna load all pics we find))
                if (not args['resized']) and (not args['original']):
                    original, resized = True, True
                else:
                    resized = args['resized']
                    original = args['original']

                mode = {
                    'original': original,
                    'resized': resized
                }
                # pprint(mode)

                # add list with posts (post URLs)
                if args['list'] is not False:
                    add_posts(args['list'], args['site'], mode)
                # check out the tags
                elif (args['tags'] is None) or (len(args['tags']) == 0):
                    print('NO TAGS!')
                    sys.exit(-1)
                # OK, RUN!
                else:
                    search(args['site'], args['tags'], mode)

def main2():
    print('Kiririn Booru Grabber')
    args = parse_args()

    grabber = Grabber()

    if args['continue']:
        grabber.cont_search()
    else:
        if args['site'] is None:
            # -s --site without args:
            # print supported booru
            print_sites()
        else:
            if (args['site']) not in BOORU_AWAILABLE:
                print('Sorry, this site not supported yet...')
            else:
                # if mode don't touched we gonna load all pics we find))
                if (not args['resized']) and (not args['original']):
                    original, resized = True, True
                else:
                    resized = args['resized']
                    original = args['original']

                mode = {
                    'original': original,
                    'resized': resized
                }
                # pprint(mode)

                # add list with posts (post URLs)
                if args['list'] is not False:
                    grabber.add_posts(args['list'], args['site'], mode)
                # check out the tags
                elif (args['tags'] is None) or (len(args['tags']) == 0):
                    print('NO TAGS!')
                    sys.exit(-1)
                # OK, RUN!
                else:
                    grabber.search(args['site'], args['tags'], mode)

def parse_args():
    parser = argparse.ArgumentParser(description='Kiririn Booru Grabber')

    parser.add_argument('-s', '--site',
                        help='Site where you want to grab pics',
                        nargs='?',
                        default=False,
                        required=False)

    parser.add_argument('-c', '--continue',
                        help='Continue processing the job',
                        nargs='?',
                        const=True,
                        default=False,
                        required=False)

    parser.add_argument('-o', '--original',
                        help='Load original pics only (not resized). Disabled by default (loading all).',
                        nargs='?',
                        const=True,
                        default=False,
                        required=False,
                        type=bool
                        )

    parser.add_argument('-r', '--resized',
                        help='Load resized pics only (not original). Disabled by default (loading all).',
                        nargs='?',
                        const=True,
                        default=False,
                        required=False,
                        type=bool
                        )

    parser.add_argument('-p', '--pool',
                        help='Pool you want to load',
                        default=False,
                        required=False
                        )

    parser.add_argument('-l', '--list',
                        help='List of post urls you want to load pics',
                        default=False,
                        required=False
                        )

    parser.add_argument('-t', '--tags',
                        # nargs='*',
                        nargs=argparse.REMAINDER,
                        help='Picture tags, example: game_cg',
                        required=False)

    args = vars(parser.parse_args())
    return args



def test_print_post(info):
    print('HAS ORIG:', info.has_original)
    print('ORIG:', info.original_link)
    print('ORIG SIZE:', info.original_size)
    print('HAS ORIG2:', info.has_original2)
    print('ORIG2:', info.original_link2)
    print('ORIG SIZE2:', info.original_size2)
    print('HAS RESIZED:', info.has_resized)
    print('RESIZED:', info.resized_link)
    print('RESIZED RES:', info.resized_res)
    print('RATING:', info.rating)
    print('ID:', info.post_id)
    print('POSTED:', info.posted)
    print('POSTED AGO:', info.posted_ago)
    pprint('tags')
    # pprint(info.tags)

def test_booru_file():
    post_file = '3579391.txt'
    # post_file = '194838.txt'
    from kiririn_main.parser import BooruParser
    parser = BooruParser('sankaku')
    with open(post_file) as pf:
        txt = pf.read()
    info = parser.parse_post(txt)
    test_print_post(info)


def test_main():
    search('sankaku', ['shiramine_rika', 'aoyama_sumika', 'winter_clothes'], mode={'original': True, 'resized': True})

if __name__ == '__main__':
    main2()

    # test_main()
    # test_konachan()
    # test_konachan_search()
    # test()
    # sankaku()
    # test_sankaku()