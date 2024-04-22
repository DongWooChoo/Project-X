import random
from Q6.mars_mission_computer import DummySensor
import time
class MissionComputer:
    def __init__(self): # 클래스 초기화 함수
        self.env_values = {
            'mars_base_internal_temperature' : str(random.randrange(18,31))+'도', # 화성 기지 내부 온도
            'mars_base_external_temperature' : str(random.randrange(0,22))+'도', # 화성 기지 외부 온도
            'mars_base_internal_humidity' : str(random.randrange(50,61))+'%', # 화성 기지 내부 습도
            'mars_base_external_illuminance' :str(random.randrange(500,716))+'W/m2',# 회성 기지 외부 광량
            'mars_base_internal_co2' :str(random.randrange(2,11)/100)+'%', # 화성 기지 내부 이산화탄소 농도
            'mars_base_internal_oxygen' :str(random.randrange(4,8)) + '%' # 화성 기지 내부 산소 농도
        }    
    def get_sensor_data(self,env_values): #센서 데이터를 가져오는 함수
        self.env_values = env_values
        return env_values
ds = DummySensor()
RunComputer = MissionComputer()
while(True):
    ds.set_env() # r값 갱신
    print('실행중 : ', RunComputer.get_sensor_data(ds.get_env())) # 값 출력
    time.sleep(5) # 5초마다 실행
