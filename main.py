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
    icon = "fa-solid fa-user"
    column_list = [User.id, User.name]
    column_labels = dict(id="ID", name="Name")
    column_searchable_list = [User.name]
    column_sortable_list = [User.id, User.name]
    page_size = 25
    page_size_options = [50, 100]


admin.register_model(UserAdmin)
