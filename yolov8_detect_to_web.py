import os
import time
from threading import Thread
#from yolov8_detect import Detector
#detector = Detector("./best.pt")
img_path = os.path.abspath(".")+'/V006_77_0_00_01_01_13_0_c03_20201209_0000_S01_1.jpg'
#dicts = detector(0,img_path)

class AI_Server:
    def __init__(self):
        #self.detector = Detector("./best.pt")
        self.work_queue = []
        self.isRunning = False
        self.backThread = Thread(target=self.runner)

    def runner(self):
        while self.work_queue:
            data = self.work_queue.pop(0)
            self.sendToClient(data)
        self.isRunning = False

    def receiveToClient(self,json_file):
        print("receive" + str(json_file))
        self.work_queue.append(json_file)
        if not self.backThread.is_alive():
            self.isRunning = True
            self.backThread.start()

    def sendToClient(self,json_file):
        time.sleep(1)
        print("hello" + str(json_file))
        return
worker = AI_Server()
for i in range(0,11):
    worker.receiveToClient(i)
    #if worker.
