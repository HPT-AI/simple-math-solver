from fastapi import FastAPI

app = FastAPI(title="User Service")

@app.get("/api/users/me")
def get_current_user():
    """Returns a mock user."""
    return {"user_id": "12345", "username": "testuser", "email": "test@example.com"}
