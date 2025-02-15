from common.database import db_manager
from apis.token.queries.query import get_user_pass, create_user
from apis.token.utils.hash_utils import hash_password
from fastapi import HTTPException


class UpdateService:
    @staticmethod
    async def register_user(username: str, password: str, isAdmin: bool = False):
        database = db_manager.get_db()
        user = await database.fetch_one(get_user_pass, {"username": username})
        if user:
            return user

        hashed_password = hash_password(password)
        await database.execute(create_user,
                               {"username": username,
                                "password": hashed_password,
                                "isAdmin": isAdmin
                                })

