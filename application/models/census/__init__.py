"""."""
__author__ = 'minhoryang'

from . import (
    question,
    reply,
    comment,
)


ENABLE_MODELS = [
    ("Census", question, (
        question.Question,
        question.QuestionBook,
    )),
    ("Census", reply, (
        reply.Reply,
        reply.ReplyBook,
    )),
    ("Census", comment, (
        comment.Comment,
        #comment.CommentLike,
    )),
    ("MergedNamespace", type(
        "MergedNamespace", (), {
            "init": lambda *args, **kwargs: init(*args, **kwargs),
            "module_init": lambda *args, **kwargs: None,
        }
    ), (
    )),
] \
    + []  # XXX : ADD ABOVE


def init(api, jwt):
    namespace = api.namespace(__name__.split('.')[-1], description=__doc__.split('.')[0])
    for _, module, _ in ENABLE_MODELS:
        module.module_init(api, jwt, namespace)
