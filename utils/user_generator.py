import pytest
from app.api.api_client import APIClient
from utils.user_builder import UserBuilder


class UserGenerator:
    builder = UserBuilder()

    @pytest.fixture()
    def random_valid_user(self):
        api_client = APIClient()
        user = (
            self.builder.reset_user()
            .set_name()
            .set_email()
            .set_password()
            .set_date_of_birth()
            .set_first_name()
            .set_last_name()
            .set_company()
            .set_address_one()
            .set_address_two()
            .set_country()
            .set_state()
            .set_city()
            .set_zipcode()
            .set_phone_number()
            .get_user()
        )
        api_client.create_user(user)
        yield user
        # teardown
        api_client.delete_user()

    @classmethod
    def existing_user_with_valid_creds(cls):
        user = (
            cls.builder.reset_user()
            .set_email(email="aqa.test.420@gmail.com")
            .set_password(password="cmutddsh2304")
            .get_user()
        )
        return user

    @classmethod
    def existing_user_with_incorrect_pass(cls):
        user = (
            cls.builder.reset_user()
            .set_email(email="aqa.test.420@gmail.com")
            .set_password(password="incorrect")
            .get_user()
        )
        return user
