import cv2
from ultralytics import YOLO
import torch
import os
def example():
    now_path = os.path.abspath(".")
    model = YOLO(now_path+"/best.pt")
    img_path = os.path.abspath(".")+'/V006_77_0_00_01_01_13_0_c03_20201209_0000_S01_1.jpg'
    inputs = [img_path]
    result = model(inputs)[0]
    result = result.cpu()
    #predict = model.predict(source=img_path, show=False, show_labels=True, show_conf=True, conf=0.3)
    boxes = result.boxes
    masks = result.masks
    probs = result.probs
    print("-------------boxes----------------")
    #box 좌표
    print(boxes.xyxyn)
    print("----------boxes conf ------------")
    #box 정확도
    print(boxes.conf)
    #box 분류한 값
    print("-----------boxes class --------------")
    print(boxes.cls)


class Detector:
    def load_model(self,model_path):
        if model_path:
            try:
                model = YOLO(os.path.abspath(".")+"/"+model_path)
                return model
            except:
                print("Model Name is Wrong!!")
                return None
            
    def __init__(self, model_path):
        self.model = self.load_model(model_path)
        self.crop_type_match = {
            0: [0, 1, 2],
            1: [3, 4, 5],
            2: [6, 7, 8],
            3: [9, 10, 11]
        }
        self.empty_dict = {
            "responseCode": 1,
            "diagnoseReults": []
        }

    def getMyDiagnosis(self,crop_type, boxes):
        return list(filter(lambda box: True if int(box.cls) in self.crop_type_match[crop_type] else False, boxes))
    
    def getTop3Diagnosis(self,boxes):
        return list(map(lambda box:{
                "diseaseCode":int(box.cls),
                "accuracy":float(box.conf),
                "bbox":[float(v) for v in box.xyxyn[0].tolist()]
            },sorted(boxes,key=lambda x: float(x.conf))[:3])
        )
    async def __call__(self,crop_type,img_path):
        result = self.model([img_path])[0]
        #여기 수정하기 -- 필터링 로직
        boxes = list(result.boxes)
        if not boxes: return self.empty_dict
        #boxes = list(filter(lambda box: True if box.cls in crop_type_match[crop_type] else False, boxes))
        boxes = self.getMyDiagnosis(crop_type,boxes)
        if not boxes: return self.empty_dict
        return {
            "responseCode" : 0,
            "diagnoseReults": self.getTop3Diagnosis(boxes)
        }
