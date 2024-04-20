#구의 넓이 4πr²
#구의 단면 πr²
#반구체의 형태를 한 돔의 전체 면적 = 반구의 넓기 + 구의 단면
# 3πr² = 2πr² + πr²
# 지구의 중력 9.807m/s²
# 화성의 중력 3.71m/s²

def sphere_area(diameter, material = '유리', thickness = 1): #면적과 무게를 계산해주는 함수
    if material == '유리' :
        weight = 2.4
    if material == '알루미늄' :
        weight = 2.7
    if material == '탄소강' :
        weight = 7.85
    weight = convert_weight(weight)
    area = round((diameter/2)**2 * 3.141,3)
    dome_weight = round(area * thickness * weight,3)
    print('재질 =⇒ ', material, '지름 =⇒ ',diameter, '두께 =⇒ ',thickness, '면적 =⇒ ',area, '무게 =⇒ ',dome_weight, 'kg')
    return

def convert_weight(weight): #무게를 화성 기준으로 변환해주는 함수
    weight = round(weight / 9.807,3)
    weight = round(weight * 3.71,3)
    return weight

while(True):
    dome = 1000 # 돔의 길이 10m
    material = input('재질을 입력하시오 : ') # 재질
    if material not in('유리','알루미늄','탄소강'):
        print('올바르지 않은 값입니다. 다시 입력하세요 ')
        continue
    diameter = int(input('지름을 입력하시오 : ')) # 지름
    if diameter <= 0 :
        print('올바르지 않은 값입니다. 다시 입력하세요 ')
        continue
    sphere_area(diameter,material) # 두께는 값 추가시 파리미터 추가
    stop = inpu('종료하시려면 네를 입력하십시오 : ')
    if stop == '네':
        break
    print()
