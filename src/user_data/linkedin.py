import json
import logging
import urllib2

from google.appengine.api import urlfetch
from google.appengine.ext import deferred

import linkedin_config as linkedin

def pull_profile(user, third_party_user):
    response = json.loads(urlfetch.fetch(linkedin.PROFILE_URL%('num-connections,skills', third_party_user.access_token)).content)
    connections = response['numConnections']
    skills = [skill['skill']['name'] for skill in response['skills']['values']]

def pull_data(user, third_party_user):
    deferred.defer(pull_profile, user, third_party_user)
