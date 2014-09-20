import webapp2
import logging

from model.third_party_user import ThirdPartyUser
from model.user import User
from networks import GITHUB, DRIBBBLE, LINKEDIN
from user_data import github, dribbble, linkedin


networks = {
	GITHUB: github,
	DRIBBBLE: dribbble,
	LINKEDIN: linkedin
}

class GitHubDataPullHandler(webapp2.RequestHandler):
    def get(self):
        email = self.request.get('email')
        user = User.get_by_key_name(email)
        third_party_user = ThirdPartyUser.get_by_key_name(GITHUB, parent=user)
        github.pull_data(user, third_party_user)

class UserDataPullHandler(webapp2.RequestHandler):
	def get(self):
		network = self.request.get('network')
		email = self.request.get('email')
		user = User.get_by_key_name(email)
		third_party_user = ThirdPartyUser.get_by_key_name(network, parent=user)
		networks[network].pull_data(user, third_party_user)

app = webapp2.WSGIApplication([	('/api/users/github/pull', GitHubDataPullHandler),
								('/api/users/pull_data', UserDataPullHandler)])
