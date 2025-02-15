from datetime import datetime, timedelta
import jwt
from apis.token.config import Config


class JWTUtils:
    @staticmethod
    def create_access_token(data: dict, expires_delta: timedelta = None):
        # Create a JWT token.
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=Config.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, Config.SECRET_KEY, algorithm=Config.ALGORITHM)
        return encoded_jwt

    @staticmethod
    def decode_token(token: str):
        # Decode and validate a JWT token.
        payload = jwt.decode(token, Config.SECRET_KEY, algorithms=[Config.ALGORITHM])
        return payload
