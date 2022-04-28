import os


def parse_bool(field):
    return os.getenv(field, "").lower() in ["true", "1"]


class Config:

    DEV = parse_bool("DEV")
    if DEV:
        FLASK_ENV = "development"
