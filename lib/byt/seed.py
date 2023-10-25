from faker import Faker
from random import choice as rc
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from main import (Area, Equipment, User)

fake = Faker()


engine = create_engine("sqlite:///main.db")
session = Session(engine, future=True)

def delete_records():
    session.query(Area).delete()
    session.query(Equipment).delete()
    session.query(User).delete()
    session.commit()

def create_records():
    # Klin'iT_users
    gender = ["M","F"]
    position = ["Supervisor", "Team lead", "Hygiene-clerk"]
    users = [User(
            first_name=f'{fake.first_name()}',
            last_name=f'{fake.last_name()}',
            gender=rc(gender),
            position=rc(position)
        ) for i in range(60)]

    # area or duty location 
    duty = ["Morning", "Afternoon", "Night", "Off-duty"]
    location = ["Factory A", "Factory B", "Factory C", "Office", "Loading-bay", "Restroom", "Reception", "Warehouse", "Canteen", "External"]
    areas = [Area(
        duty = rc(duty),
        location = rc(location),
        user_id = fake.random_int(min=1, max=60)
    ) for i in range(60)]

    # equipment
    equipment_types = ["Scrubbing-machine", "Vaccum-sucker", "Pressure-washer", "Telescopic-pole", "Mops", "Squee-gee", "soft-brush", "Glass-cleaner", "Drain-rods", "Truck", "Grass-Trimer", "Scaffolding", "K-rod"]
    equipments = [Equipment(
        type = rc(equipment_types),
        user_id = fake.random_int(min=1, max=60)
    ) for i in range(60)]

    session.add_all(users + areas + equipments)
    session.commit()
    return users, areas, equipments

def relate_records(users, areas, equipments):
    for user in users:
        user.area = rc(areas)
        user.equipment = rc(equipments)
    
    session.add_all(users)
    session.commit()

if __name__ == "__main__":
    delete_records()
    create_records()


    session.close()
    session.commit()
