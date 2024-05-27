import pandas as pd
from collections import deque

def getShortestRoute(struct_df,matrix):
    start = None
    for r in range(len(matrix)): #시작 위치 찾기
        for c in range(len(matrix[0])):
            if matrix[r][c] == 'K':
                start = (r, c)
                break
        if start:
            break
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우 이동
    rows, cols = len(matrix), len(matrix[0])
    queue = deque([start])
    visited = set()
    visited.add(start)
    parent = {start: None}

    while queue:
        current = queue.popleft()
        if matrix[current[0]][current[1]] == 'U':
            return reconstructPath(struct_df,parent, start, current)
        
        for direction in directions:
            nr, nc = current[0] + direction[0], current[1] + direction[1]
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and matrix[nr][nc] != 1:
                queue.append((nr, nc))
                visited.add((nr, nc))
                parent[(nr, nc)] = current

    return None

def reconstructPath(struct_df,parent, start, end):
    path = []
    current = end
    while current != start:
        path.append(current)
        current = parent[current]
    path.append(start)
    path.reverse()
    print(path)
    createFile(struct_df,path)

def createFile(struct_df,path):
    max_x = max(struct_df['x'])
    max_y = max(struct_df['y'])
    map_list = [[0 for _ in range(max_x)] for _ in range(max_y)]
    for x,y in path:
        map_list[x][y] = 1
    try :
        outputfile = open('C:/Users/ehddn/project-x/3st_week/Q3/home_to_us_camp.csv', 'w')
    except FileNotFoundError :
        print("파일이 존재하지 않습니다")
    else :
        for row in map_list:
            line = ','.join(map(str, row))
            outputfile.write(line + '\n')

def readFile(category_file,map_file,struct_file):
    category_dict = {}
    category_df = pd.read_csv(category_file, sep=',')
    map_df = pd.read_csv(map_file, sep=',')
    struct_df = pd.read_csv(struct_file, sep=',')
    # with pd.option_context('display.max_rows', None, 'display.max_columns', None): # 전체 출력하는 코드, pandas는 기본적으로 요약된 형태로 출력함
    #    print(struct_df)
    struct_df_temp = struct_df.merge(category_df, left_on='category',right_on='category') # category 칼럼을 기준으로 합침
    struct_df_temp = struct_df.drop(columns='category') # category 칼럼을 제거함
    struct_df = struct_df.merge(category_df, left_on='category',right_on='category',how='left') # category 칼럼을 기준 왼쪽 기준 조인
    struct_df = struct_df.merge(map_df, on=['x', 'y'])
    #with pd.option_context('display.max_rows', None, 'display.max_columns', None): # 전체 출력하는 코드, pandas는 기본적으로 요약된 형태로 출력함
    #    print(struct_df['x'])
    index = 0
    max_x = max(struct_df['x'])
    max_y = max(struct_df['y'])
    matrix = [[None for _ in range(max_x)] for _ in range(max_y)]
    for i in range (1,max(struct_df['x']) + 1):
        for j in range (1,max(struct_df['y']) + 1):
            value = struct_df.loc[(struct_df['x'] == i) & (struct_df['y'] == j), 'mountain'].values
            struct_value = struct_df.loc[(struct_df['x'] == i) & (struct_df['y'] == j), 'struct'].values
            if (struct_value[0] == "Korea Mars Base"):
                value = "K"
            if (struct_value[0] == "U.S. Mars Base Camp"):
                value = "U"
            matrix[i-1][j-1] = value[0]
    getShortestRoute(struct_df,matrix)
    
    
readFile('C:/Users/ehddn/project-x/3st_week/Q1/area_category.csv','C:/Users/ehddn/project-x/3st_week/Q1/area_map.csv','C:/Users/ehddn/project-x/3st_week/Q1/area_struct.csv')

# 보너스 과제는 진행하지 않았습니다.