booru_data = {
    'QUERY_PREFIX' : '',
    'TAG_SEP' : '+',
    #search
    #if we want to del smtng before grab posts ('popular' section on sankakuclannel for example)
    'DEL_TEXT' : False,
    'DEL_REGEX' : '',

    'NEXT_REGEX' : '',
    'NEXT_PREFIX' : '',

    'POST_REGEX' : '',
    'POST_PREFIX' : '',
    #post
    'POST_ID_REGEX' : '<li>Id: (\d*?)</li>',
    'TAGS_REGEX' : '<li class="tag-link tag-type.*?" data-name="(.*?)" data-type=".*?"',

    # 'POSTED_REGEX' : '<li>Posted: <a href="/post?tags=date%3A\d{4}-\d{2}-\d{2}" title="(.*?)">.*?</a>.*?</li>',
    # 'POSTED_AGO_REGEX' : '<li>Posted: <a href="/post?tags=date%3A\d{4}-\d{2}-\d{2}" title=".*?">(.*?)</a>.*?</li>',
    #
    # 'PIC_RESIZE_REGEX' : '<img alt=".*?".*?src="(http://konachan.com/image/.*?)".*?>',
    # 'PIC_RESIZE_RES_REGEX' : '<li>Size: (\d*?x\d*?)</li>',

    'POSTED_REGEX' : '',
    'POSTED_AGO_REGEX' : '',

    'PIC_RESIZE_REGEX' : '',
    'PIC_RESIZE_RES_REGEX' : '',

    'PIC_RESIZE_PREFIX' : '',

    'PIC_ORIG_REGEX' : '<li><a class="original-file-changed" href="(http://konachan.com/[^ ]*?/[^ ]*?)" id="highres">Download larger version [(].*? [KM]B.*?[)]</a>',
    'PIC_ORIG_RES_REGEX' : '',
    'PIC_ORIG_SIZE_REGEX' : '<li><a class="original-file-changed" href="http://konachan.com/[^ ]*?/[^ ]*?" id="highres">Download larger version [(](.*? [KM]B).*?[)]</a>',
    'PIC_ORIG_PREFIX' : '',

    'PIC_ORIG2' : True,
    'PIC_ORIG2_REGEX' : '<li><a class="original-file-unchanged" href="(http://konachan.com/image/[^ ]*?/[^ ]*?)".*?[(].*? [KM]B.*?[)]</a>',
    'PIC_ORIG2_RES_REGEX' : '',
    'PIC_ORIG2_SIZE_REGEX' : '<li><a class="original-file-unchanged" href="http://konachan.com/image/[^ ]*?/[^ ]*?".*?[(](.*? [KM]B).*?[)]</a>',
    'PIC_ORIG2_PREFIX' : '',

    'RATING_REGEX' : '<li>Rating: ([^ ]*?) <span class="vote-desc"></span></li>'
}
