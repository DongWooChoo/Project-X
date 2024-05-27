import cv2
import os

# 파일 이름이 이미지 파일인지 확인하는 함수
def is_image_file(filename):
    return filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))

# 지정된 폴더에서 이미지를 로드하는 함수
def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):  # 폴더 내 모든 파일을 순회
        if is_image_file(filename):  # 이미지 파일인지 확인
            img = cv2.imread(os.path.join(folder, filename))  # 이미지 파일 읽기
            if img is not None:  # 이미지가 유효한 경우
                images.append((filename, img))  # 파일 이름과 이미지를 리스트에 추가
    return images

# 이미지에서 사람을 감지하는 함수
def detect_person(image):
    hog = cv2.HOGDescriptor()  # HOGDescriptor 객체 생성
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())  # 사람 감지기를 설정
    (regions, _) = hog.detectMultiScale(image, winStride=(4, 4), padding=(4, 4), scale=1.05)  # 사람 감지
    return regions  # 감지된 영역 반환

# 메인 함수
def main():
    folder = 'path_to_cctv_images_folder'  # CCTV 이미지 폴더 경로 설정
    images = load_images_from_folder(folder)  # 폴더에서 이미지 로드
    if not images:  # 이미지가 없는 경우
        print('No images found in the specified folder.')  # 이미지가 없다는 메시지 출력
        return

    for filename, img in images:  # 로드된 모든 이미지를 순회
        regions = detect_person(img)  # 이미지에서 사람 감지
        for (x, y, w, h) in regions:  # 감지된 영역에 대해
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)  # 빨간색 사각형 그리기

        cv2.imshow('Image', img)  # 이미지를 화면에 표시
        print(f'Displaying {filename}. Press Enter to continue...')  # 사용자에게 Enter 키를 누르라는 메시지 출력
        cv2.waitKey(0)  # 키 입력 대기

    print('Search completed.')  # 모든 이미지 검색 완료 메시지 출력
    cv2.destroyAllWindows()  # 모든 창 닫기

# 프로그램 시작점
if __name__ == '__main__':
    main()  # 메인 함수 실행
