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
    # test()
    # return 0
    print('Kiririn Booru Grabber')
    args = parse_args()
    print('args:')
    pprint(args)

    if args['continue']:
        cont_search()
    else:
        site = args['site']
        tags = args['tags']
        resized = args['resized']
        original = args['original']
        mode = ''
        if resized:
            mode = mode + 'r'
        if original:
            mode = mode + 'o'
        print('mode:', mode)
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
    file1='3579391.txt'
    file2='3527738.txt'
    with open(file2, encoding='utf-8') as f:
        txt = f.read()

    import kiririn_main.parsers.parser as parser
    info = parser.parse_post(txt)
    from pprint import pprint
    pprint(info.has_resized)
    pprint(info.resized_link)
    pprint(info.has_original)
    pprint(info.original_link)

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


def test_job():
    from kiririn_main.search import Job
    job = Job()
    posts = ['https://chan.sankakucomplex.com/post/show/4066098',
 'https://chan.sankakucomplex.com/post/show/4066095',
 'https://chan.sankakucomplex.com/post/show/3919545',
 'https://chan.sankakucomplex.com/post/show/3587366',
 'https://chan.sankakucomplex.com/post/show/3586117',
 'https://chan.sankakucomplex.com/post/show/3579391',
 'https://chan.sankakucomplex.com/post/show/3527738',
 'https://chan.sankakucomplex.com/post/show/3502269',
 'https://chan.sankakucomplex.com/post/show/3397137',
 'https://chan.sankakucomplex.com/post/show/3384707',
 'https://chan.sankakucomplex.com/post/show/3384706',
 'https://chan.sankakucomplex.com/post/show/3000716',
 'https://chan.sankakucomplex.com/post/show/2969256',
 'https://chan.sankakucomplex.com/post/show/2894858',
 'https://chan.sankakucomplex.com/post/show/2782228',
 'https://chan.sankakucomplex.com/post/show/2782223',
 'https://chan.sankakucomplex.com/post/show/2474700',
 'https://chan.sankakucomplex.com/post/show/2474697',
 'https://chan.sankakucomplex.com/post/show/2048286',
 'https://chan.sankakucomplex.com/post/show/2023040']
    # job.write_posts(posts)
    posts2 = job.read_posts()
    pprint(posts2)

if __name__ == '__main__':
    main()
    # sankaku()