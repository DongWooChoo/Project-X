inventory_list = []

with open('C:/Users/ehddn/project-x/1st_week/Q3/Mars_Base_Inventory_List.csv', 'r', newline='', encoding='utf-8') as file:
    header = file.readline().strip().split(',')  # 헤더 처리
    for line in file:
        row = line.strip().split(',')  # 쉼표로 분할하여 각 열의 값을 리스트로 저장
        item = dict(zip(header, row))  # 헤더와 값들을 딕셔너리로 묶어서 리스트에 추가
        inventory_list.append(item)


inventory_list.sort(key=lambda x: float(x['Flammability']), reverse=True)

# 인화성 지수가 0.7 이상인 목록을 출력
for item in inventory_list:
    if float(item['Flammability']) >= 0.7:
        print(item)

# 인화성 지수가 0.7 이상인 목록을 CSV 파일로 저장
with open('Mars_Base_Inventory_danger.csv', 'w', newline='', encoding='utf-8') as danger_file:
    # 헤더 쓰기
    danger_file.write(','.join(header) + '\n')
    # 데이터 쓰기
    for item in inventory_list:
        if float(item['Flammability']) >= 0.7:
            danger_file.write(','.join(item[column] for column in header) + '\n')
