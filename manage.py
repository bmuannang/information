from flask import Flask
#此模块用来指定session的保存位置
from flask import session
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager
from flask.ext.session import Session
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import CSRFProtect
from redis import StrictRedis


class Config(object):
    '''项目配置'''
    DEBUG = True

    SECRET_KEY = 'VKBK0fOa/ogY93KyFcM4U1yCB+hDdrSZrcztRBJGqOKrDz1Gtcrce9XYtJNcRIMr'
    #为数据库添加配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/information"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #redis的配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    #session保存配置
    SESSION_TYPE = 'redis'
    #开启session签名
    SESSION_USE_SIGNER = True
    #制定session保存的redis
    SESSION_REDIS = StrictRedis(host = REDIS_HOST,port=REDIS_PORT)
    #设置过期
    SESSON_PERMANENT = False
    # 设置过期时间
    PERMANENT_SESSION_LIFETIME = 86400 * 2




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