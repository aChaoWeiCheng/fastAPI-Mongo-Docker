from fastapi import (
    FastAPI,
    HTTPException,
    status,
    Request,
)
from src.routers import router


app = FastAPI()



# ================= Routers inclusion from src directory ===============
app.include_router(router)