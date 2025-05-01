
# 🧠 Open Door – Key Variables and Cross-File References

This document summarizes key variables and concepts that are shared across the frontend and backend of the Open Door app. Keep this handy as the project grows.

---

## 1. `BASE_URL`

**Used in:** `/frontend/app.js`

**Purpose:** Specifies the base API endpoint used for all `fetch()` requests.

```js
const BASE_URL = "https://open-door-backend.onrender.com";
```

- 🔄 Switch to localhost for local development
- ✅ Ensure it matches the backend deployment URL in production

---

## 2. `content`

**Used in:**
- `app.js` (POST request body)
- `app.py` (`data.get('content')`)

**Purpose:** Holds the user's submitted message content.

```js
body: JSON.stringify({ content: message })
```

```python
message = data.get('content', '').strip()
```

- ❗ Must match between frontend and backend for posts to work

---

## 3. `timestamp`

**Used in:**
- SQLite DB: `DEFAULT CURRENT_TIMESTAMP`
- `app.py`: selected in `/get-messages`
- `app.js`: displayed via `formatTimestamp(msg.timestamp)`

**Purpose:** Records when the message was posted and displays a friendly timestamp.

- ⏱️ Format consistently in frontend to avoid display errors

---

## 4. `flagged`

**Used in:**
- SQLite DB schema
- Backend moderation logic
- Admin panel rendering

**Purpose:** Indicates whether a message was flagged by soft moderation.

- Stored as `INTEGER` (0 or 1)
- Cast with `int()` or `!!` as needed

---

## 5. `ADMIN_KEY`

**Used in:** `app.py`, `/admin` and `/delete-message` routes

**Purpose:** Controls access to protected admin functions.

```python
if key != ADMIN_KEY:
    return "Unauthorized", 403
```

- 🔐 Passed via query string `?key=pass1029`
- 🔄 Replace with login auth in future

---

## 🔁 Suggested Improvements

- Move `BASE_URL` and `ADMIN_KEY` into `.env` or config file
- Document payload structures (`{ content: ... }`)
- Add consistent timestamp formatting utils

