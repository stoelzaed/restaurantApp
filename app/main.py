
from fastapi import FastAPI
from app.routes.productes import router as productes_router

app = FastAPI()
app.include_router(productes_router)
