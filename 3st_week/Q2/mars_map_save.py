import cv2
import numpy as np
import pandas as pd
def makeGrid(imge):
    for i in range(0,15):
        cv2.line(img, (0,i*50), (750,i*50), (255,255,255)) # 가로 선 긋기 (50간격 마다), 시작위치, 끝위치,
    for i in range(0,15):
        cv2.line(img, (i*50,0), (i*50,750), (255,255,255)) # 세로 선 긋기 (50간격 마다)

def makeRock(img,map_file):
    map_df = pd.read_csv(map_file, sep=',')
    map_rock_index = map_df['mountain'] == 1
    map_rock_df = map_df[map_rock_index]
    for x,y in zip(map_rock_df['y'],map_rock_df['x']):
        cv2.circle(img,(x * 50,y * 50),30,(42, 42, 165)) # 위치, 반지름,색상
    
def makeStruct(img,category_file,struct_file):
    category_df = pd.read_csv(category_file, sep=',')
    struct_df = pd.read_csv(struct_file, sep=',')
    struct_df_temp = struct_df.merge(category_df, left_on='category',right_on='category') # category 칼럼을 기준으로 합침
    struct_df_index = (struct_df_temp['struct'] == 'U.S. Mars Base Camp') | (struct_df_temp['struct'] == 'Korea Mars Base')
    struct_df_filtered = struct_df_temp[struct_df_index]
    
    for x,y in zip(struct_df_filtered['y'],struct_df_filtered['x']):
                # 삼각형의 세 꼭짓점 좌표 계산
        center = (x * 50, y * 50)
        pt1 = (center[0], center[1] - 25)  # 위쪽 꼭짓점
        pt2 = (center[0] + 30, center[1] + 25)  # 오른쪽 아래 꼭짓점
        pt3 = (center[0] - 30, center[1] + 25)  # 왼쪽 아래 꼭짓점
        # 삼각형을 이루는 꼭짓점들
        triangle_cnt = np.array([pt1, pt2, pt3])
        # 삼각형 그리기
        cv2.drawContours(img, [triangle_cnt], 0, (0, 255, 0), -1) 
img = np.full((750, 750, 3), (0, 0, 0), dtype=np.uint8) # 750 * 750 크기의 검은 이미지 생성
makeGrid(img)
makeRock(img,'C:/Users/ehddn/project-x/3st_week/Q1/area_map.csv')
makeStruct(img,'C:/Users/ehddn/project-x/3st_week/Q1/area_category.csv','C:/Users/ehddn/project-x/3st_week/Q1/area_struct.csv')
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 보너스 과제는 진행하지 않았습니다.
