CLIENT_ID = '0bcbd1db8ddca3570fa9'
CLIENT_SECRET = '026f27e44b1a07186ebf4ec5fa736cc6bbca5de7'
REDIRECT_URL = 'https://minyattra.appspot.com/users/github/callback'
SCOPE = 'repo,user:email'
AUTH_URL = 'https://github.com/login/oauth/authorize'
ACCESS_TOKEN_URL = 'https://github.com/login/oauth/access_token'
USER_URL = 'https://api.github.com/user?access_token=%s'
USER_EMAILS_URL = 'https://api.github.com/user/emails?access_token=%s'
REPOS_URL = 'https://api.github.com/user/repos?access_token=%s'
GISTS_URL = 'https://api.github.com/gists?access_token=%s'
REPO_STATS_URL = 'https://api.github.com/repos/%s/%s/stats/contributors?access_token=%s'
FOLLOWERS_URL = 'https://api.github.com/users/%s/followers?access_token=%s'