from flask import Flask
#此模块用来指定session的保存位置
from flask import session
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager
from flask.ext.session import Session
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import CSRFProtect
from redis import StrictRedis
from config import Config





app = Flask(__name__)

#加载配置
app.config.from_object(Config)

#初始化数据库
db = SQLAlchemy(app)

#初始化redis存储对象
redis_store = StrictRedis(host = Config.REDIS_HOST,port = Config.REDIS_PORT)

#开启当前项目 CSRF 保护，只做服务器验证功能
CSRFProtect(app)

#设置session保存制定位置
Session(app)

manager = Manager(app)

#将app与db关联
Migrate(app,db)

#将迁移命令添加到manager中
manager.add_command('db',MigrateCommand)

@app.route('/')
def index():
    session["name"] = "itheima"
    return 'index'


if __name__ == '__main__':
    manager.run()