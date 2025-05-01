🛠️ Open Door — Full-Stack Mental Health Support Platform

Type: Solo Project · Personal / Portfolio
Tech Stack: HTML · CSS · JavaScript · Flask · SQLite · Render · Netlify

💡 Overview
Open Door is an anonymous mental health platform created to give people space to speak freely — especially in their most unheard moments. With no usernames, likes, or followers, it offers a simple space for honesty, presence, and belonging.

🌟 Key Features
📝 Post & Read Messages — Anonymously share what you’re feeling and read messages from others.

    🎨 Minimalist UI — A quiet, clean interface designed for calm emotional presence.

    🔐 Admin Panel (v0.2.2) — Secure backend dashboard to view and delete messages.

    🛡️ Soft Moderation (v0.2.3) — Auto-flags potentially harmful content for admin review.

    🚀 Live Deployment —

        Frontend: Hosted on Netlify

        Backend & DB: Hosted on Render with full API integration

        CI/CD: GitHub-connected with auto-deploy

🔧 Technical Highlights

    RESTful Flask API with CORS and structured JSON handling

    SQLite database with auto-init, timestamps, and content flagging

    Secure content moderation with admin-only access

    Production-ready error handling and environment configs

✨ Motivation
Open Door was built to explore how emotionally intelligent tech can support real people in quiet ways. It’s not about engagement — it’s about being seen and heard.

📜 Creator’s Note
I created Open Door to design, develop, and deploy a complete full-stack application with intention and care. Through it, I learned:

    Backend/API design and database handling

    Troubleshooting real-world deployment issues

    Building for emotional presence over metrics

    Prioritizing accessibility and purpose in design

This project represents both a tool I believe the world needs — and the start of my journey as a developer who builds for impact.

    Welcome Home. Speak Freely. Be Heard.

Built with Flask Frontend Database Stage

---

# 📜 Open Door - Patch Notes

---

## 📦 Changelog

| Version | Date       | Highlights                                                           |
| ------- | ---------- | -------------------------------------------------------------------- |
| v0.2.3  | 2025-04-30 | ✅ Soft moderation, flagged content detection, admin panel updates   |
| v0.2.2  | 2025-04-29 | ✅ Admin tools: message listing, deletion, password key protection   |
| v0.2.1  | 2025-04-28 | ✅ Stable MVP: post and read messages, deployed frontend and backend |

## 🐞 Debugging Lessons & Fixes (v0.2.3)

Throughout development, several issues were encountered and solved. Below are the key debugging insights:

| Issue                                        | Result                                                   | Lesson                                                                                   |
| -------------------------------------------- | -------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Forgot to call `request.get_json()`          | Backend crashed silently when trying to access post data | Always call functions like `get_json()` with parentheses; test APIs with dummy requests. |
| Frontend pointing to 127.0.0.1 in prod       | Fetch requests failed after deployment                   | Use a `BASE_URL` constant and swap between dev/prod with env flags or build scripts.     |
| Missing dependency: flask-cors / gunicorn    | Render deployment failed                                 | Maintain a clean `requirements.txt`; only freeze dependencies after local validation.    |
| 500 Internal Server Error on `/post-message` | Frontend couldn’t parse server response, user saw error  | Use `try/except` around DB inserts and return valid JSON with proper status codes.       |
| Vim commit editor confusion                  | Stuck in terminal, couldn’t commit                       | Use `git commit -m "..."` or change your default Git editor.                             |
| All messages showed FLAGGED tag              | Admin UI falsely marked every message as flagged         | Use conditional rendering; cast data safely with `int(x)` and check flags explicitly.    |
| Logging a variable before defining it        | 500 crash from `UnboundLocalError`                       | Declare and define all variables before using them, especially in logs and responses.    |

## 🛣️ Roadmap

| Version | Planned Features                                                        | Status  |
| ------- | ----------------------------------------------------------------------- | ------- |
| v0.2.4  | 🌐 Admin login form (replace ?key=...) with secure login UI             | Planned |
| v0.2.5  | 📱 Mobile-friendly layout improvements, animation polish                | Planned |
| v0.2.6  | 📊 Admin stats dashboard (message count, % flagged, time trends)        | Planned |
| v0.3.0  | 💬 Anonymous replies: allow users to respond to messages                | Planned |
| v0.3.1  | 🧠 Emotion tagging: auto-label messages by mood using NLP               | Planned |
| v0.3.2  | 🔍 Filter and search for messages by keywords, flag status, and time    | Planned |
| v1.0.0  | 🚀 Public launch with branding, onboarding, and long-term hosting setup | Future  |

## Version: 0.2

**Mission:**  
A safe, anonymous platform for sharing thoughts, struggles, victories, and hopes.

**Core Features:**

- Post anonymous messages
- Read anonymous messages
- Friendly timestamps ("Just now", "5 minutes ago")
- Soft entrance animations
- Responsive mobile and desktop layouts
- About Open Door page
- Clean, calming visual design
- No accounts, no judgment — just presence.

---

**Future Plans:**

- Improve moderation
- Build reply threads
- Enable geolocation tags (optional)
- Integrate volunteer listeners
- Real-time updates (WebSocket)

---

**© 2025 Open Door**

## Version 0.1.0 – "The First Light" 🌅

_(Initial MVP Release)_

---

### 🚀 New Features

- **Backend API (Flask):**

  - `/post-message` endpoint added: Accepts user-submitted messages via POST requests.
  - `/get-messages` endpoint added: Returns all saved messages in JSON format.
  - Messages automatically timestamped with SQLite `CURRENT_TIMESTAMP` feature.

- **Database (SQLite):**

  - Messages saved persistently with `content` and `timestamp` fields.
  - Automatic database creation if `database.db` does not exist.

- **Frontend (HTML/CSS/JavaScript):**

  - **Landing Page** with two main options:
    - [Post a Message]
    - [Read Messages]
  - **Post Message Flow:**
    - Displays a text area for anonymous sharing.
    - Sends message data securely to backend via `fetch()`.
    - Success and error handling with user-friendly alerts.
  - **Read Messages Flow:**
    - Fetches and displays all stored messages.
    - Each message shows content and formatted timestamp.
    - "Back to Home" button allows easy navigation reset.

- **Technical Foundations:**
  - **CORS Enabled:** Full frontend-backend communication across different origins.
  - **Backend and Frontend fully connected:** Functional cross-layer communication.
  - **Error Handling:** Basic error responses for invalid submissions and server communication failures.

---

### 🛠 Improvements

- **UI Enhancements:**

  - Clean minimalist design using CSS.
  - Responsive button layouts.
  - Basic hover effects for buttons.

- **Developer Experience:**
  - Terminal logs incoming posted messages for easy backend monitoring.
  - Modular code structure ready for future scaling.

---

### ⚡ Known Limitations

- Messages are not yet sorted (displayed in insertion order).
- No input validation beyond "non-empty" yet.
- No user authentication (anonymous platform by design at this stage).
- Single-server, local development only (no live hosting yet).

---

# ✨ Notes

- Open Door represents a commitment to **authentic anonymous expression**.
- Built step-by-step with a focus on **presence**, **trust**, and **human connection** over "likes" or "profiles."

---

# 📌 Current Tech Stack

| Layer    | Technology                      |
| :------- | :------------------------------ |
| Backend  | Flask (Python)                  |
| Frontend | HTML / CSS / Vanilla JavaScript |
| Database | SQLite                          |
| Hosting  | Local (localhost)               |

---

🎉 Milestone Unlocked

    First working version live locally ✅

    Real users can post and read anonymous messages ✅

    Full-stack communication achieved ✅

    Backend deployed with auto-redeploy on Render ✅

    Admin panel and moderation tools fully functional ✅

---

### 🧡 Thank you for being part of building Open Door.

---

# 🎉 Status

> 🚧 **Open Door MVP is live for local development!**  
> Real people can post and read messages in real-time.

---

# 🧡

Thank you for believing in raw presence.  
Thank you for building a space the world quietly needs.

---

## 📘 Developer Handbook

For a full reference of key variables, API routes, and database schema, see:

👉 [Download the Open Door Developer Handbook (PDF)](./open-door-dev-handbook.pdf)
