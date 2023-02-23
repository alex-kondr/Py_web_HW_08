from faker import Faker

import connect
from models import User


faker = Faker()

for _ in range(10):
    
    User(
        fullname=faker.name(),
        email=faker.email(),
        phone_number=faker.phone_number()
    ).save()