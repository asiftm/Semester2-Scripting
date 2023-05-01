# import time
# print(time.time())
# print(time.ctime())
# print(time.ctime(time.time()))



# import requests
# import json
# import time
#
# # start time
# startTime = time.time()
#
# response = requests.get("https://worldtimeapi.org/api/timezone/Asia/Dhaka")
# json_data = json.loads(response.text)
#
# # end time
# endTime = time.time()
#
# print('Tokyo time is', json_data["datetime"])
# print(f'Took {endTime - startTime} seconds to get.')



# import time
#
# for i in range(10):
#     print('Tick')
#     time.sleep(1)
#     print('Tock')
#     time.sleep(1)



# import time
#
# print("Before the sleep statement")
# time.sleep(.01)
# print("After the sleep statement")



# import time
# startTime = time.time()
# for i in range(0,5):
#    print(i)
#    # making delay for 1 second
#    time.sleep(1)
# endTime = time.time()
# elapsedTime = endTime - startTime
# print("Elapsed Time = %s" % elapsedTime)



# import time
#
# for i in [ .5, .5, 1, 2]:
#    print("Waiting for %s" % i , end='')
#    print(" seconds")
#    time.sleep(i)



# # importing time module
# import time
# message = "Hi!!! I am trying to create suspense"
#
# for i in message:
#    # printing each character of the message
#    print(i,end='')
#    time.sleep(0.3)



# import time
# from threading import Thread
# class Worker(Thread):
#     def run(self):
#         for x in range(0, 11):
#             print(x)
#             time.sleep(1)
# class Waiter(Thread):
#     def run(self):
#         for x in range(100, 103):
#             print(x)
#             time.sleep(5)
# print("Staring Worker Thread")
# Worker().start()
# print("Starting Waiter Thread")
# Waiter().start()
# print("Done")


import datetime
import time
print(datetime.datetime.now())
dt = datetime.datetime(2019, 10, 21, 16, 29, 0)
print(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
print(datetime.datetime.fromtimestamp(10000))
print(datetime.datetime.fromtimestamp(time.time()))
print(datetime.datetime.fromtimestamp(round(time.time(),0)))


# import time,datetime
#
# dt = datetime.datetime.now()
# print(dt)
# dt += datetime.timedelta(days=1000)
# print(dt)
#
# aboutThirtyYears = datetime.timedelta(days=365 * 30)
# dt -= aboutThirtyYears
# print(dt)
# dt = datetime.datetime.now()
# print(dt.strftime('%Y/%m/%d %H:%M:%S'))


# import datetime,time
# startTime = datetime.datetime(2029, 10, 31, 0, 0, 0)
# while datetime.datetime.now() < startTime:
#     time.sleep(1)
#
# print('Program now starting on Halloween 2029')



# # code in a separate file
# # multi.py
#
# import threading, time
#
# def TakeANap():
#     time.sleep(1)
#     print('Wake up!')
#
# print('Start of program.')
#
# thread = threading.Thread(target=TakeANap)
# thread.start()
#
# print('End of program.')



