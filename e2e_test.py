import requests
import gevent
import datetime
import argparse
import logging

console = logging.StreamHandler()
console.setLevel(logging.INFO)
logger = logging.getLogger(__name__)
logger.addHandler(console)

port = "5000"
url = "http://localhost:" + port

number_of_client = 10
unit_time_out = 120
finished_task = 0

# def post():
#     resp = requests.post(url+"/report")
#     if resp.status_code == 200:
#         id = resp.json()['report_id']
#         start_time = datetime.datetime.now()
#         print(f'[INIT] init process for id:{id}, {start_time}')
#         global finished_task
#         while finished_task < number_of_client and \
#                 (datetime.datetime.now() - start_time).total_seconds() < number_of_client * unit_time_out:
#             r = requests.get(url+f"/report/{id}")
#             if r.status_code == 200 and r.json()['result'] != None:
#                 duration = (datetime.datetime.now() -
#                             start_time).total_seconds()
#                 finished_task += 1
#                 print(
#                     f'[COMPLETED] finished count: {finished_task} task id:{id} duration:{duration} seconds')
#                 break
#             gevent.sleep(3)
# gevent.joinall([gevent.spawn(post) for _ in range(number_of_client)])

class E2eTest:

    def __init__(self, url, number_requests):
        self.url = url
        self.number_requests = number_requests
            
    def __call(self):
        resp = requests.post(self.url+"/report")
        if resp.status_code == 200:
            id = resp.json()['report_id']
            start_time = datetime.datetime.now()
            print(f'[INIT] init process for id:{id}, {start_time}')
            global finished_task
            while finished_task < self.number_requests and \
                    (datetime.datetime.now() - start_time).total_seconds() < self.number_requests * unit_time_out:
                r = requests.get(url+f"/report/{id}")
                if r.status_code == 200 and r.json()['result'] != None:
                    duration = (datetime.datetime.now() -
                                start_time).total_seconds()
                    finished_task += 1
                    print(
                        f'[COMPLETED] finished count: {finished_task} task id:{id} duration:{duration} seconds')
                    break
                gevent.sleep(3)
        

    def run(self): 
        print('dddd')
        logger.info('ddffff')
        logging.info('info')
        gevent.joinall([gevent.spawn(self.__call) for _ in range(self.number_requests)])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='test celery service with number of requests')
    parser.add_argument('url', type=str, 
                        help='celery service url')
    parser.add_argument('-n', type=int, default=10,
                        help='number of requests')
    args = parser.parse_args()
    e2eTest = E2eTest(args.url, args.n)
    e2eTest.run()
    