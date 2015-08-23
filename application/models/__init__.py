from ._base import db

from . import (
    user,
    record,
    file,
    phone,
    selfstory,
    notice,
)

from .dating import ENABLE_MODELS as DATING_ENABLE_MODELS

ENABLE_MODELS = [
    ("User", user, (
            user.User,
            user.MaleUser,
            user.FemaleUser,
    )),
    ("User", record, (
            record.Record,
    )),
    ("User", file, (
            file.File,
    )),
    ("User", phone, (
            phone.Phone,
    )),
    ("User", selfstory, (
            selfstory.SelfStory,
    )),
    ("User", notice, (
            notice.Notice,
    ))
] \
    + DATING_ENABLE_MODELS \
    + []  # XXX : ADD ABOVE
