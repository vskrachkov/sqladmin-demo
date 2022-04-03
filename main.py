from fastapi import FastAPI
from sqladmin import Admin, ModelAdmin
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine(
    "sqlite:///example.db",
    connect_args={"check_same_thread": False},
)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)


Base.metadata.create_all(engine)


app = FastAPI()
admin = Admin(app, engine)


class UserAdmin(ModelAdmin, model=User):
    column_list = [User.id, User.name]


admin.register_model(UserAdmin)
