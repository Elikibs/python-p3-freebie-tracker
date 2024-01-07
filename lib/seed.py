#!/usr/bin/env python3

from faker import Faker
from datetime import datetime
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Company, Freebie

if __name__== '__main__':
    engine = create_engine('sqlite:///freebies.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Company).delete()
    session.query(Freebie).delete()

    fake =  Faker()

    companies = []
    for i in range(50):
        company = Company(
            name=fake.unique.name(),
            founding_year= fake.date_between_dates(date_start=datetime(2002, 1, 1), date_end=datetime(2015, 12, 31)).year
        )

        # add and commit individually to get IDs back
        session.add(company)
        session.commit()

        companies.append(company)

    
    freebies = []
    for company in companies:
        for i in range(random.randint(1,5)):
            freebie = Freebie(
                name = fake.name(),
                value = random.randint(100, 1000),
                company_id = company.id,
            )

            freebies.append(freebie)
    
    session.bulk_save_objects(freebies)
    session.commit()
    session.close()
