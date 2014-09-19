import logging
import webapp2
import urllib2
import urllib

from google.appengine.ext.webapp import template
from google.appengine.api import urlfetch
from google.appengine.ext import deferred

import github_config as github


def get_github_auth_url():
	params = {'client_id': github.CLIENT_ID, 'redirect_uri': github.REDIRECT_URL, 'scope': github.SCOPE}
	return "%s?%s"%(github.AUTH_URL, urllib.urlencode(params))

class GitHubAuthHandler(webapp2.RequestHandler):
	def get(self):
		template_values = {'github_auth_url' : get_github_auth_url()}
		index_path = 'templates/users/login.html'
		self.response.out.write(template.render(index_path, template_values))

class GitHubCallbackHandler(webapp2.RequestHandler):
	def get(self):
		logging.info(self.request.get('code'))

app = webapp2.WSGIApplication([('/users/github/authorize', GitHubAuthHandler,
								'/users/github/callback', GitHubCallbackHandler)])