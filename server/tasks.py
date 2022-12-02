from server.app import celery
import time
import os
SLEEP_TIME = int(os.getenv("SLEEP_TIME", '60'))


@celery.task(name="report", bind=True, acks_late=True)
def report(self):
    print(f"Task id:{self.request.id} generating report")
    time.sleep(SLEEP_TIME)
    return {"state":"completed"}
