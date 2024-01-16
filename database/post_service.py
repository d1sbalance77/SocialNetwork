from database.models import PostPhoto,UserPost
from database import get_db

def get_all_posts():
    db = next(get_db())
    all_posts = db.query(UserPost).all()

    return all_posts

