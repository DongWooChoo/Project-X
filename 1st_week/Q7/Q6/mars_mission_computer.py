import random
class DummySensor:
    def __init__(self): # 클래스 초기화 함수
        self.env_values = {
            'mars_base_internal_temperature' : str(random.randrange(18,31))+'도', # 화성 기지 내부 온도
            'mars_base_external_temperature' : str(random.randrange(0,22))+'도', # 화성 기지 외부 온도
            'mars_base_internal_humidity' : str(random.randrange(50,61))+'%', # 화성 기지 내부 습도
            'mars_base_external_illuminance' :str(random.randrange(500,716))+'W/m2',# 회성 기지 외부 광량
            'mars_base_internal_co2' :str(random.randrange(2,11)/100)+'%', # 화성 기지 내부 이산화탄소 농도
            'mars_base_internal_oxygen' :str(random.randrange(4,8)) + "%" # 화성 기지 내부 산소 농도
        }
    
    def set_env(self): # env 정 함수
        self.env_values = {
            'mars_base_internal_temperature' : str(random.randrange(18,31))+'도', # 화성 기지 내부 온도
            'mars_base_external_temperature' : str(random.randrange(0,22))+'도', # 화성 기지 외부 온도
            'mars_base_internal_humidity' : str(random.randrange(50,61))+'%', # 화성 기지 내부 습도
            'mars_base_external_illuminance' :str(random.randrange(500,716))+'W/m2',# 회성 기지 외부 광량
            'mars_base_internal_co2' :str(random.randrange(2,11)/100)+'%', # 화성 기지 내부 이산화탄소 농도
            'mars_base_internal_oxygen' :str(random.randrange(4,8)) + "%" # 화성 기지 내부 산소 농도
        }
    
    def get_env(self): # env 반환 함수
        return self.env_values

def main():
    ds = DummySensor()
    print('초기값 : ', ds.get_env())
    ds.set_env()
    print('수정값 : ', ds.get_env())
    ds.set_env()
    print('수정값 : ', ds.get_env())
if __name__ == "__main__":
    main()