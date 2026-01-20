# user_auth.py

users = {
    "admin": "admin123",
    "user": "user123"
}

def login(username, password):
    if username in users and users[username] == password:
        print("Login successful")
        return True
    else:
        print("Invalid credentials")
        return False

# Sample test
login("admin", "admin123")
