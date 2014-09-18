from google.appengine.ext import db

class Repo(db.Model):
    stars = db.IntegerProperty(indexed=False)
    forks = db.IntegerProperty(indexed=False)
    contributors = db.IntegerProperty(indexed=False)
    language = db.StringProperty(indexed=False)
    #origanization = db.StringProperty(indexed=False)
