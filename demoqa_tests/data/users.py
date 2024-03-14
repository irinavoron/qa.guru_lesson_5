from dataclasses import dataclass
import datetime
from enum import Enum


class Gender(Enum):
    male = 'Male'
    female = 'Female'
    other = 'Other'


class Hobby(Enum):
    sports = 'Sports'
    reading = 'Reading'
    music = 'Music'


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    phone_number: str
    birth_date: datetime.date
    subject: str
    hobby: Hobby
    file: str
    address: str
    state: str
    city: str


student = User(first_name='firstName',
               last_name='lastName',
               email='email@example.com',
               gender=Gender.female.value,
               phone_number='1234567890',
               birth_date=datetime.date(1985, 4, 18),
               subject='English',
               hobby=Hobby.sports.value,
               file='picture.jpg',
               address='Some Street, 1',
               state='NCR',
               city='Delhi'
               )
