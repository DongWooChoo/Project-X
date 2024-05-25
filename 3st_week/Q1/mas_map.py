import pandas as pd
def readfile(category_file,map_file,struct_file):
    category_dict = {}
    category_df = pd.read_csv(category_file, sep=',')
    map_df = pd.read_csv(map_file, sep=',')
    struct_df = pd.read_csv(struct_file, sep=',')
    print('area_map.csv 출력')
    print(map_df)
    print()
    print('area_struct.csv 출력')
    print(struct_df)
    # with pd.option_context('display.max_rows', None, 'display.max_columns', None): # 전체 출력하는 코드, pandas는 기본적으로 요약된 형태로 출력함
    #    print(struct_df)
    struct_df_temp = struct_df.merge(category_df, left_on='category',right_on='category',how='left') # category 칼럼을 기준으로 합침
    print()
    print('area_struct 파일에 시설 종류를 한글로 표현')
    print(struct_df_temp)
    struct_df = struct_df.merge(category_df, left_on='category',right_on='category',how="left") # category 칼럼을 기준으로 합침
    struct_df = struct_df.merge(map_df, on=['x', 'y'],how='left')
    print()
    print('area_map.csv, area_struct.csv, struct_category.csv 의 내용을 모두 병합')
    print(struct_df)
    print()
    print('area1의 데이터만 출력')
    area_1_data = struct_df['area'] == 1
    print(struct_df[area_1_data])
    
readfile('C:/Users/ehddn/project-x/3st_week/Q1/area_category.csv','C:/Users/ehddn/project-x/3st_week/Q1/area_map.csv','C:/Users/ehddn/project-x/3st_week/Q1/area_struct.csv')
