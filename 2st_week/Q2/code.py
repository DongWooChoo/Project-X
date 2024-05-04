def caesar_cipher_decode(target_text, shift):
    decoded_text = ''
    for char in target_text:
        if char.isalpha():
            start = 'a' if char.islower() else 'A'
            shifted = ord(start) + (ord(char) - ord(start) + shift) % 26
            decoded_text += chr(shifted)
        else:
            decoded_text += char
    return decoded_text

def main():
    try:
        with open('C:/Users/ehddn/project-x/2st_week/Q2/password.txt', 'r') as file:
            encrypted_text = file.read().strip()

        print('자리수에 따라 이동 한 암호')
        for i in range(26):
            decoded = caesar_cipher_decode(encrypted_text, i)
            print(f'Shift {i}: {decoded}')

        shift_used = int(input('적절한 자리수 이동의 수를 고르세요: '))
        correct_decoded_text = caesar_cipher_decode(encrypted_text, shift_used)

        with open('C:/Users/ehddn/project-x/2st_week/Q2/result.txt', 'w') as file:
            file.write(correct_decoded_text)
            
    except Exception :
        print('에러발생')
        
if __name__ == '__main__':
    main()
