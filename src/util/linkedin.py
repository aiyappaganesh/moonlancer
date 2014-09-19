from google.appengine.api import urlfetch
import urllib
import logging

response_type = 'code'
client_id = '75roiql0j3mfv4'
client_secret='LeW9ypga1UdUo5Ix'
authorization_url = 'https://www.linkedin.com/uas/oauth2/authorization'
scope = 'r_fullprofile'
state = 'karnatakanammarajya'
redirect_uri = 'http://minyattra.appspot.com/users/handle_linkedin_auth'
access_token_url = 'https://www.linkedin.com/uas/oauth2/accessToken'
grant_type = 'authorization_code'

def get_access_token(self):
    resp_code = str(self.request.get('code'))
    resp_state = str(self.request.get('state'))
    if resp_state == state:
        params = {'grant_type': grant_type,
               'code': resp_code,
               'redirect_uri': redirect_uri,
               'client_id': client_id,
               'client_secret': client_secret}
        result = urlfetch.fetch(access_token_url,
            urllib.urlencode(params),
            urlfetch.POST,
            deadline = 60)
        logging.info(result.content)