import logging
import webapp2
import urllib2
import urllib
import json

from google.appengine.ext.webapp import template
from google.appengine.api import urlfetch
from google.appengine.ext import deferred

import github_config as github
import dribbble_config as dribbble
from model.third_party_user import ThirdPartyUser
from model.user import User
from networks import GITHUB

from util import linkedin

def get_github_auth_url():
	params = {'client_id': github.CLIENT_ID, 'redirect_uri': github.REDIRECT_URL, 'scope': github.SCOPE}
	return "%s?%s"%(github.AUTH_URL, urllib.urlencode(params))

def get_github_access_token_url(code):
	params = {'code': code, 'client_id': github.CLIENT_ID, 'client_secret': github.CLIENT_SECRET}
	return "%s?%s"%(github.ACCESS_TOKEN_URL, urllib.urlencode(params))

def get_dribbble_auth_url():
	params = {'client_id': dribbble.CLIENT_ID, 'redirect_uri': dribbble.REDIRECT_URL, 'scope': dribbble.SCOPE}
	return "%s?%s"%(dribbble.AUTH_URL, urllib.urlencode(params))

def fetch_and_save_github_user(access_token):
	response = json.loads(urlfetch.fetch(github.USER_EMAILS_URL%access_token).content)
	for email in response:
		if email['primary']:
			logging.info(email['email'])
			user = User.get_by_key_name(email['email'])
	if not user:
		user = User(key_name=email['email'])
		user.put()
	response = json.loads(urlfetch.fetch(github.USER_URL%access_token).content)
	id, followers = response['login'], response['followers']
	ThirdPartyUser(key_name=GITHUB, parent=user, access_token=access_token, id=id, followers=followers).put()

class GitHubAuthHandler(webapp2.RequestHandler):
	def get(self):
		template_values = {'github_auth_url' : get_github_auth_url()}
		index_path = 'templates/users/login.html'
		self.response.out.write(template.render(index_path, template_values))

class GitHubCallbackHandler(webapp2.RequestHandler):
	def get(self):
		code = self.request.get('code')
		response = urlfetch.fetch(get_github_access_token_url(code)).content
		access_token = response.split('&')[0].split('=')[1]
		logging.info(access_token)
		fetch_and_save_github_user(access_token)

class LinkedInAuthHandler(webapp2.RequestHandler):
    def get(self):
        linkedin.get_access_token(self)

class DribbbleAuthHandler(webapp2.RequestHandler):
	def get(self):
		template_values = {'dribbble_auth_url' : get_dribbble_auth_url()}
		index_path = 'templates/users/login.html'
		self.response.out.write(template.render(index_path, template_values))

class DribbbleCallbackHandler(webapp2.RequestHandler):
	def get(self):
		code = self.request.get('code')
		params = {'code': code, 'client_id': dribbble.CLIENT_ID, 'client_secret': dribbble.CLIENT_SECRET}
		response = json.loads(urlfetch.fetch(dribbble.ACCESS_TOKEN_URL, payload=urllib.urlencode(params), method=urlfetch.POST).content)
		access_token = response['access_token']
		logging.info(access_token)

app = webapp2.WSGIApplication([	('/users/github/authorize', GitHubAuthHandler),
								('/users/github/callback', GitHubCallbackHandler),
								('/users/dribbble/authorize', DribbbleAuthHandler),
								('/users/dribbble/callback', DribbbleCallbackHandler),
								('/users/handle_linkedin_auth', LinkedInAuthHandler)])