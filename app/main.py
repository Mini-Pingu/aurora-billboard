from typing import Dict
from fastapi import Depends, FastAPI

from routers import tasks

app = FastAPI()

app.include_router(tasks.router)


@app.get("/")
async def admin() -> Dict[str, str]:
    return {"message": "Hello, world!"}
