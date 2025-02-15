from fastapi import APIRouter, Depends
from common.auth_required import get_current_user

router = APIRouter()


@router.post("/test", dependencies=Depends(get_current_user))
def hello_world():
    return {"message": "yes you are authorized"}


