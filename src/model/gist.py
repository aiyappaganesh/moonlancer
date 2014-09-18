from google.appengine.ext import db

class Gist(db.Model):
    comments = db.IntegerProperty(indexed=False)
