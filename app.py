from flask import Flask, render_template, request, redirect, url_for, session, flash
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import random
from datetime import timedelta
from dotenv import load_dotenv
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.secret_key = '123'
app.permanent_session_lifetime = timedelta(days=1)

load_dotenv()


print("STARTING THE APP DEBUGG")


uri = os.getenv("MONGO_URI")
print(f"Debug: Loaded Mongo URI: {uri}")  

client = None
db = None

try:
    if not uri:
        raise Exception("MONGO_URI not loaded from environment variables.")

    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client["songRq"]

    if not db:
        raise Exception("Failed to initialize the database.")

    # Collections
    song_requests_collection = db.song_requests
    sessions_collection = db.sessions

    print("Debug: MongoDB connected successfully.") 

except Exception as e:
    print(f"Error: Database connection failed: {e}")
    client = None  


def generateGuestUsername():
    guest_username = "Guest" + "".join(random.choices("0123456789", k=5))
    print(f"Debug: Generated guest username: {guest_username}")  
    return guest_username

@app.route("/", methods=["GET", "POST"])
def login():
    print("Debug: Login function started.")  

    if request.method == "POST":
        session_id = request.form.get("session_id")
        password = request.form.get("password")
        username = request.form.get("username")

        print(f"Debug: Received login data: session_id={session_id}, password={password}, username={username}")

        if not username:
            username = generateGuestUsername()

        print(f"Debug: Collections in DB: {db.list_collection_names()}")

        try:
            if not client or not db:
                raise Exception("Database connection not initialized.")

            session_data = sessions_collection.find_one({"session_id": session_id, "password": password})
            print(f"Debug: Session data found: {session_data}")

            if not session_data:
                raise Exception("Invalid session ID or password.")

            session.permanent = True
            session["session_id"] = session_id
            session["username"] = username

            print(f"Debug: Login successful. Session data: {session}")

            return redirect(url_for("request_song"))

        except Exception as e:
            print(f"Error: Login failed: {e}")
            flash(f"Error: {e}", "danger")

    return render_template("login.html")

@app.route("/request", methods=["GET", "POST"])
def request_song():
    print("Debug: request_song function started.") 
    print(f"Debug: Session data: {session}")

    if "session_id" not in session:
        print("Debug: No session found. Redirecting to login.")  
        return redirect(url_for("login"))

    if request.method == "POST":
        song = request.form.get("song")
        if not song:
            flash("Please enter a song.", "danger")
            return redirect(url_for("request_song"))

        session_id = session["session_id"]
        username = session["username"]

        print(f"Debug: Song request received: song={song}, session_id={session_id}, username={username}")

        try:
            if not client or not db:
                raise Exception("Database connection not initialized.")

            song_requests_collection.insert_one({"session_id": session_id, "song": song, "username": username})
            flash("Song request submitted!", "success")
            print("Debug: Song request successfully inserted into database.") 

        except Exception as e:
            print(f"Error: Song request failed: {e}")
            flash(f"An error occurred: {e}", "danger")

        return redirect(url_for("request_song"))

    return render_template("request.html")

@app.route("/logout")
def logout():
    print("Debug: Logout function started.")  
    session.clear()
    flash("You have been logged out.", "info")
    print("Debug: Session cleared. Redirecting to login.") 
    return redirect(url_for("login"))

if __name__ == "__main__":
    print("Debug: Flask app starting.")  
    app.run(host='0.0.0.0', port=5000)  
