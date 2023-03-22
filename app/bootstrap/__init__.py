from flask import Flask
from flask_cors import CORS
from flask_injector import FlaskInjector, request
from flask_sqlalchemy import SQLAlchemy

from app.extensions import cache
from app.config import Config

# class AppBuilder:
#     def __init__(self):
#         self.app = Flask(Config.NAME)


def create_app(config_mode='development'):
    app = Flask(Config.NAME)
    app.config.from_object(Config)
    app.secret_key = Config.APP_SECRET
    app.url_map.strict_slashes = False

    # cache.init_app(app)

    # init_db(app)

    # register_routes(app)

    CORS(app,
         send_wildcard=True,
         expose_headers=['x-auth-token', "content-disposition"])
    # AllBlueprintsErrorHandler(app)

    # FlaskInjector(app=app, modules=[configure])

    return app


# def configure(binder):
#     binder.bind(
#         SQLAlchemy,
#         to=db,
#         scope=request,
#     )