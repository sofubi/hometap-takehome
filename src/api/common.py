import os
from flask import Blueprint


blueprint = Blueprint("common", __name__)


API_VERSION = os.getenv("API_VERSION")


@blueprint.route("/")
def index():
    return f"Septic Check Service {API_VERSION}", 200


@blueprint.route("/health")
def health():
    return "", 200


@blueprint.route("/ready")
def ready():
    return "", 200
