from celery import shared_task
from time import sleep

@shared_task(bind=True)
def go_to_sleep(self,durations):
    sleep(durations)
    return 'DONE'