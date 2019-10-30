from flask import Flask
from flask_session import Session
# 第一步：导入并实例化SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy() # 实例化SQLAlchemy  里面封装了数据库连接等


from .views.home import he
from .models import *

def create_app():
    app = Flask(__name__)
    app.config.from_object('settings.ProConfig')
    app.register_blueprint(he)
    # Flask-Session: 第一步示例Session
    # Session(app)

    # 第三步：依赖app中的配置文件
    db.init_app(app)   # 注册 SQLAlchemy
    return app
