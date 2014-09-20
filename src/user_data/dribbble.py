import json
import logging
import urllib2

from google.appengine.api import urlfetch
from google.appengine.ext import deferred

from model.shot import Shot
import dribbble_config as dribbble

def pull_shots(user, third_party_user):
    response = json.loads(urlfetch.fetch(dribbble.SHOTS_URL%third_party_user.access_token).content)
    for shot in response:
    	views, likes, comments, rebounds, buckets = shot['views_count'], shot['likes_count'], shot['comments_count'], shot['rebounds_count'], shot['buckets_count']
    	Shot(parent=user, views=views, likes=likes, comments=comments, rebounds=rebounds, buckets=buckets).put()

def pull_data(user, third_party_user):
    deferred.defer(pull_shots, user, third_party_user)
