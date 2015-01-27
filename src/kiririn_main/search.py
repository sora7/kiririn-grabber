'''
Created on 13.12.2014
'''

from pprint import pprint

from kiririn_main.web.opener import URLopen
from kiririn_main.job import Job

import kiririn_main.parsers.parser as parser

def search(site, tags, mode=''):
    # sankaku parser
    # import kiririn_main.parsers.parser as parser

    url = parser.query_url(tags)
    job = Job()
    job.site = site
    job.tags = tags
    job.load_mode = mode

    # return 0
    find_posts(parser, url)
    process_posts(parser)


def cont_search():
    job = Job()
    # if job.next == '':
    #     print('Nothing to continue!')
    #     job.clear()
    #     sys.exit(-1)
        # TODO: try make next_url form query_url and start

    # parser = job.site

    if not job.search_done:
        url = job.next
        find_posts(parser, url)
        process_posts(parser)
    else:
        process_posts(parser)


def find_posts(parser, url):
    opener = URLopen()
    opener.connect(url)
    html_text = opener.get_html()

    job = Job()

    search_info = parser.parse_search(html_text)
    if search_info.has_posts:
        posts = search_info.posts
        job.write_posts(posts)

    if search_info.has_next:
        next_url = search_info.next
        job.next = next_url
        find_posts(parser, next_url)
    else:
        job.search_done = True


def process_posts(parser):
    job = Job()
    # parser = job.site
    posts = job.read_posts()
    count = job.post_count

    last_post = job.last_post

    while (last_post < count):
        print('Processing post %s of %s'%(last_post+1, count))
        post_url = posts[last_post]
        opener = URLopen()
        opener.connect(post_url)
        html_text = opener.get_html()

        pic_info = parser.parse_post(html_text)
        job.write_pic(pic_info)

        last_post += 1
        job.last_post = last_post

    job.extract_pics()



