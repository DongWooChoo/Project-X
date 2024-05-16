import zipfile
import os
from PIL import Image, ImageTk
import tkinter as tk

# 파일 압축 해제 함수
def unlock_zip(zip_file_path, output_file_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        try:
            zip_ref.extractall(path=output_file_path)  # 암호를 이용하여 zip 파일 열기 시도
        except zipfile.BadZipFile:
            print("에러 발생")  # ZIP 파일 손상

# 파일에 있는 이미지들을 반환하는 함수
def get_image_files(folder):
    return [os.path.join(folder, file) for file in os.listdir(folder) if file.lower().endswith(('.png', '.jpg', '.jpeg'))]

# 현재 이미지를 업데이트하는 함수
def update_image():
    global img_label, img_files, current_img
    img = Image.open(img_files[current_img])
    img = ImageTk.PhotoImage(img)
    img_label.config(image=img)
    img_label.image = img

# 다음 이미지를 표시하는 함수
def show_next_image(event):
    global current_img
    current_img = (current_img + 1) % len(img_files)
    update_image()

# 이전 이미지를 표시하는 함수
def show_prev_image(event):
    global current_img
    current_img = (current_img - 1) % len(img_files)
    update_image()

# 메인 프로그램
if __name__ == '__main__':
    zip_path = 'C:/Users/ehddn/project-x/2st_week/Q9/cctv.zip'
    extract_to = 'C:/Users/ehddn/project-x/2st_week/Q9/cctv'

    # 압축 파일 풀기
    unlock_zip(zip_path, extract_to)

    # 이미지 파일 목록 가져오기
    img_files = get_image_files(extract_to)
    if not img_files:
        print("이미지 파일이 없습니다.")
        exit()

    current_img = 0

    # GUI 설정
    root = tk.Tk()
    root.title('CCTV Viewer')

    img_label = tk.Label(root)
    img_label.pack()

    # 키 바인딩
    root.bind('<Right>', show_next_image)
    root.bind('<Left>', show_prev_image)

    # 첫 번째 이미지 표시
    update_image()

    root.mainloop()
