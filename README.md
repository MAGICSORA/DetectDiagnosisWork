# DetectDiagnosisWork
병해 검출 처리하기

### 아직 실제 플라스크 서버에서 사용하지 않았음으로 임의의 입력 데이터 json을 만듬
### 추가로 아직 외부 서버에서 직접 이미지를 가져오지 않기 때문에 이미지 Path에 접근해 이미지를 가져오게 코드를 작성함

## 디렉토리 구조
- DetectDiagnosisWork
  - best.pt -> 인공지능 모델
  - img.jpg -> 이미지
  - yolov8_detect.py -> 인공지능 모델을 실행하는 모듈 파일
  - yolov8_detect_to_web.py -> 외부 서버와 인공지능 모델간의 정보를 관리하는 모듈 파일
