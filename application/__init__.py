from datetime import timedelta
from os.path import abspath, dirname, join

from flask import Flask, jsonify
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.restplus import Api
from flask_jwt import JWT

def create_app():
    app = Flask(__name__)
    # TODO: EXTRACT!!!!
    app.config['PROJECT_PATH'] = abspath(join(dirname(__file__), '..'))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s/db/app.db' % (app.config['PROJECT_PATH'], )
    app.config['SECRET_KEY'] = 'developer'  # TODO: need to change.
    app.config['JWT_AUTH_HEADER_PREFIX'] = 'Bearer'
    app.config['JWT_AUTH_URL_RULE'] = None
    app.config['JWT_EXPIRATION_DELTA'] = timedelta(minutes=10)  # TODO: need to change.
    app.config['UPLOAD_FOLDER'] = '/tmp/'

    from .models import db, user, record, file, phone
    db.init_app(app)

    admin = Admin(app)
    admin.add_view(ModelView(user.User, db.session))
    admin.add_view(ModelView(record.Record, db.session))
    admin.add_view(ModelView(file.File, db.session))
    admin.add_view(ModelView(phone.Phone, db.session))

    class MyJWT(JWT):
        def _error_callback(self, e):
            return jsonify(dict([('status', e.status_code), ('message', e.error + ' - ' + e.description)])), 401, e.headers  # e.status_code

    jwt = MyJWT(app)

    api = Api(app, version='1.0', title='MarryBird API', description='Hi There!')
    user.init(api, jwt)
    record.init(api, jwt)
    file.init(api, jwt)
    phone.init(api, jwt)

    return app