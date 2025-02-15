from datetime import timedelta
from fastapi import APIRouter, HTTPException
from apis.token.config import Config
from apis.token.utils.jwt_utils import JWTUtils
from common.database import db_manager
from common.logger import get_logger
from apis.token.models.token_model import TokenResponse, TokenRequest
from apis.token.services.auth_service import AuthService

router = APIRouter()


# Dont Change This
######################################
@router.on_event("startup")
async def startup():
    db_manager.mysql_connection()
    await db_manager.db_start()


@router.on_event("shutdown")
async def shutdown():
    await db_manager.db_stop()
######################################


# Add Your Code In This Section
@router.post("/token")
async def token(request: TokenRequest):
    logger = get_logger('token_token')
    try:
        logger.info(f"Token request: {request}")
        user = await AuthService.authenticate_user(request.username, request.password)
        if not user:
            logger.error(f"invalid username or password: {request.username}, {request.password}")
            return {"Error": "Invalid username or password", "ErrorCode": 401}
            # raise HTTPException(status_code=401, detail="Incorrect username or password")

        access_token = JWTUtils.create_access_token(
            data={"sub": request.username,
                  "isAdmin": user["isAdmin"]},
            expires_delta=timedelta(minutes=Config.ACCESS_TOKEN_EXPIRE_MINUTES)
        )
        logger.info(f"Generated access token: {request.username}")
        return {"access_token": access_token, "token_type": "bearer"}
    except Exception as e:
        logger.error(f"Error while generating access token: {e}")
        return {"error": "Failed to generate access", "ErrorCode": 500}

