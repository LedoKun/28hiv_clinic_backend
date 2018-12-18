import os

from dotenv import load_dotenv

# load env file
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))


class Config(object):
    # Must be set to True
    PROPAGATE_EXCEPTIONS = True
    TRAP_HTTP_EXCEPTIONS = os.environ.get("TRAP_HTTP_EXCEPTIONS")

    SECRET_KEY = os.environ.get("SECRET_KEY")
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
    JWT_BLACKLIST_ENABLED = os.environ.get("JWT_BLACKLIST_ENABLED")

    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get(
        "SQLALCHEMY_TRACK_MODIFICATIONS"
    )

    BCRYPT_ROUNDS = os.environ.get("BCRYPT_ROUNDS")
    DEFAULT_USER = os.environ.get("DEFAULT_USER")
    DEFAULT_PASSWORD = os.environ.get("DEFAULT_PASSWORD")

    PATIENTS_PER_PAGE = os.environ.get("PATIENTS_PER_PAGE")
    DASHBOARD_APPOINTMENT_PER_PAGE = os.environ.get(
        "DASHBOARD_APPOINTMENT_PER_PAGE"
    )
    DASHBOARD_EXAMINED_PER_PAGE = os.environ.get(
        "DASHBOARD_EXAMINED_PER_PAGE"
    )

    STATS_TABLE_CLASSES = os.environ.get(
        "STATS_TABLE_CLASSES"
    ).split(",")