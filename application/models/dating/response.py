"""."""
__author__ = 'minhoryang'

from datetime import datetime

from flask.ext.restplus import Resource, fields
from flask_jwt import jwt_required, current_user

from .. import db
from .progress import Progress

class Response(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    request_id = db.Column(db.Integer)
    username = db.Column(db.String(50))

    isDone = db.Column(db.Boolean)
    result_json = db.Column(db.String(200))  # TODO : is there db.Column(db.JSON()) ??


def init(api, jwt):
    namespace = api.namespace(__name__.split('.')[-1], description=__doc__)
    authorization = api.parser()
    authorization.add_argument('authorization', type=str, required=True, help='"Bearer $JsonWebToken"', location='headers')

    @namespace.route('/')
    class GetResponse(Resource):

        @jwt_required()
        @api.doc(parser=authorization)
        def get(self):
            username = current_user.username

            #Response.query.filter(Response.username == username).
            result_json = None
            Success, Someone, Mine = Progress.SearchHeLovesSheOrNot(
                Progress.SearchWhoLovesMe(username),
                Progress.SearchMeLovesWho(username)
            )

            return {'status': 200, 'message': {
                'success': Success,
                'someonelovesme': Someone,
                'notyet': Mine,
                'result': result_json
            }}