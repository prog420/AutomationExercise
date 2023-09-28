import datetime

from faker import Faker

from app.models.user import User


class UserBuilder:
    faker = Faker()

    def __init__(self):
        self.user = User()

    def get_user(self):
        return self.user

    def set_name(self, username: str = None, length=20):
        if username is not None:
            self.user.name = username
        else:
            self.user.name = self.faker.pystr(min_chars=length, max_chars=length)
        return self

    def set_email(self, email: str = None):
        if email is not None:
            self.user.email = email
        else:
            self.user.email = self.faker.email()
        return self

    def set_password(
        self,
        password: str = None,
        length: int = 10,
        special_chars: bool = True,
        digits: bool = True,
        upper_case: bool = True,
        lower_case: bool = True,
    ):
        if password is not None:
            self.user.password = password
        else:
            self.user.password = self.faker.password(
                length=length,
                special_chars=special_chars,
                digits=digits,
                upper_case=upper_case,
                lower_case=lower_case,
            )
        return self

    def set_date_of_birth(self, maximum_age: int = 115):
        date_of_birth: datetime.date = self.faker.date_of_birth(
            maximum_age=maximum_age
        )
        self.user.years = date_of_birth.year
        self.user.months = date_of_birth.month
        self.user.days = date_of_birth.day
        return self

    def set_first_name(self, first_name: str = None, length: int = None):
        if first_name is not None:
            self.user.first_name = first_name
        else:
            self.user.first_name = (
                self.faker.first_name()
                if length is None
                else self.faker.pystr(min_chars=length, max_chars=length)
            )
        return self

    def set_last_name(self, last_name: str = None, length: int = None):
        if last_name is not None:
            self.user.last_name = last_name
        else:
            self.user.last_name = (
                self.faker.last_name()
                if length is None
                else self.faker.pystr(min_chars=length, max_chars=length)
            )
        return self

    def set_company(self, company: str = None):
        self.user.company = self.faker.company() if company is None else company
        return self

    def set_address_one(self, address: str = None):
        self.user.address = self.faker.address() if address is None else address
        return self

    def set_address_two(self, address: str = None):
        self.user.address2 = self.faker.address() if address is None else address
        return self

    def set_country(self, country: str = None):
        self.user.country = self.faker.country() if country is None else country
        return self

    def set_state(self, state: str = None):
        self.user.state = self.faker.state() if state is None else state
        return self

    def set_city(self, city: str = None):
        self.user.city = self.faker.city() if city is None else city
        return self

    def set_zipcode(self, zipcode: str = None):
        self.user.zipcode = self.faker.zipcode() if zipcode is None else zipcode
        return self

    def set_phone_number(self, phone_number: str = None):
        self.user.mobile_number = (
            self.faker.phone_number() if phone_number is None else phone_number
        )
        return self

    def reset_user(self):
        self.user = User()
        return self
