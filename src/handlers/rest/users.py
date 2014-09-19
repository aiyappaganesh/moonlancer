import webapp2
from webapp2 import RequestHandler
from model.third_party_user import ThirdPartyUser
from model.user import User
from networks import GITHUB
from user_data import github

class GitHubDataPullHandler(RequestHandler):
    def get(self):
        email = self.request.get('email')
        user = User.get_by_key_name(email)
        third_party_user = ThirdPartyUser.get_by_key_name(GITHUB, parent=user)
        github.pull_data(user, third_party_user)

app = webapp2.WSGIApplication([('/api/users/github/pull', GitHubDataPullHandler)])
