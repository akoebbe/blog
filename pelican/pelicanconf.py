#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = u'Andrew Koebbe'
SITENAME = u'Andrew Koebbe'
TAGLINE = u'Just another developer with a blog.'
#SITEURL = 'http://blog.andrewkoebbe.com'
SITEURL = 'http://localhost:8000'
COVER_IMG_URL = '/images/cover.jpg'

TIMEZONE = 'America/Chicago'
CURRENT_YEAR = datetime.now().strftime('%Y')

DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = '%B %d, %Y'

PATH = 'content'
ARTICLE_PATHS = ['articles', ]
PAGE_PATHS = ['pages', ]

STATIC_PATHS = ['images', 'static', ]

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ATOM = 'atom.xml'
FEED_RSS = 'rss.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('VML (My employer)', 'http://vml.com/'),)

# Menu Items
MENUITEMS = (
    ('Resume', 'resume'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/profile/view?id=14776117'),
          ('twitter', 'https://twitter.com/andrewkoebbe'),
          ('github', 'https://github.com/vml-akoebbe'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = '../pelican-themes/pure-single'
BOOTSTRAP_THEME = 'flatly'
PYGMENTS_STYLE = 'solarizeddark'
SITELOGO = '/images/logo.svg'
FAVICON_URL = '/images/favicon.ico'
PROFILE_IMG_URL = '/images/headshot.jpg'

TYPOGRIFY = True

# Formatting for urls

PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}/index.html"

ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{slug}/index.html"

CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

AUTHORS_SAVE_AS = False

DISQUS_SITENAME = 'akoebbeblog'

GOOGLE_ANALYTICS = 'UA-51896543-1'