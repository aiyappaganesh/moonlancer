import json
import logging
import urllib2

from google.appengine.api import urlfetch
from google.appengine.ext import deferred

import linkedin_config as linkedin

    '''
    skills = [skill['skill']['name'] for skill in response['skills']['values']] if response['skills']['_total'] > 0 else None
    companies = [position['company']['name'] for position in response['positions']['values']] if response['positions']['_total'] > 0 else None
    schools = [education['educations']['name'] for education in response['educations']['values']] if response['educations']['_total'] > 0 else None
    '''

def pull_data(user, third_party_user):
    response = json.loads(urlfetch.fetch(linkedin.PROFILE_URL%('num-connections,num-recommenders,publications,patents,skills,positions,educations,certifications', third_party_user.access_token)).content)
    connections = response['numConnections']
    recommenders = response['numRecommenders']
    patents = response['patents']['_total'] if 'patents' in response else None
    publications = response['publications']['_total'] if 'publications' in response else None
