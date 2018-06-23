from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
from database_config import Base, Category, Item, User

engine = create_engine('sqlite:///catalog.db',
                       connect_args={'check_same_thread': False})
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


def get_category_list():
    """
    :return: all categories
    """
    categories = session.query(Category).all()
    return categories


def get_category_by_id(category_id):
    """
    :param category_id: id of a category
    :return: a specific category
    """
    category = session.query(Category).filter_by(id=category_id).one()
    return category


def count_items_by_category(category_id):
    """
    :param category_id: id of a category
    :return: quantity of items filter by category
    """
    count = session.query(Item).filter_by(category_id=category_id).count()
    return count


def get_item_list(category_id, limit):
    """
    :param category_id: id of a category
    :param limit: limit of returned items
    :return: items
    """
    if limit:
        items = session.query(Item).order_by(desc('id')).limit(limit)
    else:
        items = session.query(Item).filter_by(category_id=category_id).all()
    return items


def get_item_by_id(item_id):
    """
    :param item_id: id of a item
    :return: a specific item
    """
    item = session.query(Item).filter_by(id=item_id).one()
    return item


def add_new_item(item):
    """
    :param item: item to create
    :return: None
    """
    session.add(item)
    session.commit()


def edit_item_by_id(item):
    """
    :param item: item to update
    :return: None
    """
    session.add(item)
    session.commit()


def delete_item_by_id(item):
    """
    :param item: item to delete
    :return: None
    """
    session.delete(item)
    session.commit()


def validate_item(item):
    """
    :param item: item to validate
    :return: None
    """
    errors = []
    if not item.title or item.title == '':
        errors.append('invalid title')
    if not item.category_id or item.category_id <= 0:
        errors.append('invalid category')
    return errors


def create_user(login_session):
    """
    :param login_session: dict with login session
    :return: return id of the user created
    """
    new_user = User(name=login_session['username'],
                    email=login_session['email'])
    session.add(new_user)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user


def get_user_by_id(user_id):
    """
    :param user_id: id of the user
    :return: a specific user
    """
    user = session.query(User).filter_by(id=user_id).one()
    return user


def get_user_by_email(email):
    """
    :param email: email from an user
    :return: a specific user
    """
    try:
        user = session.query(User).filter_by(email=email).one()
        return user
    except:
        return None
