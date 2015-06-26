'''
Created on 13.12.2014
'''

from pprint import pprint

import sys

from grabber.web.opener import URLopen
from grabber.job import Job
from grabber.parser import BooruParser

BOORU_AWAILABLE = (
    'sankaku',
    'konachan'
)

def print_sites():
    print('BOORU GRAB AVAILABLE FROM:')
    print('sankaku')
    print('konachan')


def search(site, tags, mode=''):
    job = Job()
    job.new_job()

    job.site = site
    job.tags = tags
    job.load_mode = mode

    parser = BooruParser(job.site)
    url = parser.query_url(tags)

    find_posts(parser, url)
    process_posts(parser)


def cont_search():
    job = Job()
    parser = BooruParser(job.site)

    if job.next == '':
        if job.site == '' or job.tags == []:
            print('Nothing to continue!')
            job.clear()
            sys.exit(-1)

        url = parser.query_url(job.tags)
        job.next = url

    if not job.search_done:
        url = job.next
        find_posts(parser, url)
        process_posts(parser)
    else:
        process_posts(parser)


def add_posts(posts_file, site, mode=''):
    job = Job()
    job.search_done = True
    job.add_posts(posts_file)
    job.site = site
    job.load_mode = mode

    parser = BooruParser(job.site)
    process_posts(parser)


def find_posts(parser, url):
    # pprint('FIND POSTS')
    opener = URLopen()
    opener.connect(url)
    html_text = opener.get_html()

    job = Job()

    search_info = parser.parse_search(html_text)

    if search_info.has_posts:
        posts = search_info.posts
        # pprint(posts)
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
        percent = round(float(last_post)/count*100, 4)
        print('Processing post %s of %s [%s %s'%(last_post+1, count, percent, '%]'))

        post_url = posts[last_post]
        opener = URLopen()
        opener.connect(post_url)
        html_text = opener.get_html()

        pic_info = parser.parse_post(html_text)
        job.write_pic(pic_info)

        last_post += 1
        job.last_post = last_post

    job.extract_pics()
    job.extract_posts()
    job.extract_job()



