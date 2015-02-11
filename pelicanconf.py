#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Load from cache?
LOAD_CONTENT_CACHE = True

# Personal information
AUTHOR = 'FSFW Dresden'
SITENAME = 'FSFW Dresden'
SITEURL = 'http://www.fsfw-dresden.de'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'de'

# Subfolders are the names for categories
USE_FOLDER_AS_CATEGORY = True

# Path related
PATH = 'content'
# Folder which holds pages (seen from /content/)
PAGE_PATHS = ['pages']
RELATIVE_URLS = True
ARTICLE_URL = '{date:%Y-%m}/{slug}'
ARTICLE_SAVE_AS = '{date:%Y-%m}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

# Theme related
THEME = 'blue-penguin'
DEFAULT_PAGINATION = 5

# Feed related
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('FSFW', 'http://www.fsfw-dresden.de/'),
         ('TU Dresden', 'http://tu-dresden.de'))

# Markdown extension related (syntax highlighting, newline 2 <br>, better
# tables. See https://pythonhosted.org//Markdown/extensions/index.html
MD_EXTENSIONS = ['codehilite(linenums=False, noclasses=True)', 'nl2br', 'tables', 'toc']
