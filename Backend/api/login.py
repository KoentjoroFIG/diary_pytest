from fastapi import APIRouter
Router = APIRouter()

credentials = {"username": "Halo", "password": "Bye"}

@Router.post("/login")
def login(username, password):
    if username == credentials["username"] and password == credentials["password"]:
        return "Login successful"
    else:
        return "Login failed"