import webapp2
from handlers.web import WebRequestHandler

class IndexPage(WebRequestHandler):
    def get(self):
        path = 'landing.html'
        template_values = {}
        self.write(self.get_rendered_html(path, template_values), 200)

class StartupLoginPage(WebRequestHandler):
    def get(self):
        path = 'startup_login.html'
        template_values = {}
        self.write(self.get_rendered_html(path, template_values), 200)

class StartupRegistrationPage(WebRequestHandler):
    def get(self):
        path = 'startup_registration.html'
        template_values = {}
        self.write(self.get_rendered_html(path, template_values), 200)

class AddMemberPage(WebRequestHandler):
    def get(self):
        path = 'add_member.html'
        template_values = {}
        self.write(self.get_rendered_html(path, template_values), 200)

app = webapp2.WSGIApplication(
    [
        ('/', IndexPage),
        ('/startup_login', StartupLoginPage),
        ('/startup_registration', StartupRegistrationPage),
        ('/add_member', AddMemberPage)
    ]
)