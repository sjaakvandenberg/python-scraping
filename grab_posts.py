#!/usr/bin/env python
# grab_posts.py
# A simple Python scraper
#
# Sjaak van den Berg
# @svdb

import lxml.html
import scraperwiki
import requests
import sys
import arrow
import re
import textwrap

# filter = sys.argv[1]

sites = ['http://svdb.co']

for url in sites:

    html = requests.get('http://svdb.co').content
    dom = lxml.html.fromstring(html)

    site_title = dom.cssselect('title')[0].text_content()
    print('\nWebsite : ' + site_title)
    print('URL     : ' + url)
    print('=' * 79)

    for entry in dom.cssselect('article'):
        time = entry.cssselect('time')[0].attrib['datetime']
        excerpt = entry.cssselect('p')[0].text_content().strip()
        post = {
            'title': entry.cssselect('h2 a')[0].text_content().strip(),
            'date': entry.cssselect('time')[0].text_content().strip(),
            'time_ago': arrow.get(time).humanize(),
            'excerpt': textwrap.fill(excerpt, 69).replace('\n', '\n\t  '),
            'link': entry.cssselect('h2 a')[0].get('href')
        }

        print('Title   : ' + post['title'])
        print('Date    : ' + post['date'] + ' (' + post['time_ago'] + ')')
        print('URL     : ' + url + post['link'])
        print('Excerpt : ' + post['excerpt'])
        print('-' * 79)
