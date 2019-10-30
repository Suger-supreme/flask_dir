from redis import Redis
import os
from datetime import timedelta
basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

class BaseConfig(object):
    # Flask-Session: 第二步配置
    # SESSION_TYPE = 'redis'
    # SESSION_REDIS = Redis(host='192.168.0.94', port='6379')
    # session配置
    SESSION_COOKIE_NAME = 'session'
    SESSION_COOKIE_DOMAIN = None
    SESSION_COOKIE_PATH = None
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = False
    SESSION_REFRESH_EACH_REQUEST = True
    PERMANENT_SESSION_LIFETIME = timedelta(hours=1)


    # ##### SQLALchemy配置文件 #####
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@127.0.0.1:3306/mydb5?charset=utf8"
    SQLALCHEMY_POOL_SIZE = 10
    SQLALCHEMY_MAX_OVERFLOW = 5
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    pass


class ProConfig(BaseConfig):
    SECRET_KEY = 'asdf123sdfsdfsdf'
    pass