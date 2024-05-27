import cv2
import numpy as np
import pandas as pd

def makeGrid(image):
    for i in range(0,15):
        cv2.line(image, (0,i*50), (750,i*50), (255,255,255)) # 가로 선 긋기 (50간격 마다), 시작위치, 끝위치,
    for i in range(0,15):
        cv2.line(image, (i*50,0), (i*50,750), (255,255,255)) # 세로 선 긋기 (50간격 마다)
        
def makeLine(image, path):
    data = pd.read_csv(path, header=None)
    array = data.to_numpy()

    # 선을 그릴 좌표 찾기
    points = np.argwhere(array == 1)
    sorted_points = sorted(points, key=lambda x: (x[1], x[0]))
    
    # 결과를 원하는 순서로 재배치
    ordered_points = []
    
    # 1열에 해당하는 좌표들을 위에서 아래로 추가
    ordered_points.extend(sorted_points[:14][::-1])  # 0열 ~ 13열을 역순으로 추가
    
    # 0열에 해당하는 좌표들을 왼쪽에서 오른쪽으로 추가
    ordered_points.extend(sorted_points[14:])
    
    # 리스트를 numpy 배열로 변환
    ordered_points = np.array(ordered_points)
    print(ordered_points)
    # 모든 좌표에 1을 더하고 50을 곱합니다. x, y 좌표는 1부터 시작함
    ordered_points = (ordered_points + 1) * 50
    
    # OpenCV를 사용하여 선 그리기
    for i in range(len(ordered_points) - 1):
        cv2.line(image, (ordered_points[i][1], ordered_points[i][0]), (ordered_points[i + 1][1], ordered_points[i + 1][0]), (0, 0, 255), 2)
        if i > 0 and i < len(ordered_points) - 1:
            if (ordered_points[i-1][0] != ordered_points[i][0] and ordered_points[i+1][0] != ordered_points[i][0]) or (ordered_points[i-1][1] != ordered_points[i][1] and ordered_points[i+1][1] != ordered_points[i][1]):
                continue
            else :
                cv2.circle(image, (ordered_points[i][1], ordered_points[i][0]), 5, (0, 0, 255), -1)
    
    
def initPng(path) :
    image = np.full((750, 750, 3), (0, 0, 0), dtype=np.uint8) # 750 * 750 크기의 검은 이미지 생성
    makeGrid(image) # 격자 생성
    makeLine(image,path)
    cv2.imshow("image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
path ='C:/Users/ehddn/project-x/3st_week/Q4/home_to_us_camp.csv'
initPng(path)

# 보너스 과제는 진행하지 않았습니다.
