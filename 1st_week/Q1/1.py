print('Hello Mars')  # 테스트 출력

def report_md(infile, outfile):
    try:
        with open(infile, 'r') as infile, open(outfile, 'w') as outfile:
            while True:
                line = infile.readline()
                print(line.strip())
                if not line:
                    break
                if 'unstable' in line or 'explosion' in line:
                    outfile.write('### 문제발생\n') #마크다운 형식
                    line = line.split(',')
                    outfile.write('시간: {}\n'.format(line[0]))
                    outfile.write('원인: {}\n'.format(line[2]))
                else:
                    outfile.write('### 정상\n')
                    line = line.split(',')
                    outfile.write('시간: {}\n'.format(line[0]))
                    outfile.write('내용: {}\n'.format(line[2]))
    except FileNotFoundError:                    #예외처리
        print('파일을 찾을 수 없거나 잘못된 파일 경로입니다.')

report_md('C:/Users/ehddn/project-x/1st_week/Q1/mission_computer_main.log', 'C:/Users/ehddn/project-x/1st_week/Q1/log_analysis.md')
