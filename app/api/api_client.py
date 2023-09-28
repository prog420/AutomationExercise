import requests
from app.models.user import User


class APIClient:
    def __init__(self):
        self.base_url = "https://www.automationexercise.com/"
        self.session = requests.Session()
        self.generate_csrf_token()

    def generate_csrf_token(self):
        self.session.get(self.base_url)

    def get_csrf_token(self):
        return self.session.cookies.get("csrftoken")

    def create_user(self, user: User) -> requests.Response:
        """
        Create user: send POST request to ".../signup" with CSRF-token.
        """
        self.session.headers["Content-Type"] = "application/x-www-form-urlencoded"
        self.session.headers["X-CSRFToken"] = self.get_csrf_token()
        self.session.headers["Origin"] = "https://www.automationexercise.com"
        self.session.headers["Referer"] = "https://www.automationexercise.com/signup"
        self.session.headers["Cookie"] = f"csrftoken={self.get_csrf_token()}; "

        request_data = {
            "csrfmiddlewaretoken": self.get_csrf_token(),
            "title": user.title,
            "name": user.name,
            "email_address": user.email,
            "password": user.password,
            "days": user.days,
            "months": user.months,
            "years": user.years,
            "newsletter": user.newsletter,
            "optin": user.optin,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "company": user.company,
            "address1": user.address,
            "address2": user.address2,
            "country": "United+States",
            "state": user.state,
            "city": user.city,
            "zipcode": str(user.zipcode),
            "mobile_number": str(user.mobile_number),
            "form_type": "create_account",
        }
        request_string = "&".join(
            [f"{key}={value}" for key, value in request_data.items()]
        )
        response = self.session.post(
            url=f"https://www.automationexercise.com/signup",
            data=request_string
        )
        return response

    def delete_user(self) -> requests.Response:
        """
        Delete user: send GET request to ".../delete_account" with
        "sessionid" header.
        """
        if self.session.cookies.get("sessionid"):
            self.session.headers[
                "Cookie"
            ] += f"sessionid={self.session.cookies.get('sessionid')}"

        response = self.session.get(
            url="https://www.automationexercise.com/delete_account"
        )
        return response
