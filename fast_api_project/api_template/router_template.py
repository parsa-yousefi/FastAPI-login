router_template = '''from datetime import timedelta
from fastapi import APIRouter, HTTPException, Depends
from common.database import db_manager
from apis.{{ service_name }}.models.{{ router_name }}_model import {{ router_name.capitalize() }}Response,{{ router_name.capitalize() }}Request
from apis.{{ service_name }}.services.{{ router_name }}_service import {{ router_name.capitalize() }}Service
from common.auth_required import get_current_user
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


@router.post("/{{ router_name }}",response_model={{ router_name.capitalize() }}Response)
async def {{ router_name }}(request: {{ router_name.capitalize() }}Request, current_user: str = Depends(get_current_user)):
    logger = get_logger("{{ service_name }}_{{ router_name }}")
    try:
        logger.info(f"request: {request}")
        # Write your code here
        return {"message": current_user}
    except Exception as e:
        logger.error(f"Error massage: {e}")
        return {"message":"error in request", "ErrorCode":500}
'''