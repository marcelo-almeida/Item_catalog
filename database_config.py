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
    description = Column(String(500))
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship("Category", back_populates="item")

    @property
    def serialize(self):
        """Return object to JSON format"""
        return {
            'title': self.title,
            'description': self.description,
            'id': self.id,
            'cat_id': self.category_id
        }

    @property
    def serialize_with_category(self):
        return {
            'title': self.title,
            'description': self.description,
            'id': self.id,
            'category': self.serialize_one2one
        }

    @property
    def serialize_one2one(self):
        return self.category.serialize


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    item = relationship(Item)

    @property
    def serialize_with_item(self):
        """Return object to JSON format"""
        return {
            'name': self.name,
            'id': self.id,
            'item': self.serialize_one2many
        }

    @property
    def serialize(self):
        """Return object to JSON format"""
        return {
            'name': self.name,
            'id': self.id
        }

    @property
    def serialize_one2many(self):
        return [i.serialize for i in self.item]


engine = create_engine('sqlite:///catalog.db')


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    print("Created all tables")
