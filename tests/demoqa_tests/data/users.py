from dataclasses import dataclass


@dataclass
class User:
    full_name: str
    email: str
    current_address: str
    permanent_address: str


student = User(
    full_name='FirstName LastName',
    email='student@example.com',
    current_address='Current Address',
    permanent_address='Permanent Address'
)
