import speech_recognition as sr

# 음성 파일 경로
audio_file = "2024514-11211.wav"

# 인식기 초기화
recognizer = sr.Recognizer()

# 음성 파일을 오디오 데이터로 변환
with sr.AudioFile(audio_file) as source:
    audio_data = recognizer.record(source)

# 음성 인식을 통한 텍스트 변환
try:
    # 한국어 음성 인식
    text = recognizer.recognize_google(audio_data, language="ko-KR")
    print("음성에서 추출한 텍스트: ", text)

    # 텍스트를 파일로 저장
    with open("output_text.txt", "w", encoding="utf-8") as file:
        file.write(text)

    print("텍스트가 output_text.txt 파일에 저장되었습니다.")

except sr.UnknownValueError:
    print("음성을 인식할 수 없습니다.")
except sr.RequestError as e:
    print(f"구글 음성 인식 서비스에 접근할 수 없습니다. 에러: {e}")
