from datetime import datetime

from celery import shared_task


@shared_task
def printSth():
    with open("C:/Users/mansu/Desktop/test.txt","a") as file:
        file.write("1")
        file.write(str(datetime.now()))
        file.close()