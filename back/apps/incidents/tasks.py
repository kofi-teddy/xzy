from celery import shared_tasks


@shared_task
def update_to_visitor():
    print('Task update_to_visitor has been initiated')