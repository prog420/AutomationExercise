from dataclasses import dataclass


@dataclass
class User:
    # Account Information
    title: str = None
    name: str = None
    email: str = None
    password: str = None
    days: str = None
    months: str = None
    years: str = None
    newsletter: str = None
    optin: str = None
    # Address Information
    first_name: str = None
    last_name: str = None
    company: str = None
    address: str = None
    address2: str = None
    country: str = None
    state: str = None
    city: str = None
    zipcode: str = None
    mobile_number: str = None
