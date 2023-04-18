import os
import time
from threading import Thread
from queue import Queue
from yolov8_detect import Detector
import asyncio
import json

class AI_Server:
    def __init__(self):
        self.detector = Detector("./best.pt")
        self.work_queue = Queue()
        self.isRunning = False
        self.backThread = Thread(target=self.runner)

    # 백 쓰레드가 실행할 작업들
    def runner(self):
        while not self.work_queue.empty():
            json_file,img_file = self.work_queue.get()
            user_data = json.loads(json_file)
            result = asyncio.run(self.detector(user_data["imageCode"],img_file))
            result["cropImageID"] = user_data["cropImageID"]
            self.sendToClient(result)
        self.isRunning = False

    #메인 서버 정보를 플라스크에서 받는 함수
    def receiveToClient(self,json_file,img_file):
        self.work_queue.put((json_file,img_file))
        if not self.backThread.is_alive():
            self.isRunning = True
            self.backThread.start()

    #여기에 Flask에서 메인 서버로 보내는 코드 작성
    def sendToClient(self,result):
        print(json.dumps(result))
        return

worker = AI_Server()
img_list = [os.path.abspath(".")+v for v in ['/V006_77_0_00_01_01_13_0_c03_20201209_0000_S01_1.jpg'
,'/V006_77_0_00_01_01_13_0_c03_20201209_0188_S01_1.jpg']]
for img in img_list:
    json_file = json.dumps({
        "cropImageID": "hello12345",
        "imageCode": 0
    })
    worker.receiveToClient(json_file,img)
for img in img_list:
    json_file = json.dumps({
        "cropImageID": "hello12345",
        "imageCode": 0
    })
    worker.receiveToClient(json_file,img)
for img in img_list:
    json_file = json.dumps({
        "cropImageID": "hello12345",
        "imageCode": 0
    })
    worker.receiveToClient(json_file,img)
