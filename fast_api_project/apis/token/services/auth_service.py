from common.database import db_manager
from apis.token.queries.query import get_user_pass
from apis.token.utils.hash_utils import verify_password


class AuthService:
    @staticmethod
    async def authenticate_user(username: str, password: str):
        database = db_manager.get_db()
        user = await database.fetch_one(get_user_pass, {"username": username})
        if user:
            if verify_password(password, user["password"]):
                return {"username": username,
                        "isAdmin": user['isAdmin']}
            else:
                return None
        else:
            return None





