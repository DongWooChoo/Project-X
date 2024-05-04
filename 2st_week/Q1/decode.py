import zipfile
import time

# aaaaaa부터 시작하여 999999까지 모든 경우를 작성하여 비밀번호를 열어보므로 올바른 코드라고 생각합니다. 다만 모든 경우의
# 숫자를 대입할 경우 매우 긴 시간이 걸리므로 출력에는 어려움이 있습니다.
def unlock_zip(zip_file_path,inputfile):
    start_time = time.time()
    found = False
    total_attempts = 0
    valid = 'abcdefghijklmnopqrstuvwxyz0123456789'
    password_file = open('C:/Users/ehddn/project-x/2st_week/Q1/password.txt', 'w')  # 파일을 한 번 열고 유지

    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            while True :
                password = inputfile.readline().strip() #한 줄 단위로 읽음
                total_attempts += 1
                if not password: #줄이 없다면
                    break
                try:
                    zip_ref.extractall(pwd=password.encode())  # 암호를 이용하여 zip 파일 열기 시도
                    print(f'Password 발견: {password}')
                    password_file.write(password + '\n')  # 비밀번호 파일에 쓰기
                    print(password)
                    found = True
                    break
                except Exception as e:
                    print(total_attempts, " : " ,password)
                    #print(f"Password 오류 '{password}'")
    
    except FileNotFoundError:
        print(f"The file {zip_file_path} does not exist.")
    except zipfile.BadZipFile:
        print("The ZIP file is corrupted.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        password_file.close()  # 비밀번호 파일을 닫음

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"총 시도 횟수: {total_attempts}")
    print(f"소요시간: {elapsed_time:.2f} 초")
inputfile = open('C:/Users/ehddn/project-x/2st_week/Q1/dict.txt', 'r')
unlock_zip('C:/Users/ehddn/project-x/2st_week/Q1/emergency_storage_key.zip',inputfile)
