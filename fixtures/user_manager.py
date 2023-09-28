import pytest
from app.api import APIClient
from app.models import User


class UserManager:
    def __init__(self):
        self.api_client = APIClient()
        self._user = None

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user: User):
        self._user = user

    def create_user(self, user: User):
        self.user = user
        self.api_client.create_user(user)

    def teardown(self):
        if self.user is not None:
            self.api_client.delete_user()


@pytest.fixture(scope="function")
def user_manager():
    """
    Fixture to provide user management options (create user via API call) with
    teardown (delete user after the test).
    """
    um = UserManager()
    yield um
    um.teardown()
