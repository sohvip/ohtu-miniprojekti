import os
from flask_sqlalchemy import SQLAlchemy
from app import app
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

DATABASE_URL = os.getenv("DATABASE_URL")
ENV = os.getenv("FLASK_ENV") or "production"

if DATABASE_URL is None:
    raise Exception(
        f"Database URI is not defined with the DATABASE_URL environment variable"
    )

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
