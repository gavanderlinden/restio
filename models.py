from app import db

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)    
    pwd = db.Column(db.String)

    def __init__(self, username, pwd):
        self.username = username
        self.pwd = pwd
        super(User, self).__init__()
