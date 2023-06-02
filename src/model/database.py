import sqlalchemy
import databases
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./support.db"

# создаем таблицу в базе данных
metadata = sqlalchemy.MetaData()

requests_table = sqlalchemy.Table(
    "requests",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("date", sqlalchemy.String),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("email", sqlalchemy.String),
    sqlalchemy.Column("message", sqlalchemy.String),
    sqlalchemy.Column("category", sqlalchemy.String),
    sqlalchemy.Column("status", sqlalchemy.String),
)

# настройка подключения к базе данных
database = databases.Database(DATABASE_URL)
engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(bind=engine)
# Удаление таблицы "requests" из базы данных
# requests.drop(engine)

metadata.create_all(engine)
