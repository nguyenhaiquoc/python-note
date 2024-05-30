import tasks

from tenacity import retry, stop_after_attempt, wait_exponential


@retry(stop=stop_after_attempt(10), wait=wait_exponential(multiplier=1, min=4, max=10))
def publish_add_number_tenacity(x, y):
    tasks.add_numbers.apply_async((x, y), retry=False)


def publish_add_number_celery(x, y):
    tasks.add_numbers.apply_async(
        (2, 2),
        retry=True,
        retry_policy={
            "max_retries": 20,
            "interval_start": 1,
            "interval_step": 1,
            "interval_max": 1,
            "retry_errors": (Exception,),
        },
    )
