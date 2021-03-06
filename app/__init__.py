import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
oid = OpenID(app, os.path.join(basedir, 'tmp'))

# Logging to a file
if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    logpath = os.path.join(basedir, 'tmp', 'microblog.log')
    file_handler = RotatingFileHandler(logpath,
                                       'a',
                                       1 * 1024 * 1024,
                                       10)
    fmtstr = '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    fmt = logging.Formatter(fmtstr)
    file_handler.setFormatter(fmt)
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('microblog startup')

from app import views, models
