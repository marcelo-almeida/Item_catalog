from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_config import Category, Base

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


def add_category(category_list):
    for category in category_list:
        session.add(category)
        session.commit()


if __name__ == '__main__':
    # Create default categories
    categories = [
        Category(name="Soccer"),
        Category(name="Basketball"),
        Category(name="Baseball"),
        Category(name="Frisbee"),
        Category(name="Snowboarding"),
        Category(name="Rock Climbing"),
        Category(name="Foosball"),
        Category(name="Skating"),
        Category(name="Hockey")
    ]
    add_category(categories)
    print("Fill database!")
