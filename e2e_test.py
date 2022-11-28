import requests
import gevent
import datetime

port = "5000"
url = "http://localhost:" + port

number_of_client = 10
unit_time_out = 120
finished_task = 0

def post():
    resp = requests.post(url+"/report")
    if resp.status_code == 200:
        id = resp.json()['report_id']
        start_time = datetime.datetime.now()
        print(f'[INIT] init process for id:{id}, {start_time}')
        global finished_task
        while finished_task < number_of_client and \
            (datetime.datetime.now() - start_time).total_seconds() < number_of_client * unit_time_out:
            r = requests.get(url+f"/report/{id}")
            if r.status_code == 200 and r.json()['result'] != None:
                duration = (datetime.datetime.now() - start_time).total_seconds()
                finished_task += 1
                print(f'[COMPLETED] finished count: {finished_task} task id:{id} duration:{duration} seconds')
                break 
            gevent.sleep(3) 

gevent.joinall([gevent.spawn(post) for _ in range(number_of_client)])