from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_config import Category, Base, User

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create default user
user = User(name="bob", email="bob@fakemail.com")
session.add(user)
session.commit()


def add_category(category_list):
    for category in category_list:
        session.add(category)
        session.commit()


# Create default categories
categories = [
    Category(user_id=1, name="Soccer"),
    Category(user_id=1, name="Basketball"),
    Category(user_id=1, name="Baseball"),
    Category(user_id=1, name="Frisbee"),
    Category(user_id=1, name="Snowboarding"),
    Category(user_id=1, name="Rock Climbing"),
    Category(user_id=1, name="Foosball"),
    Category(user_id=1, name="Skating"),
    Category(user_id=1, name="Hockey")
]


if __name__ == '__main__':
    add_category(categories)
    print("Fill database!")
