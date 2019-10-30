from flask import Blueprint,render_template
from supflask import db
from supflask import models
he= Blueprint('uhhaha',__name__)

@he.route('/home/')
def homes():
    # 使用SQLAlchemy在数据库中插入一条数据
    # db.session.add(models.User(name='张三三废'))
    # db.session.commit()
    # db.session.remove()

    result = db.session.query(models.User).all()
    print(result)
    db.session.remove()  #  内部自动 为每个线程去连接池创建一个连接

    return  render_template('index.html')