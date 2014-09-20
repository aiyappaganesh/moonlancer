from google.appengine.ext import db

class Shot(db.Model):
    views = db.IntegerProperty(indexed=False)
    likes = db.IntegerProperty(indexed=False)
    comments = db.IntegerProperty(indexed=False)
    rebounds = db.IntegerProperty(indexed=False)
    buckets = db.IntegerProperty(indexed=False)
