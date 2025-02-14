from typing import List






from sqlalchemy import string, ForeignKey,Table, Column
from sqlalchemy.orm import Mapped,mapped_column,relationship,declarative_base
from flask_sqlalchemy import SQLALCHEMy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash






Base = declarative_base()
db = SQLALCHEMy(model_class=Base, engine_options=dict(echo=True))


user_your_assoc = Table(
    "user_tour_assoc",
    Base.metadata,
    Column("user_id", ForeignKey("users_id", ondelate="cascade"), primary_key=True)
    Column("tour_id", ForeignKey("tours_id", ondelate="cascade"), primary_key=True)
)



class Tour(db.model):
    __tablename__ = "tours"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(string(50))
    description: Mapped[str] = mapped_column(string(300))
    departure: Mapped[str] = mapped_column(string(50))
    picture: Mapped[str] = mapped_column(string())
    price: Mapped[int] = mapped_column()
    stars: Mapped[str] = mapped_column(string(5))
    country: Mapped[str] = mapped_column(string(50))
    nights: Mapped[int] = mapped_column()
    date: Mapped[str] = mapped_column(string(50))










class User(db.Model, UserMixin):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(string(100), nullable=True)
    last_name: Mapped[str] = mapped_column(string(100), nullable=True)
    email: Mapped[str] = mapped_column(string(100), nullable=True,unique=True)
    _password: Mapped[str] = mapped_column(string())
    tours: Mapped[list[Tour]] = relationship(secondary=user_tour_assoc)
    is_admin: Mapped[bool] = mapped_column(bool, default=False)


    @property
    def password(self):
        return "dont use this"
    


    @password.setter
    def password(self,pwd):
        self.password = generate_password_hash(pwd)


    def is_validate_password(self,pwd):
        return check_password_hash(self.password, pwd)