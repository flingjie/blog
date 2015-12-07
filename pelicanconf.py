#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'flingjie'
SITENAME = u"Jie's Blog"
SITEURL = ''

DISPLAY_CATEGORIES_ON_MENU = False

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'ch'

GOOGLE_ANALYTICS = 'UA-71093531-1'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
        )

# Social widget
SOCIAL = (('github', 'https://github.com/flingjie'),
         )

DEFAULT_PAGINATION = 10

#顶部菜单项
MENUITEMS = [
            ('Archives',SITEURL+'/archives.html'),
            ('Algorithm',SITEURL+'/category/algorithm.html'),
            ('Clojure',SITEURL+'/category/clojure.html'),
            ('Emacs',SITEURL+'/category/emacs.html'),
            ('Note',SITEURL+'/category/note.html'),
            ('Python',SITEURL+'/category/python.html'),
            ]
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}
