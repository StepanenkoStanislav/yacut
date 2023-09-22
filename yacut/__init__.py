from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint

from settings import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

SWAGGER_URL = '/api/docs'
API_URL = '/static/openapi.yml'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'YaCut'
    }
)
app.register_blueprint(swaggerui_blueprint)


from yacut import forms, models, views, api_views, error_handlers

db.create_all()
