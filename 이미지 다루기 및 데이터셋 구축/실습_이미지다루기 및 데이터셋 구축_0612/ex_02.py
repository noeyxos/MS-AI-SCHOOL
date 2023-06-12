import cv2
import numpy as np

# 칼만 필터 초기화
kalman = cv2.KalmanFilter(4,2)
kalman.measurementMatrix = np.array([[1, 0, 0, 0], 
                                     [0, 1, 0, 0]], np.float32) # 측정행렬
kalman.transitionMatrix = np.array([[1, 0, 1, 0],
                                    [0, 1, 0, 1],
                                    [0, 0, 1, 0],
                                    [0, 0, 0, 1]], np.float32) # 전이 행렬
kalman.processNoiseCov = np.array([[1, 0, 0, 0],
                                   [0, 1, 0 ,0],
                                   [0, 0, 1, 0],
                                   [0, 0, 0, 1]], np.float32) * 0.05 # 잡음 공분산 설정

# 칼만 필터 추적 실습
# 동영상 파일 열기
cap = cv2.VideoCapture('../data/slow_traffic_small.mp4')

# 첫 프레임에서 추적할 객체 선택
ret, frame = cap.read()
bbox = cv2.selectROI("Select Object", frame, False, False)

# 객체 추적을 위한 초기 추정 위치 설정
# 객체의 x좌표, 객체의 y좌표, 객체의 x 방향 속도(초기 0), 객체의 y 방향 속도(초기 0)
kalman.statePre = np.array([[bbox[0]],
                            [bbox[1]],
                            [0],
                            [0]], np.float32)

# 칼만 필터 추적 실습
while True:
    # 프레임 읽기
    ret, frame = cap.read()
    if not ret:
        break
    
    # 칼만 필터를 사용하여 객체 위치 추정
    kalman.correct(
        np.array(
            [
                [np.float32(bbox[0]+ bbox[2]/ 2)],
                [np.float32(bbox[1]+ bbox[3]/ 2)]
            ]
        )
    )
    kalman.predict()
    
    # 칼만 필터로 추정된 객체 위치 
    predict_bbox = tuple(map(int, kalman.statePost[:2, 0]))
    
    #  추정된 객체 위치를 사각형으로 표시
    cv2.rectangle(frame, (predict_bbox[0] - bbox[2]//2, predict_bbox[1]-bbox[3]//2),
                  (predict_bbox[0]+ bbox[2]//2,  predict_bbox[1]+ bbox[3]//2),
    (0, 255, 0), 2)
    
    
    #프레임 출력
    cv2.imshow("kalman Filter Tracking", frame)
    
    # 'q' 키를 누르면 종료
    if cv2.waitKey(30) & 0xFF == ord("q"):
        exit()
        
# 지원 해제 
cap.release()
cv2.destroyAllWindows()