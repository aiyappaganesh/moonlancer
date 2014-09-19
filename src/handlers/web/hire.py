import webapp2
from handlers.web import WebRequestHandler

class CriteriaPage(WebRequestHandler):
    def get(self):
        path = 'hire/criteria.html'
        template_values = {}
        self.write(self.get_rendered_html(path, template_values), 200)

app = webapp2.WSGIApplication(
    [
        ('/hire/criteria', CriteriaPage)
    ]
)