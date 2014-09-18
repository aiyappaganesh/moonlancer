import webapp2
import logging

from model.third_party_user import ThirdPartyUser
from model.user import User
from networks import GITHUB
from user_data import github

class GitHubDataPullHandler(webapp2.RequestHandler):
    def get(self):
        email = self.request.get('email')
        user = User.get_by_key_name(email)
        third_party_user = ThirdPartyUser.get_by_key_name(GITHUB, parent=user)
        github.pull_data(user, third_party_user)

app = webapp2.WSGIApplication([('/users/github/pull', GitHubDataPullHandler)])