"""Stores the met (by Accepts/Rejects/NoResponse)."""

__author__ = 'minhoryang'

from enum import Enum
from datetime import datetime

from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy_utils.types.choice import ChoiceType

from .. import db


class MetType(Enum):
    rejected = "rejected"
    accepted = "accepted"
    notresponsed = "notresponsed"

class Met(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    response_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.now)
    type = db.Column(ChoiceType(MetType), nullable=False)
    A = db.Column(db.String(50))
    B = db.Column(db.String(50))

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


class Met_Rejected(Met):
    id = db.Column(db.Integer, db.ForeignKey('met.id'), primary_key=True)

    @classmethod
    def create(cls, response_id, A, B):
        c = cls()
        c.response_id = response_id
        c.type = MetType.rejected.value
        c.A = A
        c.B = B
        return c


class Met_Accepted(Met):
    id = db.Column(db.Integer, db.ForeignKey('met.id'), primary_key=True)

    @classmethod
    def create(cls, response_id, A, B):
        c = cls()
        c.response_id = response_id
        c.type = MetType.accepted.value
        c.A = A
        c.B = B
        return c


class Met_NotResponsed(Met):
    id = db.Column(db.Integer, db.ForeignKey('met.id'), primary_key=True)

    @classmethod
    def create(cls, response_id, A, B):
        c = cls()
        c.response_id = response_id
        c.type = MetType.notresponsed.value
        c.A = A
        c.B = B
        return c


def init(api, jwt):
    pass