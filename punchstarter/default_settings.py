__author__ = 'sonali'
import os
import cloudinary




DEBUG = True
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SQLALCHEMY_DATABASE_URI = "sqlite:///" + BASE_DIR + "/app.db"


cloudinary.config(
  cloud_name = "dqldclhq4",
  api_key = "792831388795511",
  api_secret = "ShNoCvePuRV66PD0EuuOS7LuT8s"
)