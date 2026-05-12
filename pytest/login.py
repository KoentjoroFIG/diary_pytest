import pytest
from Backend.api import login


class loginpage:
    def test_login_successful(self):
        assert login.login("halo", "bye") == "Login successful"

    def test_login_unsuccessful(self):
        assert login.login("null", "null") == "Login failed"









