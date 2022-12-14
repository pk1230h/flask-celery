import requests
import datetime
import argparse
try:
    import gevent
except ImportError:
    print("please install gevent")

unit_time_out = 120
finished_task = 0


class ClientRequest:
    def __init__(self, url, number_requests):
        self.url = url
        self.number_requests = number_requests

    def call(self):
        resp = requests.post(self.url+"/report")
        if resp.status_code == 200:
            id = resp.json()['report_id']
            start_time = datetime.datetime.now()
            print(f'[INIT] init process for id:{id}, {start_time}')
            global finished_task
            while finished_task < self.number_requests and \
                    (datetime.datetime.now() - start_time).total_seconds() < self.number_requests * unit_time_out:
                print(f'{id} {finished_task} working')
                r = requests.get(self.url+f"/report/{id}")
                if r.status_code == 200 and r.json()['result'] != None:
                    duration = (datetime.datetime.now() -
                                start_time).total_seconds()
                    finished_task += 1
                    print(
                        f'[COMPLETED] finished count: {finished_task} task id:{id} duration:{duration} seconds')
                    break
                gevent.sleep(3)

    def run(self):
        threads = [gevent.spawn(self.call)
                   for _ in range(self.number_requests)]
        gevent.joinall(threads)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='test celery service with number of requests')
    parser.add_argument('url', type=str,
                        help='celery service url')
    parser.add_argument('-n', type=int, default=10,
                        help='number of requests')
    args = parser.parse_args()
    client = ClientRequest(args.url, args.n)
    client.run()
