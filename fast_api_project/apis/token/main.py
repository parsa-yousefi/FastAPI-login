from fastapi import FastAPI
import uvicorn
from apis.token.routers import token
from apis.token.routers import update_user
from apis.token.routers import create_user

app = FastAPI()

app.include_router(token.router, prefix="/token", tags=["token"])
app.include_router(update_user.router, prefix="/token", tags=["update_user"])
app.include_router(create_user.router, prefix="/token", tags=["create_user"])


host = '127.0.0.1'
port = 8002


if __name__ == "__main__":
    uvicorn.run('apis.token.main:app', host=host, port=port, reload=True)


