#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Zach Norman'
SITENAME = 'Norman-Schuelke Matrimony'
SITEURL = ''
THEME = 'theme/attila'
HEADER_COVER = 'images/znh2.jpg'

PLUGIN_PATHS = ['plugins/pelican-plugins']

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
         ('Map', 'https://goo.gl/maps/VKrQS5jgDPYW9jSF9'),
         ('Hotel', 'https://www.hilton.com/en/book/reservation/deeplink/?ctyhocn=MSPSTDT&groupCode=CDTNWS&arrivaldate=2021-09-24&departuredate=2021-09-26&cid=OM,WW,HILTONLINK,EN,DirectLink&fromId=HILTONLINKDIRECT'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
PLUGINS = [
  'sitemap',
  'neighbors',
  'events'
]

PLUGIN_EVENTS = {
'ics_fname': 'calendar.ics',
}

