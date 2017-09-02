''' Jimmy's Celery Example

This file demonstrates how to use Celery using a Redis broker 
for handling tasks and Redis backend to store results.

'''

import time
from celery import Celery 

app = Celery('tasks', broker='redis://localhost:6379', backend="redis://localhost:6379/3")

@app.task(time_limit=3) 
def fast_spliter(string):

    '''
    This function completes before the time limit thus 
    returns the result successfully for storage.
    ''' 

    time.sleep(1)
    return string.split()

@app.task(time_limit=3) 
def slow_spliter(string):

    '''
    This function is terminated before completion 
    as the process exceeds the time limit of 3 seconds. 
    ''' 

    time.sleep(5)
    return string.split()

if __name__ == "__main__":
    print("Calling fast_spliter() ... ")
    job_1 = fast_spliter.delay("Road runner is super fast")
    time.sleep(3)
    print("Job status: ", job_1.status)

    print("\nCalling fast_spliter() ... ")
    job_2 = slow_spliter.delay("Slothes enjoy being slow")
    time.sleep(3)
    print("Job status: ", job_2.status)





