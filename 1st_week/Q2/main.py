def transform_list(inputfile,list_log) : #리스트로 변경하는 함수
    i = 0
    while True :
        line = inputfile.readline() # 한 줄 단위로 읽음
        if not line: # 줄이 없다면
            break        
        line = line.split(',') # ,를 기준으로 문장을 나눔
        if i == 0 :
            i+=1
        else :
            line_list = list() # 각 줄마다의 정보를 담을 리스트 객체 
            for i in range(0,len(line)):
                line_list.append(line[i])
            list_log.append(line_list) # 한 줄의 정보가 담긴 리스트 객체를 넣음
    print('로그 리스트 출력')
    for i in range(len(log_list)): # 리스트에 있는 정보를 한 줄씩 읽음
        print(log_list[i])
    return list_log

def reverse_list(list_log): # 리스트를 역순으로 정렬하는 함수
    log_reverse_list = sorted(log_list, key=lambda x: x[0], reverse=True) # 역순 정렬 list안에 있는 list의 0번째 값은 날짜 정보
    return log_reverse_list

def transfrom_dict(log_list,log_dict,outputfile): # 로그 리스트를 딕셔너리 형태로 변환한 후 파일로 출력하는 함수
    for i in range(len(log_list)): # 로그에 있는 각 줄의 정보를 '키' : '라인넘버', '값' : '정보'의 형태로 추가
        log_dict[i] = log_list[i]
    # 딕셔너리 값을 json형태로 바꾸어서 저장
    outputfile.write('{\n') #\n은 다음 줄로
    #print(log_dict)
    i = 0
    for key,value in log_dict.items():
        value = str(value).replace("['",'["')
        value = str(value).replace("']",'"]')
        value = str(value).replace("',",'",')
        value = str(value).replace(" '",' "')
        if i == len(log_dict) - 1:
            outputfile.write('\t"' + str(key) + '":' + str(value)+'\n') # 맨마지막줄이면 , 생략
        else :
            outputfile.write('\t"' + str(key) + '":' + str(value)+',\n') #\t는 탭간격
        i+=1
    outputfile.write('}\n')
    
try :
    inputfile = open('C:/Users/ehddn/project-x/1st_week/Q2/mission_computer_main.log', 'r')
    outputfile = open('C:/Users/ehddn/project-x/1st_week/Q2/mission_computer_main.json', 'w')
except FileNotFoundError :
    print("파일이 존재하지 않습니다")
else :
    log_list = list() # 리스트 객체
    log_dict = dict() # 딕셔너리 객체
    transform_list(inputfile,log_list) # 로그파일을 리스트로 변환
    ######################################    
    log_list = reverse_list(log_list) # 로그 리스트를 역순으로 변환
    ######################################
    transfrom_dict(log_list,log_dict,outputfile) # 로그 리스트를 딕셔너리로 변환