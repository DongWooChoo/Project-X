# 수행과제 
# 로그 분석을 위해 Python으로 소프트웨어를 개발해야 한다. 이를 위해서 먼저 Python을 설치해야 한다. 
# 빠른 개발을 위해 Python 개발 도구들을 알아보고 비교해서 하나의 도구를 선정해서 설치한다.
# 설치가 잘 되었는지 확인 하기 위해서 ‘Hello Mars’를 출력해 본다. 
# 본격적으로 로그를 분석하기 위해서 mission_computer_main.log 파일을 열고 전체 내용을 화면에 출력해 본다.  이때 코드는 main.py 파일로 저장한다. (로그 데이터는 별도 제공)
# 파일을 처리 할 때에 발생할 수 있는 예외를 처리한다. 
# mission_computer_main.log의 내용을 통해서 사고의 원인을 분석하고 정리해서 보고서(log_analysis.md)를 Markdown 형태로 를 작성해 놓는다. 

def reverse(inputfile): # 파일을 역순으로 변환하는 함수
    data = inputfile.readlines()
    reversed_data = sorted(data,reverse = True) #데이터를 역순으로 정렬함
    #for i in range(len(reversed_data)): # 각 문장을 출력
    #    print(reversed_data[i].strip()) # 문장에 \n기호가 있기때문에 이를 없앰
        
def write_md(inputfile,outfile): # 파일을 md로 작성하는 함수
    i = 0
    outfile.write('# 사고 원인 분석 보고서\n')
    while True :
        line = inputfile.readline() # 한 줄 단위로 읽음
        print(line.strip())
        if not line: #줄이 없다면
            break
        if line.count('start') or line.count('complete') : #출력 결과 중 문제가 되는 부분만 따로 파일로 저장한다. 
            outfile.write("### 진행 경과\n")
            line = line.split(",")
            outfile.write('시간 : ' + line[0])
            outfile.write('\n내용 : ' + line[2])
        if line.count('unstable') or line.count('explosion') : #출력 결과 중 문제가 되는 부분만 따로 파일로 저장한다. 
            outfile.write('### 사고 발생\n')
            line = line.split(',')            
            outfile.write('시간 : ' + line[0])
            outfile.write('\n내용 : ' + line[2])
    return outfile

def write_error(inputfile,outfile): # 파일중 에러문구를 찾아 따로 저장하는 함수
    i = 0
    while True :
        line = inputfile.readline() #한 줄 단위로 읽음
        if not line: #줄이 없다면
            break
        if line.count('unstable') or line.count('explosion') : #출력 결과 중 문제가 되는 부분만 따로 파일로 저장한다. 
            outfile.write(line)
    return outfile

print('Hello Mars')

try :
    inputfile = open('C:/Users/ehddn/project-x/1st_week/Q1/mission_computer_main.log', 'r')
    outputfile = open('C:/Users/ehddn/project-x/1st_week/Q1/log_analysis.md', 'w', encoding='utf-8')
    erroroutputfile = open('C:/Users/ehddn/project-x/1st_week/Q1/error_analysis.md', 'w', encoding='utf-8')
except FileNotFoundError :
    print('파일이 존재하지 않습니다')
else :
    write_md(inputfile,outputfile)
    inputfile.seek(0) # 파일의 위치를 맨 위로 옮김
    reverse(inputfile)
    inputfile.seek(0) # 파일의 위치를 맨 위로 옮김
    write_error(inputfile,erroroutputfile)
    inputfile.close()
    outputfile.close()
    erroroutputfile.close()

