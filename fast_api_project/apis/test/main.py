from fastapi import FastAPI
from apis.test.routers import test
import uvicorn

app = FastAPI()

app.include_router(test.router, prefix="/test", tags=["test"])


host = '127.0.0.1'
port = 8003


if __name__ == "__main__":
    uvicorn.run('apis.test.main:app', host=host, port=port, reload=True)
