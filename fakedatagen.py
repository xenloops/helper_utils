from faker import Faker
import random
import datetime

# Use the Faker library to generate dummy data for well, anything really.
# Usage: python3 fakedatagen.py > fakedata.csv

# create a Faker object
fake = Faker()

# generate 300 random profiles
for i in range(300):
    # generate fake data
    name = fake.first_name()
    surname = fake.last_name()
    address = fake.address()
    phone = fake.phone_number()
    eye_color = random.choice(['Blue', 'Black', 'Green', 'Brown', 'Hazel'])
    hair_color = random.choice(['Blond', 'Grey', 'Brown', 'White', 'Red', 'Multi'])
    fav_color = random.choice(['Blue', 'Green', 'Brown', 'Black', 'White', 'Red', 'Orange'])
    role = fake.job()
    work = fake.company()
    license = fake.license_plate()
    email = fake.ascii_email()
    ssn = ''.join(random.choices('0123456789', k=9))
    birth_date = fake.date_between(start_date='-120y', end_date='-18y')
    card_type = random.choice(['Visa', 'MasterCard', 'American Express'])
    if card_type == 'Visa':
        card_number = fake.credit_card_number(card_type='visa')
    elif card_type == 'MasterCard':
        card_number = fake.credit_card_number(card_type='mastercard')
    else:
        card_number = fake.credit_card_number(card_type='amex')
    card_exp = fake.credit_card_expire()
    card_ccd = fake.credit_card_security_code()
    
    # print the profile
    print(f'{surname},{name},"{address}",{phone}, {eye_color}, {hair_color}, {fav_color}, {role},"{work}",{license},{email},{ssn},{birth_date},{card_number},{card_exp},{card_ccd}')

    
