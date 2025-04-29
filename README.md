# 🚪 Open Door

📜 Creator's Note
I created Open Door to build a space where honesty matters more than noise.
Through this project, I taught myself how to design, develop, and deploy a full-stack web application — from frontend interface to backend database management.
Along the way, I learned how to troubleshoot real-world deployment issues, refine mobile-first design, and create user experiences focused on emotional presence rather than engagement metrics.
Open Door reflects my belief that technology should serve real human needs.
It also represents the beginning of my journey as a developer — someone who builds with intention, care, and a deep respect for the people who use what I create.

> _Welcome Home. Speak Freely. Be Heard._

![Built with Flask](https://img.shields.io/badge/Built%20With-Flask-blue)
![Frontend](https://img.shields.io/badge/Frontend-HTML%2FCSS%2FJS-yellow)
![Database](https://img.shields.io/badge/Database-SQLite-lightgrey)
![Stage](https://img.shields.io/badge/Stage-MVP-blueviolet)

---

**Open Door** is an anonymous messaging platform built to create **a space for real human expression** — without judgment, likes, or profiles.

In a world that often feels noisy, competitive, and curated, Open Door offers something different:  
a place to simply **be heard**.

Anyone can:

- 📝 **Share a message** from their heart — freely and anonymously.
- 🌎 **Read** what others have shared — moments of hope, hurt, gratitude, and honesty.

No accounts. No followers. No pressure.  
Just _presence_, _listening_, and _belonging_.

---

# ✨ Why Open Door?

> "You are not alone — even when it feels like it."

- A platform for **silent voices**.
- A reminder that **everyone is carrying something unseen**.
- A celebration of **raw, authentic presence** over performance.

Built with love — and the belief that small, quiet acts of honesty can change lives. 🌱

---

# 🚀 Technology Stack

| Layer    | Technology                              |
| :------- | :-------------------------------------- |
| Frontend | HTML / CSS / JavaScript                 |
| Backend  | Flask (Python)                          |
| Database | SQLite                                  |
| Hosting  | Local (localhost, coming soon to cloud) |

---

# 📜 Open Door - Patch Notes

---

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

# 🌟 What's Next (Planned)

- Add sorting (Newest → Oldest).
- Improve UI styling with background visuals and animations.
- Deploy backend and frontend to a public server (e.g., Render, Railway, Vercel).
- Add "time ago" formatting (e.g., "5 minutes ago" instead of full timestamp).

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

# 🎉 Milestone Unlocked

- First working version live locally ✅
- Real users can post and read anonymous messages ✅
- Full-stack communication achieved ✅

---

### 🧡 Thank you for being part of building Open Door.

---

# 📈 Roadmap

- Sort messages (newest to oldest)
- Improve message card design
- Add "posted X minutes ago" formatting
- Deploy online for real-world use

---

# 🎉 Status

> 🚧 **Open Door MVP is live for local development!**  
> Real people can post and read messages in real-time.

---

# 🧡

Thank you for believing in raw presence.  
Thank you for building a space the world quietly needs.
