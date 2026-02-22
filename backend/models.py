from extensions import db

class User(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       username = db.Column(db.String(50), unique=True, nullable=False)  # Must have length
       email = db.Column(db.String(100), unique=True, nullable=False)
       password = db.Column(db.String(255), nullable=False)
       def __str__(self):
              self.username

class Posts(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       username = db.Column(db.String(50))
       title = db.Column(db.String(50))
       caption = db.Column(db.String(400))
       post = db.Column(db.String(200))
       def __str__(self):
              self.username

class Profile(db.Model):
       id = db.Column(db.Integer,primary_key=True)
       username = db.Column(db.String(50)) 
       bio = db.Column(db.String(500))
       profile = db.Column(db.String(200))
       def __str__(self):
              return self.username  

class Followers(db.Model):
       id = db.Column(db.Integer,primary_key=True)
       username = db.Column(db.String(50)) 
       follower = db.Column(db.String(50))
       def __str__(self):
              return self.username

