import zipfile
import time

# aaaaaa부터 시작하여 999999까지 모든 경우를 작성하여 비밀번호를 열어보므로 올바른 코드라고 생각합니다. 다만 모든 경우의
# 숫자를 대입할 경우 매우 긴 시간이 걸리므로 출력에는 어려움이 있습니다.
def unlock_zip(zip_file_path):
    start_time = time.time()
    found = False
    total_attempts = 0
    valid = 'mabcdefghijklnopqrstuvwxyz0123456789'
    password_file = open('C:/Users/ehddn/project-x/2st_week/Q1/password.txt', 'w')  # 파일을 한 번 열고 유지

    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            for a in valid:
                for b in valid:
                    for c in valid:
                        for d in valid:
                            for ef in valid:
                                for f in valid:
                                    password = a + b + c + d + ef + f  # 암호 생성
                                    total_attempts += 1  # 시도 횟수 증가
                                    try:
                                        zip_ref.extractall(pwd=password.encode())  # 암호를 이용하여 zip 파일 열기 시도
                                        print(f'Password 발견: {password}')
                                        password_file.write(password + '\n')  # 비밀번호 파일에 쓰기
                                        found = True
                                        break
                                    except RuntimeError:
                                        continue  # 비밀번호 오류 무시
                                    except zipfile.BadZipFile:
                                        continue  # ZIP 파일 손상 무시
                                    except Exception as e:
                                        print(f"Password 오류 '{password}'")
                            if found:
                                break
                        if found:
                            break
                    if found:
                        break
                if found:
                    break
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

unlock_zip('C:/Users/ehddn/project-x/2st_week/Q1/emergency_storage_key.zip')
