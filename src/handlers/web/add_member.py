import webapp2
from handlers.web import WebRequestHandler
from google.appengine.api import users

class AddMemberPage(WebRequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            self.redirect('/member/expose_third_party')
        else:
            self.redirect(users.create_login_url('/member/expose_third_party'))

class ExposeThirdPartyPage(WebRequestHandler):
    def get(self):
        user = users.get_current_user()
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, ' + user.nickname())

app = webapp2.WSGIApplication(
    [
        ('/member/add', AddMemberPage),
        ('/member/expose_third_party', ExposeThirdPartyPage)
    ]
)
