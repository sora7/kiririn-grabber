#!/usr/bin/env python3

'''
Created on 13.12.2014
'''

import sys
import argparse
import kiririn_main.search
from kiririn_main.search import search, cont_search
from pprint import pprint


def main():
    print('Kiririn Booru Grabber')
    args = parse_args()
    print('args:')
    pprint(args)

    if args['continue']:
        cont_search()
    else:
        site = args['site']
        tags = args['tags']
        if (not args['resized']) and (not args['original']):
            original, resized = True, True
        else:
            resized = args['resized']
            original = args['original']
        mode = {
            'original' : original,
            'resized' : resized
        }

        # print('mode:', mode)
        # return 0
        search(site, tags, mode)
    #


def parse_args():
    parser = argparse.ArgumentParser(description='Kiririn Booru Grabber')

    parser.add_argument('-s', '--site',
                        help='Site where you want to grab pics',
                        required=True)

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
                        required=False
                        )

    parser.add_argument('-r', '--resized',
                        help='Load resized pics only (not original). Disabled by default (loading all).',
                        nargs='?',
                        const=True,
                        default=False,
                        required=False
                        )

    parser.add_argument('-p', '--pool',
                        help='Pool you want to load',
                        required=False
                        )

    parser.add_argument('-t', '--tags',
                        nargs='*',
                        help='Picture tags, example: game_cg',
                        required=True)

    args = vars(parser.parse_args())
    return args

def test():
    print('test!')
    file1='3579391.txt'
    file2='3527738.txt'
    with open(file2, encoding='utf-8') as f:
        txt = f.read()

    # import kiririn_main.parsers.parser as parser
    # info = parser.parse_post(txt)

    from kiririn_main.parser import BooruParser
    parser = BooruParser('sankaku')
    info = parser.parse_post(txt)

    from pprint import pprint
    pprint(info.has_resized)
    pprint(info.resized_link)
    pprint(info.has_original)
    pprint(info.original_link)

def test_konachan():
    post_file = '181642.txt'
    post_file = '195178.txt'
    # post_file = '194838.txt'
    from kiririn_main.parser import BooruParser
    parser = BooruParser('konachan')
    with open(post_file) as pf:
        txt = pf.read()
    info = parser.parse_post(txt)
    print('ORIG:', info.original_link)
    print('ORIG SIZE:', info.original_size)
    print('ORIG2:', info.original_link2)
    print('ORIG SIZE2:', info.original_size2)
    print('RESIZED:', info.resized_link)
    print('RESIZED RES:', info.resized_res)
    print('RATING:', info.rating)
    print('ID:', info.post_id)
    print('POSTED:', info.posted)
    print('POSTED AGO:', info.posted_ago)
    pprint('tags')
    pprint(info.tags)


def sankaku():
    # print(sys.platform)

    from kiririn_main.search import search
    from kiririn_main.parsers import parser

    # with open('search.html', encoding='utf-8') as f:
    #     txt = f.read()
    # info = parser.parse_search(txt)
    # pprint(info.posts)


    with open('file_lol.html', encoding='utf-8') as f:
        txt = f.read()
    info = parser.parse_post(txt)

    print()
    print('has res:', info.has_resized)
    print('res:', info.resized_link)

    # pprint.pprint(info.next)
    # pprint.pprint(info.posts)

    # search(sankaku, ['shiramine_rika', 'aoyama_sumika'])


if __name__ == '__main__':
    main()
    # test_konachan()
    # test()
    # sankaku()