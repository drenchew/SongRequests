🎶 Song Requests App 🎶
Overview

Welcome to the Song Requests App! This web app allows users to log in (either as a guest or with their own session ID and password), submit song requests, and view their requests.

The backend is built using Flask and the data is stored in MongoDB Atlas. The app also uses Flask-CORS for handling cross-origin requests and Dotenv for securely loading environment variables.
🚀 Features

    Login/Registration: Users can log in with their credentials or as a guest.
    Submit Song Requests: After logging in, users can submit song requests.
    Session Management: Each user gets a unique session ID to track their activity.
    MongoDB: Song requests and user sessions are stored in a MongoDB database.

🛠 Technologies Used

    Flask: The web framework used to build the backend of the app.
    MongoDB Atlas: Cloud database used to store song requests and user sessions.
    Flask-CORS: Used for handling cross-origin requests in the app.
    Dotenv: Loads environment variables from the .env file to keep sensitive data secure.
    HTML/CSS: For the frontend user interface.

🏗 Installation and Setup
Prerequisites

To run this project, make sure you have the following installed on your machine:

    Python 3.x
    MongoDB Atlas account for database storage
    Git for version control

Setup Steps

    Clone the repository:

git clone https://github.com/drenchew/SongRequestsApp.git
cd SongRequestsApp

Install required dependencies:

pip install -r requirements.txt

Set up MongoDB Atlas:

    Create an account on MongoDB Atlas.
    Create a cluster and get your MongoDB connection URI.
    Set the connection URI in a .env file as MONGO_URI.

Example .env file:

MONGO_URI=your-mongo-uri-here

Run the app:

    python app.py

    The app will be available at http://127.0.0.1:5000/ by default.

🌐 Deployment

Deploy on renderer.com

For deployment, make sure to set the MONGO_URI environment variable for the MongoDB connection on your cloud provider's settings panel.
🗺 API Routes
/ (Login Page)

    Method: GET, POST
    Description: Users can log in with their session ID and password or use a guest account.

/request (Song Request Page)

    Method: GET, POST
    Description: Allows logged-in users to submit their song requests. Displays a form for submitting songs.

/logout (Logout Page)

    Method: GET
    Description: Logs the user out and clears their session.

🗄 MongoDB Collections

    song_requests: Stores the song requests made by users. Fields:
        session_id: The unique ID of the user's session.
        song: The requested song's title.
        username: The name of the user who submitted the request.
    sessions: Stores session data for users. Fields:
        session_id: A unique session identifier.
        password: The password used for login.

🛠 Troubleshooting
1. MongoDB Connection Issues

    Ensure that the MONGO_URI in the .env file is correct.
    Make sure your IP address is whitelisted in MongoDB Atlas for secure connections.

2. Flask App Not Running

    Ensure all dependencies are installed by running:

    pip install -r requirements.txt

    Check if your .env file is properly configured with MONGO_URI.

3. Page Not Loading After Login

    Open the browser’s developer tools and check for any errors in the JavaScript console or network requests.

🤝 Contributing

We welcome contributions! Here’s how you can get started:

    Fork the repository.
    Create a new branch:

git checkout -b feature/your-feature-name

Make your changes.
Commit your changes:

git commit -am 'Add new feature'

Push to your branch:

    git push origin feature/your-feature-name

    Open a Pull Request.

📜 License

This project is licensed under the MIT License. See the LICENSE file for details.
