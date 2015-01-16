'''
Created on 13.12.2014
'''

class SearchInfo(object):
    __has_next = False
    __next = ''
    __has_posts = False
    __posts = []
    __total_count = 0
    
    def __init__(self):
        self.__has_next = False
        self.__next = ''
        self.__has_posts = False
        self.__posts = []
        self.__total_count = 0

    def __str__(self, *args, **kwargs):
        c_name = self.__class__.__name__

        get_name = lambda item: item.replace('_%s__'%c_name, '').replace('_', ' ')
        
        pairs = []
        for prop in self.__dict__.keys():
            val = self.__dict__[prop]
            if prop == '_%s__%s'%(c_name,'posts'):
                val = len(val)
            pairs.append('%s: %s'%(get_name(prop), val))

        _str = '\n'.join(sorted(pairs))
        return _str

    @property
    def has_next(self):
        return self.__has_next
    
    @has_next.setter
    def has_next(self, value):
        self.__has_next = value
        
    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, value):
        self.__next = value             

    @property
    def has_posts(self):
        return self.__has_posts
    
    @has_posts.setter
    def has_posts(self, value):
        self.__has_posts = value
        
    @property
    def posts(self):
        return self.__posts
    
    @posts.setter
    def posts(self, value):
        self.__posts = value 
        
    @property
    def total_count(self):
        return self.__total_count
    
    @total_count.setter
    def total_count(self, value):
        self.__total_count = value 
        
                

class PostInfo():
    __has_original = False
    __has_resized = False
    __original_link = ''
    __original_size = ''
    __original_res = ''
    __posted = ''
    __posted_ago = ''
    __rating = ''
    __resized_link = ''
    __resized_res = ''
    __source = ''
    __tags = []
    __post_id = ''
    
    
    def __init__(self):
        self.__has_original = False
        self.__has_resized = False
        self.__original_link = ''
        self.__original_size = ''
        self.__original_res = ''
        self.__posted = ''
        self.__posted_ago = ''
        self.__rating = ''
        self.__resized_link = ''
        self.__resized_res = ''
        self.__source = ''
        self.__tags = []
        self.__post_id = ''
        
    def __str__(self, *args, **kwargs):
        c_name = self.__class__.__name__

        get_name = lambda item: item.replace('_%s__'%c_name, '').replace('_', ' ')
        
        pairs = []
        for prop in self.__dict__.keys():
            pairs.append('%s: %s'%(get_name(prop), self.__dict__[prop]))
        
        _str = '\n'.join(sorted(pairs))
        return _str
        
    @property
    def has_original(self):
        return self.__has_original
    
    @has_original.setter
    def has_original(self, value):
        self.__has_original = value
    
    @property
    def has_resized(self):
        return self.__has_resized
    
    @has_resized.setter
    def has_resized(self, value):
        self.__has_resized = value
    
    @property
    def original_link(self):
        return self.__original_link
    
    @original_link.setter
    def original_link(self, value):
        self.__original_link = value
    
    @property
    def original_size(self):
        return self.__original_size
    
    @original_size.setter
    def original_size(self, value):
        self.__original_size = value
    
    @property
    def original_res(self):
        return self.__original_res
    
    @original_res.setter
    def original_res(self, value):
        self.__original_res = value
    
    @property
    def posted(self):
        return self.__posted
    
    @posted.setter
    def posted(self, value):
        self.__posted = value
    
    @property
    def posted_ago(self):
        return self.__posted_ago
    
    @posted_ago.setter
    def posted_ago(self, value):
        self.__posted_ago = value
    
    @property
    def rating(self):
        return self.__rating
    
    @rating.setter
    def rating(self, value):
        self.__rating = value
        
    @property
    def resized_link(self):
        return self.__resized_link
    
    @resized_link.setter
    def resized_link(self, value):
        self.__resized_link = value
    
    @property
    def resized_res(self):
        return self.__resized_res
    
    @resized_res.setter
    def resized_res(self, value):
        self.__resized_res = value
    
    @property
    def source(self):
        return self.__source
    
    @source.setter
    def source(self, value):
        self.__source = value
        
    @property
    def tags(self):
        return self.__tags
    
    @tags.setter
    def tags(self, value):
        self.__tags = value
        
    @property
    def post_id(self):
        return self.__post_id
    
    @post_id.setter
    def post_id(self, value):
        self.__post_id = value       
       
        