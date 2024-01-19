from datetime import datetime
from database.models import PostComment
from database import get_db


def add_comment_db(post_id,user_id,comment_text):
    db = next(get_db())
    
    new_comment = PostComment(post_id=post_id,user_id=user_id,comment_text=comment_text)
    
    db.add(new_comment)
    db.commit()
    
    return 'Comment was successfully added'


def delete_comment_db(comment_id):
    db = next(get_db())
    
    exact_post_comment = db.query(PostComment).filter_by(comment_id=comment_id).first()
    
    if exact_post_comment:
        db.delete(exact_post_comment)
        db.commit()
        
        return 'Comment was successfully deleted'
    else:
        return 'This comment does not exists'
    
    
def change_comment_db(comment_id, changed_comment):
    db = next(get_db())

    change_comment = db.query(PostComment).filter_by(comment_id=comment_id,changed_comment=changed_comment).first()

    if change_comment:
        change_comment.comment_text = changed_comment
        db.commit()

        return 'Comment was successfully changed'
    else:
        return False


def get_post_comments(post_id):
    db = next(get_db())

    post_comments = db.query(PostComment).filter_by(post_id=post_id).all()

    return post_comments
