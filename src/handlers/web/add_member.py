import webapp2
from handlers.web import WebRequestHandler
from google.appengine.api import users

class AddMemberPage(WebRequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('Hello, ' + user.nickname())
        else:
            self.redirect(users.create_login_url(self.request.uri))

app = webapp2.WSGIApplication(
    [
        ('/add_member', AddMemberPage)
    ]
)
