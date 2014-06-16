#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = u'Andrew Koebbe'
SITENAME = u'Andrew Koebbe'
SITEURL = 'http://blog.andrewkoebbe.com'

TIMEZONE = 'America/Chicago'
CURRENT_YEAR = datetime.now().strftime('%Y')

DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = '%B %d, %Y'

PATH = 'content'
ARTICLE_DIR = 'articles'
PAGE_DIR = 'pages'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('VML (My employer)', 'http://vml.com/'),)

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/profile/view?id=14776117'),
          ('Twitter', 'https://twitter.com/andrewkoebbe'),
          ('Github', 'https://github.com/vml-akoebbe'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = '../themes/tuxlite_tbs'

TYPOGRIFY = True

# Formatting for urls

ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{slug}/index.html"

CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

AUTHORS_SAVE_AS = False

DISQUS_SITENAME = 'akoebbeblog'

GOOGLE_ANALYTICS = True