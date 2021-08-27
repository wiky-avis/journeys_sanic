from sanic import Sanic

app = Sanic(__name__)

from app import views

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from app.models import *
