from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException
from apis.token.config import Config
from apis.token.utils.jwt_utils import JWTUtils
from common.database import db_manager
from apis.token.models.create_user_model import CreateRequest
from apis.token.services.update_service import UpdateService
from common.auth_required import get_current_user, is_admin_required
from common.logger import get_logger

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


@router.post("/create_user")
async def create_user(request: CreateRequest, _=Depends(is_admin_required)):
    logger = get_logger('token_create_user')
    try:
        logger.info(f"Token request: {request}")
        user = await UpdateService.register_user(request.username, request.password, request.isAdmin)
        logger.info(f"user {request.username} with {request.password} password created successfully")
        if user is not None:
            return {"status_code": 409, "detail": f"User  already Exists."}
        return {"message": f"User {request.username} Created successfully"}
    except Exception as e:
        logger.error(f"Exception occurred {e}")
        return {"message": "Something went Wrong"}


