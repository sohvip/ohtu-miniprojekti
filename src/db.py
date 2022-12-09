from os import getenv
from flask_sqlalchemy import SQLAlchemy
from app import app

<<<<<<< HEAD
app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DATABASE_URL")
=======
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2:///mirelle"
>>>>>>> 58e3bed6ec026925c2749d38241fe46579f601d0
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
