
import uvicorn as uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

# from models import download_models

from pages.router import router_pages
from pages.user_request import user_router

app = FastAPI(title="Занятие №4. Прием обращений граждан")

app.mount("/static", StaticFiles(directory="static"), name="static")

# скачиваем модели при необходимости
# download_models()

# Разрешаем запросы CORS от любого источника
origins = ["*"]  # Для простоты можно разрешить доступ со всех источников
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(router_pages)

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=5020, reload=True)
