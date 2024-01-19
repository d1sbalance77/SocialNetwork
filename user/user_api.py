from fastapi import APIRouter
from user import LoginValidator,RegisterValidator
from database.user_service import login_user_db,add_new_user_db,get_all_users_db

user_router = APIRouter(prefix='/user',tags=['Управление Юзерами'])

@user_router.post('/login')
async def login_user(data: LoginValidator):

    result = login_user_db(**data.model_dump())


    return {'message': result}

@user_router.post('/register')
async def register_user(data: RegisterValidator):

    result = add_new_user_db(**data.model_dump())

    if result:
        return {'message': result}
    else:
        return {'This user already exists'}

@user_router.get('/all_users')
async def all_users():

    all_users = get_all_users_db()

    return all_users

