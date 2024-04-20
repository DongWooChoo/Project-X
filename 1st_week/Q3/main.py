def transform_list(inputfile,list_inventory) : # Mars_Base_Inventory_List.csv 내용을 읽어서 Python의 리스트(List) 객체로 변환하는 함수
    i = 0
    while True :
        line = inputfile.readline() # 한 줄 단위로 읽음
        if not line: #줄이 없다면
            break
        if i == 0:
            i+=1
            continue
        line = line.strip() # \n제거
        line = line.split(",") # ,기준으로 분할
        list_inventory.append(line) #, 기준으로 잘라서 리스트에 리스트 형태로 삽입
    return list_inventory

def sort_list(list_inventory): #배열 내용을 적제 화물 목록을 인화성이 높은 순으로 정렬하는 함수
    list_inventory = sorted(list_inventory, key = lambda x: x[4], reverse=True)
    return list_inventory

def extract_list(list_inventory,list_dangerous) : #0.7 이상되는 목록을 뽑아내는 함수
    for i in range(0,len(list_inventory)):
        if float(list_inventory[i][4]) > 0.7 :
            list_dangerous.append(list_inventory[i])
    return list_dangerous

def transform_csv(list_dangerous,outputfile):
    for i in range(0,len(list_dangerous)): # 출력
        line = str(list_dangerous[i])
        line = line.replace("[", "")
        line = line.replace("]","")
        line = line.replace("'","")
        line = line.replace("\n","")
        outputfile.writelines(line + "\n")

try :
    inputfile = open('C:/Users/ehddn/project-x/1st_week/Q3/Mars_Base_Inventory_List.csv', 'r')
    outputfile = open('C:/Users/ehddn/project-x/1st_week/Q3/Mars_Base_Inventory_danger.csv', 'w')
    #binoutputfile = open('C:/Users/ehddn/project-x/1st_week/Q3/Mars_Base_Inventory_List.bin', 'w')
except FileNotFoundError :
    print('파일이 존재하지 않습니다')
else :
    list_inventory = list(list())
    list_dangerous = list(list())
    transform_list(inputfile,list_inventory) #파일 내용을 리스트로 변환
    list_inventory = sort_list(list_inventory) # 인화성이 높은 순으로 정렬
    list_dangerous = extract_list(list_inventory,list_dangerous) # 0.7 이상되는 목록을 뽑아서 추출
    for i in range(0,len(list_dangerous)): # 출력
        print(list_dangerous[i])
    transform_csv(list_dangerous,outputfile)
    inputfile.close()
    outputfile.close()
    #binoutputfile.close()