import webapp2
from webapp2 import RequestHandler
from model.third_party_user import ThirdPartyUser
from model.user import User
from networks import GITHUB
from user_data import github
from util import linkedin

class GitHubDataPullHandler(RequestHandler):
    def get(self):
        email = self.request.get('email')
        user = User.get_by_key_name(email)
        third_party_user = ThirdPartyUser.get_by_key_name(GITHUB, parent=user)
        github.pull_data(user, third_party_user)

class LinkedInAuthHandler(RequestHandler):
    def get(self):
        linkedin.get_access_token(self)

app = webapp2.WSGIApplication([('/users/github/pull', GitHubDataPullHandler),
                               ('/users/handle_linkedin_auth', LinkedInAuthHandler)])
