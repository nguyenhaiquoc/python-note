"""
Tenacity will produce proper behavior for retrying tasks than celery's built-in retry mechanism.
Test Case 1:
    1. Start docker-compose up
    2. Run this script
    3. Stop redis container while script is running
    Expected: Retry until reach max_retries, then raise exception
    Result:
        Tenaciy: Work as expected
        Celery: Stop immediately when the broker is down. Expected: need to retry until reach max_retries


Test Case 2:
    1. Run the script (without start redis container)
    Expected: Retry until reach max_retries, then raise exception
    Result:
        Tenacity: Work as expected
        Celery: Work as expected
"""

import logging
import time

import publisher


logging.basicConfig(
    level=logging.INFO,
    format="%(module)s:%(lineno)d %(asctime)s %(message)s",
    datefmt="%H:%M:%S",
)

if __name__ == "__main__":
    for i in range(0, 1000):
        logging.info(i)
        publisher.publish_add_number_celery(1, 2)
        # publisher.publish_add_number_tenacity(1, 2)
        time.sleep(2)
