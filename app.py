from flask import Flask, render_template, request, redirect, url_for, session, flash

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import random
from datetime import timedelta
from dotenv import load_dotenv
import os


app = Flask(__name__)
app.secret_key = '123'
app.permanent_session_lifetime = timedelta(days=1) 

load_dotenv()  

uri = os.getenv("MONGO_URI")


client = MongoClient(uri, server_api=ServerApi('1'))
db = client["songRq"]

# Collections
song_requests_collection = db.song_requests
sessions_collection = db.sessions

def generateGuestUsername():
    return "Guest" + "".join(random.choices("0123456789", k=5))

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session_id = request.form.get("session_id")
        password = request.form.get("password")
        username = request.form.get("username")

        print(f"info msg! login")
        print("Received:", session_id, password, username)

        if not username:
            username = generateGuestUsername()

        try:
            # Check if session_id and password exist in the database
            session_data = sessions_collection.find_one({"session_id": session_id, "password": password})
            if not session_data:
                raise Exception("Invalid session ID or password.")

            # Set session
            session.permanent = True
            session["session_id"] = session_id
            session["username"] = username
            print("Session after login:", session)

            return redirect(url_for("request_song"))

        except Exception as e:
            flash(f"{e}", "danger")

    return render_template("login.html")

@app.route("/request", methods=["GET", "POST"])
def request_song():
    print("Got redirected to /request")
    print("Session in request_song:", session)

    if "session_id" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        song = request.form.get("song")
        if not song:
            flash("Please enter a song.", "danger")
            return redirect(url_for("request_song"))

        session_id = session["session_id"]
        username = session["username"]

        print("info msg! Request submitted:")
        print(song, session_id, username)

        try:
            song_requests_collection.insert_one({"session_id": session_id, "song": song, "username": username})
            flash("Song request submitted!", "success")
        except Exception as e:
            flash("An error occurred. Please try again later.", "danger")

        return redirect(url_for("request_song"))

    return render_template("request.html")

@app.route("/logout")
def logout():
    session.clear()  # Properly clear session
    flash("You have been logged out.", "info")  
    return redirect(url_for("login"))

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000)
