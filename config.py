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
