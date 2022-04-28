import os
from flask import Flask

from src.api.common import blueprint as common
from src.api.v1.routes import blueprint as v1
from src.config import Config


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_object(Config)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    routes = [common, v1]

    for route in routes:
        app.register_blueprint(route)

    return app
