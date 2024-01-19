from database.models import PostPhoto,UserPost,User
from database import get_db

def get_all_posts():
    db = next(get_db())
    all_posts = db.query(UserPost).all()

    return all_posts


def get_exact_post_db(post_id):
    db = next(get_db())

    exact_post = db.query(User).filter_by(post_id=post_id).first()

    if exact_post:
        return exact_post
    else:
        return 'This post does not exists'


def add_new_post_db(photo_id,post_id,photo_path):
    db = next(get_db())

    checker = db.query(User).filter_by(photo_id=photo_id).first()

    if checker:
        return 'This photo was already posted'
    else:
        new_post = User(photo_id=photo_id,
                        post_id=post_id,
                        photo_path=photo_path)

        db.add(new_post)
        db.commit()

        return 'Post was successfully added'

def edit_post_text_db(post_id, post_text):
    pass
