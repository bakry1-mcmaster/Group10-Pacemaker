# dcm_core/user_manager.py
# - Handles storing and retrieving user credentials.
# - Enforces max 10 users.
# - Provides login authentication logic.

import json
import os
import hashlib

USER_FILE = "users.json"

class UserManager:
    def __init__(self):
        if not os.path.exists(USER_FILE):
            with open(USER_FILE, "w") as f:
                json.dump({}, f)

    def _load_users(self):
        with open(USER_FILE, "r") as f:
            return json.load(f)

    def _save_users(self, users):
        with open(USER_FILE, "w") as f:
            json.dump(users, f)

    def _hash(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self, username, password):
        users = self._load_users()
        if username in users:
            return False, "Username already exists."
        if len(users) >= 10:
            return False, "Maximum 10 users allowed."
        users[username] = self._hash(password)
        self._save_users(users)
        return True, "User registered successfully."

    def login(self, username, password):
        users = self._load_users()
        hashed = self._hash(password)
        return username in users and users[username] == hashed
