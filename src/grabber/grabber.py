import sys

from grabber.job import Job
from grabber.parser import BooruParser
from grabber.web.opener import URLopen

from pprint import pprint

class Grabber(object):
    job = None
    opener = None
    parser = None

    def __init__(self):
        self.job = Job()

    def search(self, site, tags, mode=''):
        self.job.new_job()

        self.job.site = site
        self.job.tags = tags
        self.job.load_mode = mode

        self.parser = BooruParser(self.job.site)
        url = self.parser.query_url(tags)

        self.find_posts(url)

        self.process_posts()

    def cont_search(self):
        self.parser = BooruParser(self.job.site)

        if self.job.next == '':
            if self.job.site == '' or self.job.tags == []:
                print('Nothing to continue!')
                self.job.clear()
                sys.exit(-1)

            url = self.parser.query_url(self.job.tags)
            self.job.next = url

        if not self.job.search_done:
            url = self.job.next
            self.find_posts(url)
            self.process_posts()
        else:
            self.process_posts()

    def add_posts(self, posts_file, site, mode=''):
        # append or add to clear job
        self.job.new_job()

        self.job.search_done = True
        self.job.add_posts(posts_file)
        self.job.site = site

        # filename to tags
        self.job.tags = [posts_file]

        self.job.load_mode = mode

        self.parser = BooruParser(self.job.site)
        self.process_posts()

    def find_posts(self, url):
        opener = URLopen()
        opener.connect(url)
        html_text = opener.get_html()

        search_info = self.parser.parse_search(html_text)

        if search_info.has_posts:
            posts = search_info.posts
            self.job.write_posts(posts)

        if search_info.has_next:
            next_url = search_info.next
            self.job.next = next_url
            self.find_posts(next_url)
        else:
            self.job.search_done = True

    def process_posts(self):
        # job = Job()
        # parser = job.site
        posts = self.job.read_posts()
        count = self.job.post_count

        last_post = self.job.last_post

        while last_post < count:
            percent = round(float(last_post)/count*100, 4)
            print('Processing post %s of %s [%s %s'%(last_post+1, count, percent, '%]'))

            post_url = posts[last_post]

            opener = URLopen()
            opener.connect(post_url)
            html_text = opener.get_html()

            pic_info = self.parser.parse_post(html_text)
            self.job.write_pic(pic_info)

            last_post += 1
            self.job.last_post = last_post

        self.job.extract_pics()
        self.job.extract_posts()
        self.job.extract_job()

