import os
from PIL import Image, ImageTk
import tkinter as tk
import cv2

# 파일에 있는 이미지들을 반환하는 함수
def get_image_files(folder):
    print(f'Scanning folder: {folder}')
    files = [os.path.join(folder, file) for file in os.listdir(folder) if file.lower().endswith(('.png', '.jpg', '.jpeg'))]
    print(f'Found image files: {files}')
    return files

# 사람을 감지하는 함수
def detect_person(image_path):
    print(f'Detecting person in image: {image_path}')
    # OpenCV의 사전 훈련된 사람 탐지기를 로드합니다.
    person_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')
    
    if person_cascade.empty():
        print("Failed to load Haar Cascade. Please check the path to 'haarcascade_fullbody.xml'")
        return False
    
    # 이미지를 읽고 회색조로 변환합니다.
    image = cv2.imread(image_path)
    if image is None:
        print(f'Failed to load image: {image_path}')
        return False
    
    # 이미지를 리사이즈하여 감지 성능을 높입니다.
    image = cv2.resize(image, (image.shape[1] // 2, image.shape[0] // 2))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 사람을 감지합니다.
    people = person_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    if len(people) > 0:
        print(f'Detected {len(people)} person(s) in image: {image_path}')
    else:
        print(f'No person detected in image: {image_path}')
    
    return len(people) > 0

# 현재 이미지를 업데이트하는 함수
def update_image():
    global img_label, img_files, current_img
    print(f'Updating image to: {img_files[current_img]}')
    img = Image.open(img_files[current_img])
    img = ImageTk.PhotoImage(img)
    img_label.config(image=img)
    img_label.image = img

# 엔터키로 다음 이미지를 검색하는 함수
def search_next_image(event):
    global current_img
    while current_img < len(img_files):
        if detect_person(img_files[current_img]):
            update_image()
            current_img += 1
            return
        current_img += 1
    print('검색이 끝났습니다.')
    root.quit()

# 메인 프로그램
if __name__ == '__main__':
    # 업로드된 이미지 파일 경로
    extract_to = 'C:/Users/ehddn/project-x/2st_week/Q9/cctv'
    
    # 이미지 파일 목록 가져오기
    img_files = get_image_files(extract_to)
    
    if not img_files:
        print('이미지 파일이 없습니다.')
        exit()

    current_img = 0

    # GUI 설정
    root = tk.Tk()
    root.title('CCTV Viewer')

    img_label = tk.Label(root)
    img_label.pack()

    # 엔터키 바인딩
    root.bind('<Return>', search_next_image)

    # 첫 번째 검색 시작
    search_next_image(None)

    root.mainloop()
