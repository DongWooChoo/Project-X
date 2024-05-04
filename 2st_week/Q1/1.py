# -*- coding:utf-8 -*-
import zipfile  # zip 으로 압축된 파일 객체를 생성 할 수 있다.
from threading import Thread # 스레드 기법을 통해 빠른 프로세스 처리를 도와준다.
import optparse # 사용자 입력값을 파싱 처리한 후, 미리 정의해둔 정의에 따라 해당 내용을 처리할 수 있게 해준다.

def Extract_File(zFile, password): # 압축 파일을 불러온 후 비밀번호를 대입하여 해제하는 영역
# zFile 은 실제 압축 파일 객체를 가리키고 있으며, Password 는 딕셔너리 파일에서 읽어들인 단어가 들어가게 될 것이다.
    try:
        zFile.extractall(pwd=password)
        print ("Found Password is ............ "+password+"\n"  )

    except Exception :
        pass

def main():

    parser = optparse.OptionParser(usage="%prog " + "-f  -d ") # parser 변수를 통해 optparse 라이브러리를 객체화 시킨 후, 사용자 기본 Usage 메시지를 입력한다. python test.py -f Test.zip -d dictionary.txt
    parser.add_option("-f", dest="zname", type="string", help="Specify Zip File")
    parser.add_option("-d", dest="dname", type="string", help="Specify Dictionary Name")
    (options, args) = parser.parse_args() # 튜플 형의 변수에 parse_args() 메서드를 호출하면 options 과 args 가 분리되어 저장되게 된다.
    if (options.zname == None) | (options.dname == None) :
        print parser.usage
        exit(0)
    else:
        zname = options.zname
        dname = options.dname

# Main Function Area - zFile

    zFile = zipfile.ZipFile(zname) # zFile 변수는 zipFile 모듈을 통해 (zname - optparser 를 통해 입력받은 )압축 파일명을 불러들인다.
    passfile = open(dname,"r")

    print ("Extraction Start ------------ \n")

    for line in passfile.readlines(): # for 문을 통해 딕셔너리 파일을 한 라인씩 읽으면서 extract_file 함수를 호출한다.
        password = line.strip("\n")
        t = Thread(target=Extract_File, args=(zFile, password))
        t.start()

if __name__ == '__main__' :
    main ()