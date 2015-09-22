__author__ = 'minhoryang'

from .. import create_celery

Celery = create_celery()


@Celery.task(ignore_result=True)
def RestInPeace():
    from ...models.dating2.state import DeadState
    DeadState.RestInPeace()
