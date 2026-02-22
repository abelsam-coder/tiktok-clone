# TikTok Clone Web App

A simplified TikTok-style social media platform with user authentication, post creation, followers/following system, and real-time interactions using Flask, Socket.IO, and Tailwind CSS.

---

## Table of Contents

1. Features
2. Tech Stack
3. Installation
4. Project Structure
5. Database Tables
6. API Endpoints
7. Authentication & Validation
8. Frontend Design
9. Real-Time Interactions
10. Usage
11. Screenshots & Demo

---

## Features

- User Authentication: Sign up and login with username, email, and password
- Validation & Flash Messages: Signup checks for existing username/email; Login flashes incorrect password or "username not found"
- Session Management: Redirects unauthenticated users to the home page
- Dashboard: Upload posts (image/video), view posts, followers, and following, search posts and users
- Profile: View stats (posts, followers, following) and bio
- Follow/Unfollow: Real-time using Socket.IO
- Responsive Design: Tailwind CSS for modern UI
- 3D Animation: Homepage with Spline interactive 3D visuals
- Database: MySQL via XAMPP
- Flash Messages: Notify users for errors and success

---

## Tech Stack

| Layer       | Technology |
|------------|------------|
| Backend    | Flask, Flask-RESTful, Flask-SocketIO |
| Frontend   | HTML, CSS, JavaScript, Tailwind CSS |
| Database   | MySQL (XAMPP) |
| Real-Time  | Socket.IO |
| Animation  | Spline 3D |

---

# TikTok Clone Web App

A simplified TikTok-style social media platform with user authentication, post creation, followers/following system, and real-time interactions using Flask, Socket.IO, and Tailwind CSS.

---

## Table of Contents

1. Features
2. Tech Stack
3. Installation
4. Project Structure
5. Database Tables
6. API Endpoints
7. Authentication & Validation
8. Frontend Design
9. Real-Time Interactions
10. Usage
11. Screenshots & Demo

---

## Features

- User Authentication: Sign up and login with username, email, and password
- Validation & Flash Messages: Signup checks for existing username/email; Login flashes incorrect password or "username not found"
- Session Management: Redirects unauthenticated users to the home page
- Dashboard: Upload posts (image/video), view posts, followers, and following, search posts and users
- Profile: View stats (posts, followers, following) and bio
- Follow/Unfollow: Real-time using Socket.IO
- Responsive Design: Tailwind CSS for modern UI
- 3D Animation: Homepage with Spline interactive 3D visuals
- Database: MySQL via XAMPP
- Flash Messages: Notify users for errors and success

---

## Tech Stack

| Layer       | Technology |
|------------|------------|
| Backend    | Flask, Flask-RESTful, Flask-SocketIO |
| Frontend   | HTML, CSS, JavaScript, Tailwind CSS |
| Database   | MySQL (XAMPP) |
| Real-Time  | Socket.IO |
| Animation  | Spline 3D |

---




# TikTok Clone Web App - Key Documentation

This section describes the database structure, API endpoints, authentication/validation rules, real-time interaction via Socket.IO, and usage instructions.

---

## Database Tables

| Table       | Columns                                     | Description                     |
|------------ |--------------------------------------------|---------------------------------|
| **User**    | id (PK), username (unique), email (unique), password | Stores user credentials         |
| **Posts**   | id (PK), username, title, caption, post (file path) | Stores all user posts           |
| **Profile** | id (PK), username, bio, profile (image path) | Stores profile info             |
| **Followers** | id (PK), username, follower             | Tracks followers for each user  |

---

## API Endpoints

| Endpoint                        | Method | Description                           |
|---------------------------------|--------|---------------------------------------|
| `/register`                      | POST   | Register new user                      |
| `/login`                         | POST   | Login existing user                    |
| `/dashboard/upload`              | POST   | Upload post (image/video)              |
| `/dashboard/home`                | GET    | Fetch all posts for main feed          |
| `/search?search=`                | GET    | Search posts or users                  |
| `/user/<search>`                 | GET    | Fetch searched user profile            |
| `/dashboard/logout`              | GET    | Logout user (destroy session)          |
| `/dashboard/profile/edit`        | POST   | Edit logged-in user profile            |
| `/dashboard/profile`             | GET    | Get current profile info               |

---

## Authentication & Validation

### Sign Up
- **Fields:** Username, Email, Password
- **Checks:**
  - Username exists → Flash: `Please use another username`
  - Email exists → Flash: `Email already registered`

### Login
- **Fields:** Username, Password
- **Checks:**
  - Incorrect password → Flash: `Incorrect password`
  - Username not found → Flash: `No username found`

### Session Management
- Checks for session cookie on dashboard pages
- Redirects to home page if session invalid

---


# Files


## Real-Time Interactions

- Follow/Unfollow handled via Socket.IO
- Updates follow button dynamically without page reload

```javascript
const followBtn = document.getElementById("followBtn");
if(followBtn){
  const socket = io();
  followBtn.addEventListener("click", () => {
    socket.emit("follow", { follow: "{{ searched_user.username }}" });
  });
  socket.on("follow_status", (data) => {
    if (data.status === "followed") {
      followBtn.textContent = "Unfollow";
      followBtn.classList.replace("from-pink-500","from-gray-500");
    } else {
      followBtn.textContent = "Follow";
      followBtn.classList.replace("from-gray-500","from-pink-500");
    }
  });
}



## Installation

```bash
git clone https://github.com/yourusername/tiktok-clone.git
cd tiktok-clone
python -m venv venv
# Activate environment
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://username:password@localhost/db_name"

set FLASK_APP=app.py

flask db init 
flask db migrate
flask db upgrade

python app.py

tiktok-clone/
│
├─ README.md
├─ requirements.txt
├─ .gitignore
├─ backend/
|   ├─resources/
|     ├─home.py
|     ├─profile.py
|     ├─upload.py
|     ├─user.py
|   ├─routes/   
|     ├─routes.py 
|   ├─app.py
|   ├─config.py
|   ├─extensions.py
|   ├─model.py
├─ frontend/
│   ├─ 404.html
|   ├─ edit.html   
│   ├─ home.html
│   ├─ login.html
│   ├─ main.html
│   ├─ post.html
|   ├─ profile.html
|   ├─ register.html
|   ├─ upload.html
|   ├─ userprofile.html       
├─ upload/
|   ├─ files/
|   ├─ profile/   
├─ document/
|   ├─follow_unfollow.png
|   ├─get_post.png
|   ├─home_page.png
|   ├─loading_effect.png
|   ├─login_page.png
|   ├─profile_edit_page.png
|   ├─profile+page.png
|   ├─registration_page.png
|   ├─search_post.png
|   ├─upload_page.png
|   ├─upload_sample.png
|   ├─xammp.png
|   ├─code.png
|   ├─files.png
└─ config.py






