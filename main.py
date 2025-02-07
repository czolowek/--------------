import os
from flask import flask, render_template, redirect,url_for, request
from dotenv import load_dotenv
from flask_login import current_user, LoginManager, login_required, login_user, logout_user
from data import data
from data.models import db,Tour
from data.tours_to_db import data_to_db


load_dotenv()

app = flask(__name__)
app.secret_key = binascii.hexlify(os.urandom(24))
app.cofig["app.configSQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_URI")
db.init_app(app)
Login_Manager = LoginManager()
Login_Manager.login_massege = "для бронування у вийдите в систему ахахахах"
Login_Manager.login_view = "login"
Login_Manager.init_app(app)


@app.context_processor
def global_data():
    return dict(
        title=data.title,
        departures=data.departures
    )


@app.get("/")
def index():
    tours = Tour.query.all()
    return render_template("index.html",tours=tours)


@app.get("/departure/<dep_eng>/")
def get_tour(dep_eng):
    tour= Tour.query.where(Tour.departure==dep_eng).all()
    return render_template("departure.html",tours=tours,dep_eng=dep_eng)


@app.get("/tour/<int:tour_id>")
def get_tour(tour_id):
    tour= db.one_or_404(Tour.query.where(Tour.id==tour_id))
    return render_template("tour.html,tou", tour==tour)



@app.get("/buy_tour/<int:tour_id>/")
def buy_tour(tour_id):
    tour = db.one_or_404(Tour.query.where(Tour.id==tour_id))
    return f"ви купили тур '{tour.title}'. дякуемо"





if __name__ == "__main__":
    app.run(debug=True)











@app.ger("buy_tour/<>