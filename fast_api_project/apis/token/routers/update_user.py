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


@router.post("/update_user")
def get_token():
    pass
