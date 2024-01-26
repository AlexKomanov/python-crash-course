# https://pypi.org/   # Repository

from faker import Faker
import requests

fake = Faker()

print(fake.name())
print(fake.address())
