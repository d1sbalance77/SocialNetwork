from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Date
from sqlalchemy.orm import relationship

from database import Base

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String)
    phone_number = Column(Integer, unique=True)
    city = Column(String)
    birthday = Column(Integer)
    profile_photo = Column(String)
    password = Column(String)

    reg_date = Column(DateTime)

class UserPost(Base):
    __tablename__ = 'posts'

    post_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    post_text = Column(String)
    Likes = Column(Integer)

    publish_date = Column(DateTime)

    user_fk = relationship(User, lazy='subquery')


class PostPhoto(Base):
    __tablename__ = 'post_photos'

    photo_id = Column(Integer, primary_key=True, autoincrement=True)
    post_id = Column(Integer, ForeignKey("posts.post_id"))
    photo_path = Column(String)

    post_fk = relationship(UserPost, lazy='subquery')

class PostComment(Base):
    __tablename__ = "post_comments"

    comment_id = Column(Integer, primary_key=True, autoincrement=True)

    post_id = Column(Integer, ForeignKey('posts.post_id'))
    user_id = Column(Integer, ForeignKey('users.user_id'))

    comment_text = Column(String)
    publish_date = Column(Integer)

    user_fk = relationship(User, lazy='subquery')
    post_fk = relationship(UserPost, lazy='subquery')


