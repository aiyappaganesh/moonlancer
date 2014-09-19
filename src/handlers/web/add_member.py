import webapp2
from handlers.web import WebRequestHandler
from google.appengine.api import users
import logging

from model.user import User

class AddMemberPage(WebRequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            self.redirect('/member/expose_third_party')
        else:
            self.redirect(users.create_login_url('/member/expose_third_party'))

class ExposeThirdPartyPage(WebRequestHandler):
    def get(self):
        path = 'member/expose_social_data.html'
        user = users.get_current_user()
        User.get_or_insert(key_name=user.email())
        template_values = {'name':user.nickname()}
        self.write(self.get_rendered_html(path, template_values), 200)

app = webapp2.WSGIApplication(
    [
        ('/member/add', AddMemberPage),
        ('/member/expose_third_party', ExposeThirdPartyPage)
    ]
)
