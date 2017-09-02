# Celery Example Tutorial with Redis

The following document demonstrates how to use Celery with a Python 3 project. Redis is used in this example as the broker and backend. 

## Dependancies and Setup 
- Ensure Python3 is installed 
- Install redis. For Mac OSX, open the terminal and enter ``brew install redis``. 
- Start the redis service in the terminal by typing ``brew services start redis``. 
- Install celery using ``pip install celery[redis]``. (Installing this using a virtualenv environment is preferred) 

## Code 

1. Create a new file called ``tasks.py``. First, let's import the time module and the Celery constructor (line 1 and 2)

2. Next, we'll create a Celery application instance. 
  - 1st argument specifies the module in which tasks belong to. Without this, the application won't be able to reference functions. [2]
- Keyword argument: broker. This is required to transfer message between the client and the workers. [3]
- Keyword argument: backend. This allows for storage of results. 
<img width="810" alt="screen shot 2017-09-02 at 12 09 15 png" src="https://user-images.githubusercontent.com/22529514/29995213-15a7297e-8fdc-11e7-9739-7ed7ef15d008.png">

3. Save this file and open the terminal. In the directory where ``tasks.py`` exists, type ``celery -A tasks worker --loglevel=info``. Something similar to the image below should appear: 

<img width="774" alt="screen shot 2017-09-02 at 13 18 02" src="https://user-images.githubusercontent.com/22529514/29995454-7091f706-8fe1-11e7-9c00-9db99e9c8f6b.png">

4. Returning to ``tasks.py``, we can now start writing some functions which will be called as tasks. 
- To do this, we'll include the wrapper ``@app.task(time_limit=3)``. The time_limit parameter here tells the worker "If the task in progress exceeds 3 seconds, then we no longer want the result. Let's terminate this.". 
- To simulate some intensive progress, we'll mock this using the time.sleep() method. As we want this function call to succeed and return some value, we'll set sleep to 1 so that it reaches the return statement. 

<img width="402" alt="screen shot 2017-09-02 at 12 55 24" src="https://user-images.githubusercontent.com/22529514/29995286-05c69740-8fde-11e7-8d1d-6e782b09fd7e.png">

5. We can then try to run this task by adding the following code to the bottom of the file: 
<img width="561" alt="screen shot 2017-09-02 at 13 23 10" src="https://user-images.githubusercontent.com/22529514/29995478-e5615306-8fe1-11e7-93c3-02c8cd1ab4e5.png">

6. Let's run this file using ``python tasks.py``:

<img width="530" alt="screen shot 2017-09-02 at 13 22 26" src="https://user-images.githubusercontent.com/22529514/29995484-1841db4c-8fe2-11e7-848e-11206c62c2de.png">

Our task has completed before the time limit!

7. For a case where the simulation exceeds the time, let's add another task: 
<img width="291" alt="screen shot 2017-09-02 at 13 26 35" src="https://user-images.githubusercontent.com/22529514/29995496-6062eb28-8fe2-11e7-9133-92dd6820ab13.png">

8. Again, let's call this ask by adding this to the ``if __name__ == '__main__'`` section:
<img width="539" alt="screen shot 2017-09-02 at 13 28 46" src="https://user-images.githubusercontent.com/22529514/29995509-aaab5292-8fe2-11e7-98db-b105af0a1e10.png">
9. Rerunning ``python tasks.py`` in the terminal will now show a failure for the second result: 
<img width="450" alt="screen shot 2017-09-02 at 13 29 27" src="https://user-images.githubusercontent.com/22529514/29995519-d6f62c6e-8fe2-11e7-9605-ad63271322bb.png">



## References: 
http://docs.celeryproject.org/en/latest/getting-started/introduction.html 
[2] http://docs.celeryproject.org/en/latest/userguide/application.html 
[3] http://docs.celeryproject.org/en/latest/getting-started/brokers/redis.html
