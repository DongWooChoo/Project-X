import random
from Q6 import mars_mission_computer
import time
import os
import platform
import psutil
class MissionComputer:
    def __init__(self): # 클래스 초기화 함수
        try :
            self.env_values = {
                'mars_base_internal_temperature' : str(random.randrange(18,31))+'도', # 화성 기지 내부 온도
                'mars_base_external_temperature' : str(random.randrange(0,22))+'도', # 화성 기지 외부 온도
                'mars_base_internal_humidity' : str(random.randrange(50,61))+'%', # 화성 기지 내부 습도
                'mars_base_external_illuminance' :str(random.randrange(500,716))+'W/m2',# 회성 기지 외부 광량
                'mars_base_internal_co2' :str(random.randrange(2,11)/100)+'%', # 화성 기지 내부 이산화탄소 농도
                'mars_base_internal_oxygen' :str(random.randrange(4,8)) + '%' # 화성 기지 내부 산소 농도
            }    
            self.system_info = {
                'os' : platform.system(), #운영체계
                'os_version' : platform.version(), #운영체계 버전
                'cpu_type' : platform.processor(), #CPU의 타입
                'cpu_core' : os.cpu_count(), #CPU의 코어 수
                'memory_size' : psutil.Process(os.getpid()).memory_info().rss #메모리의 크기
            }
            self.system_load = {
                'cpu_usage' : psutil.cpu_percent(),
                'memory_usage' : psutil.virtual_memory().percent
            }
        except SystemError :
            print("시스템 오류가 발생했습니다")
        
    def get_sensor_data(self,env_values): #센서 데이터를 가져오는 함수
        self.env_values = env_values
        return env_values
    
    def get_mission_computer_info(self): # 컴퓨터 정보를 json형태로 출력하는 함수
        i = 0
        print('{')
        for key,value in self.system_info.items():
            if i == len(self.system_info) - 1:
                print('\t"' + str(key) + '":"' + str(value)+'"') # 맨마지막줄이면 , 생략
            else :
                print('\t"' + str(key) + '":"' + str(value)+'",') #\t는 탭간격
            i+=1
        print('}')
        return
    
    def get_mission_computer_load(self):
        i = 0
        print('{')
        for key,value in self.system_load.items():
            if i == len(self.system_load) - 1:
                print('\t"' + str(key) + '":"' + str(value)+'"') # 맨마지막줄이면 , 생략
            else :
                print('\t"' + str(key) + '":"' + str(value)+'",') #\t는 탭간격
            i+=1
        print('}')
        return
    
def main():
    ds = mars_mission_computer.DummySensor()
    RunComputer = MissionComputer()
    print("===컴퓨터 시스템 정보===")
    RunComputer.get_mission_computer_info()
    print("===컴퓨터 부하 정보===")
    RunComputer.get_mission_computer_load()
    while(True):
        ds.set_env() # r값 갱신
        print('실행중 : ', RunComputer.get_sensor_data(ds.get_env())) # 값 출력
        time.sleep(5) # 5초마다 실행
        
if __name__ == "__main__":
    main()
