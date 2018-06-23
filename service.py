from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
from database_config import Base, Category, Item

engine = create_engine('sqlite:///catalog.db',
                       connect_args={'check_same_thread': False})
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


def get_category_list():
    categories = session.query(Category).all()
    return categories


def get_category_by_id(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    return category


def count_items_by_category(category_id):
    count = session.query(Item).filter_by(category_id=category_id).count()
    return count


def get_item_list(category_id, limit):
    if limit:
        items = session.query(Item).order_by(desc('id')).limit(limit)
    else:
        items = session.query(Item).filter_by(category_id=category_id).all()
    return items


def get_item_by_id(item_id):
    item = session.query(Item).filter_by(id=item_id).one()
    return item


def add_new_item(item):
    session.add(item)
    session.commit()


def edit_item_by_id(item):
    session.add(item)
    session.commit()


def delete_item_by_id(item):
    session.delete(item)
    session.commit()


def validate_item(item):
    errors = []
    if not item.title or item.title == '':
        errors.append('invalid title')
    if not item.category_id or item.category_id <= 0:
        errors.append('invalid category')
    return errors
