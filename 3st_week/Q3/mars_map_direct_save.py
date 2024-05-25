import pandas as pd
def readfile(category_file,map_file,struct_file):
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
    with pd.option_context('display.max_rows', None, 'display.max_columns', None): # 전체 출력하는 코드, pandas는 기본적으로 요약된 형태로 출력함
        print(struct_df)
    
readfile('C:/Users/ehddn/project-x/3st_week/Q1/area_category.csv','C:/Users/ehddn/project-x/3st_week/Q1/area_map.csv','C:/Users/ehddn/project-x/3st_week/Q1/area_struct.csv')
