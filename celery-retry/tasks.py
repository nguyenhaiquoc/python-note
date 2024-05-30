from celery import Celery

# declare celery app with redis and connection timeout settings
app = Celery("tasks", broker="redis://localhost:3379/0", broker_connection_timeout=1)


@app.task
def add_numbers(x, y):
    return x + y
