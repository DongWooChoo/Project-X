import numpy

def read_file(filename): #파일을 읽어와서 array를 반환하는 함수
    try :
        data = numpy.genfromtxt(filename, delimiter=',', dtype='U50', skip_header=1) # 첫줄은 무시, U50 = 각 필드를 최대 50자 길이의 유니코드 문자열로 처리
    except FileExistsError :
        print('해당 파일이 존재하지 않습니다')
        return
    else :
        return data

def get_avg(parts):
    print(parts)
    item_avg_list = []
    item_list = numpy.unique(parts[:, 0])  # 재료들의 리스트를 가져옴
    for item in item_list:
        index = parts[:, 0] == item #해당 아이템에 해당하는 index를 가져옴 ex) 0,0,0,1,0,0,0,0,1\
        values = parts[index, 1].astype(int)  # 해당 인덱스의 값들을 가져옴
        average = numpy.mean(values)  # 평균 계산
        item_avg_list.append([item, average])
    return item_avg_list

def save_item_file(item_avg_list,parts,file_name):
    save_item_list = []
    save_list = []
    for i in range(len(item_avg_list)): #아이템 평균 값 리스트에서 50보다 작은 값만 따로 save_item_list에 추가
        if item_avg_list[i][1] < 50 :
            print(item_avg_list[i][0])
            save_item_list.append(item_avg_list[i][0])
    for item in save_item_list:
        index = parts[:, 0] == item
        save_list.extend(parts[index].tolist())  # extend를 사용하여 부분 배열을 추가
    
    try:
        numpy.savetxt(file_name, save_list, fmt='%s,%s', delimiter=',', header='parts,strength', comments='')
    except FileExistsError :
        print('해당 파일이 존재하지 않습니다')
        return
    else :
        return 
        
file1 = 'C:/Users/ehddn/project-x/1st_week/Q5/mars_base_main_parts-001.csv'
file2 = 'C:/Users/ehddn/project-x/1st_week/Q5/mars_base_main_parts-002.csv'
file3 = 'C:/Users/ehddn/project-x/1st_week/Q5/mars_base_main_parts-003.csv'
savefile = 'C:/Users/ehddn/project-x/1st_week/Q5/parts_to_work_on.csv'
array1 = numpy.array(read_file(file1))
array2 = numpy.array(read_file(file2))
array3 = numpy.array(read_file(file3))
parts = numpy.concatenate([array1, array2, array3],axis=0) #2차원 이상의 배열은 합칠 축을 정할 수 있다. 0,default는 가로축, 1은 세로축
item_avg_list = get_avg(parts)
save_item_file(item_avg_list,parts,savefile)
