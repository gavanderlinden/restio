from flask import request
from app import app, db
from app.models import User

@app.route("/", methods=["GET"])
def main():
    return "main"

@app.route("/<int:userid>", methods=["GET"])
def get_user(userid):
    if request.method == "GET":
    	q = User.query.filter_by(id=userid)
        return q.all()[0].username

@app.route("/<user>", methods=["POST"])
def add_user(user):
    if request.method == "POST":
        u = User(username=user, pwd="1234")
        db.session.add(u)
        db.session.commit()
        return user + " added"
