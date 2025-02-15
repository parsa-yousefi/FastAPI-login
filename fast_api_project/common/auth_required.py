from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt
from apis.token.utils.jwt_utils import JWTUtils

# OAuth2PasswordBearer for extracting the token from Authorization header
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token/token")


def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    Validate the JWT token and return the authenticated user's information.
    """
    try:
        # Decode the token using the utility
        payload = JWTUtils.decode_token(token)
        username: str = payload.get("sub")
        is_admin: bool = payload.get("isAdmin")
        if not username:
            raise HTTPException(status_code=401, detail="invalid token payload")
        return {"username": username, "is_admin": is_admin}  # Return the username or user data from token
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="invalid token")


async def is_admin_required(current_user: dict = Depends(get_current_user)):
    if not current_user['is_admin']:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='You do not have permission to perform this action'
        )
    return current_user
