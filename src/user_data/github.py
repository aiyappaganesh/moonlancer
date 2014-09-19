import json
import logging
import urllib2

from google.appengine.api import urlfetch
from google.appengine.ext import deferred

from model.repo import Repo
from model.gist import Gist
import github_config as github

def pull_repos(user, third_party_user):
    response = json.loads(urlfetch.fetch(github.REPOS_URL%third_party_user.access_token).content)
    logging.info(user.name)
    logging.info(third_party_user.access_token)
    for repo in response:
        name, owner, language, forks, stars = repo['name'], repo['owner']['login'], repo['language'], repo['forks_count'], repo['stargazers_count']
        Repo(parent=user, name=name, owner=owner, language=language, forks=forks, stars=stars).put()

def pull_gists(user, third_party_user):
    response = json.loads(urlfetch.fetch(github.GISTS_URL%third_party_user.access_token).content)
    for gist in response:
        comments = gist['comments']
        Gist(parent=user, comments=comments).put()

def pull_data(user, third_party_user):
    deferred.defer(pull_repos, user, third_party_user)
    deferred.defer(pull_gists, user, third_party_user)
