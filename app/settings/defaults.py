import os

SECRET_KEY = 'senao.network.com.tw'

# sqlalchemy
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI','mysql+pymysql://root:root@localhost:3306/demo?charset=utf8mb4')
SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS', True)

LOG_FILE_PATH = os.environ.get('LOG_FILE_PATH') or 'demo.log'
ERROR_LOG_FILE_PATH = os.environ.get('ERROR_LOG_FILE_PATH') or 'demo.log'
