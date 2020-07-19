import os

HOME_PATH = os.environ.get("HOME_PATH", "/home/user_name")

MYSQL_HOST = os.environ.get("MYSQL_HOST", "127.0.0.1")
MYSQL_USER = os.environ.get("MYSQL_USER", "root")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", "test")
MYSQL_PORT = int(os.environ.get("MYSQL_PORT", "3306"))
MYSQL_DB = os.environ.get("MYSQL_DB", "django")

