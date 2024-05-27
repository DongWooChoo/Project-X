import cv2
import numpy as np

# CSV 파일을 읽어 2차원 리스트로 변환하는 함수
def read_csv_to_matrix(filename):
    matrix = []
    with open(filename, mode='r') as file:
        for line in file:
            row = list(map(int, line.strip().split(',')))
            matrix.append(row)
    return matrix

# 2차원 리스트를 시각화하는 함수
def plot_matrix(matrix):
    # numpy 배열로 변환
    array = np.array(matrix, dtype=np.uint8)

    # 크기 조정을 위해 이미지 확대
    scale = 20  # 확대 비율
    array = cv2.resize(array, (array.shape[1] * scale, array.shape[0] * scale), interpolation=cv2.INTER_NEAREST)

    # 색상 변환 (0은 흰색, 1은 검은색)
    array = cv2.cvtColor(array, cv2.COLOR_GRAY2BGR)

    # 이미지 보여주기
    cv2.imshow('Path Map', array)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# CSV 파일에서 2차원 리스트 읽기
matrix = read_csv_to_matrix('C:\Users\ehddn/project-x/3st_week/Q4/home_to_us_camp.csv')

# 2차원 리스트 시각화
plot_matrix(matrix)
