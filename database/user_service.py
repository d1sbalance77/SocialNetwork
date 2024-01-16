from database.models import User
from database import get_db


def get_all_users_db():
    db = next(get_db())
    all_users = db.query(User).all()

    return all_users


def get_exact_user(user_id):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        return exact_user
    else:
        return 'This user does not exists in DataBase'


def add_new_user_id(name, surname, city, phone_number, birthday, reg_date, email):
    db = next(get_db())

    checker = db.query(User).filter_by(phone_number=phone_number).first()

    if checker:
        return 'This phone number already registered'

    else:
        new_user = User(name=name,
                        surname=surname,
                        city=city,
                        phone_number=phone_number,
                        birthday=birthday,
                        reg_date=reg_date,
                        email=email)


    db.add(new_user)
    db.commit()

    return 'User was successfully registered'


def login_user_db(phone_number, password):
    db = next(get_db())

    user = db.query(User).filter(phone_number=phone_number,password=password).first()

    if user:
        return user
    else:
        return 'Error in authorization'


def edit_user_info_db(user_id,edit_info,new_info):
    db = next(get_db())

    exact_user = get_exact_user(user_id)

    if exact_user:
        if edit_info == 'city':
            exact_user.city = new_info

        elif edit_info == 'name':
            exact_user.name = new_info

        elif edit_info == 'password':
            exact_user.password = new_info


        db.commit()

        return 'Successfully edited'
    else:
        return "Do not successfully edited"



def delete_user_db(user_id):
    db = next(get_db())

    user = db.query(User).filter_by(user_id=user_id).first()

    if user:
        db.delete()
        db.commit()


        return 'User was successfully deleted'
    else:
        return 'User was not successfully deleted'



def upload_profile_photo_db(user_id, photo_path):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        exact_user.profile_photo = photo_path
        db.commit()

        return 'Photo was successfully added'
    else:
        return 'Photo was not successfully added'


def delete_profile_photo_db(user_id):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        exact_user.profile_photo = "None"
        db.commit()

        return 'Photo was successfully deleted'
    else:
        return 'Photo was not successfully deleted'
