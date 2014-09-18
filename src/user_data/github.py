import json
import logging
import urllib2

from google.appengine.api import urlfetch
from google.appengine.ext import deferred

from model.repo import Repo

USER_URL = 'https://api.github.com/user?access_token=%s'
REPOS_URL = 'https://api.github.com/user/repos?access_token=%s'
REPO_STATS_URL = 'https://api.github.com/repos/%s/%s/stats/contributors?access_token=%s'
FOLLOWERS_URL = 'https://api.github.com/users/%s/followers?access_token=%s'

def pull_repos(user, third_party_user):
    response = json.loads(urlfetch.fetch(REPOS_URL%third_party_user.access_token).content)
    logging.info(user.name)
    logging.info(third_party_user.access_token)
    for repo in response:
        name, owner, language, forks, stars = repo['name'], repo['owner']['login'], repo['language'], repo['forks_count'], repo['stargazers_count']
        Repo(key_name=name, parent=user, owner=owner, language=language, forks=forks, stars=stars).put()
        '''
        logging.info(name)
        logging.info(owner)
        logging.info(language)
        logging.info(forks)
        logging.info(stars)
        logging.info('####')
        '''

def pull_data(user, third_party_user):
    deferred.defer(pull_repos, user, third_party_user)

