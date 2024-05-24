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
        #publisher.publish_add_number_tenacity(1, 2)
        time.sleep(2)
     
     
def dirty():  
    logging.info("dirty code")   