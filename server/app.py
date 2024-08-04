from dotenv import load_dotenv

load_dotenv()

import os
from urllib.parse import urljoin

from bs4 import BeautifulSoup
import flask
from pymongo import MongoClient
import requests

app = flask.Flask(__name__)
MONGODB_URI = os.environ['MONGODB_URI']
PAGE_URL = os.environ['PAGE_URL']
WIKI_BASE_URL = os.environ['WIKI_BASE_URL']
USER_AGENT = 'nb-wtf/1.0 <audiodude@gmail.com>'


def update_db(mapping):
  client = MongoClient(MONGODB_URI)
  client.nbwtf.links.drop()

  for slug, url in mapping.items():
    client.nbwtf.links.insert_one({'slug': slug, 'url': url})


@app.route('/api/v1/on_update')
def update():
  print('on_update')

  resp = requests.get(PAGE_URL, headers={'User-Agent': USER_AGENT})
  resp.raise_for_status()

  soup = BeautifulSoup(resp.text, 'html.parser')

  mapping = {}
  table = soup.find('table', {'class': 'wikitable'})
  for row in table.find_all('tr'):
    cols = row.find_all('td')
    if not cols:
      continue
    slug, url = cols[0].text, cols[1].text
    mapping[slug] = url

  update_db(mapping)

  return 'Updated!'


@app.route('/<slug>')
def redirect(slug):
  client = MongoClient(MONGODB_URI)
  link = client.nbwtf.links.find_one({'slug': slug})
  if not link:
    flask.abort(404)

  final_link = link['url']
  if not final_link.startswith('http'):
    final_link = urljoin(WIKI_BASE_URL, final_link)

  return flask.redirect(final_link)
