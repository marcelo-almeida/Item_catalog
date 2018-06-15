from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    picture = Column(String(255))


class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(String(500), nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'))


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    item_id = Column(Integer, ForeignKey('item.id'))
    user = relationship(User, foreign_keys=[user_id])
    item = relationship(Item, foreign_keys=[item_id])


engine = create_engine('sqlite:///catalog.db')


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    print("Created all databases")
