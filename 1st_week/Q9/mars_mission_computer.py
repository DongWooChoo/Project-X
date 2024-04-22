import random
import platform
import os
import time
import threading
import multiprocessing
import psutil

class MissionComputer:
    def __init__(self):
        self.system_info = {
            'os': platform.system(),
            'os_version': platform.version(),
            'cpu_type': platform.processor(),
            'cpu_core': os.cpu_count(),
            'memory_size': psutil.Process(os.getpid()).memory_info().rss
        }
        self.system_load = {
            'cpu_usage': psutil.cpu_percent(interval=1),
            'memory_usage': psutil.virtual_memory().percent
        }
        self.env_values = {
            'mars_base_internal_temperature': str(random.randrange(18, 31)) + '도',
            'mars_base_external_temperature': str(random.randrange(0, 22)) + '도',
            'mars_base_internal_humidity': str(random.randrange(50, 61)) + '%',
            'mars_base_external_illuminance': str(random.randrange(500, 716)) + 'W/m2',
            'mars_base_internal_co2': str(random.randrange(2, 11) / 100) + '%',
            'mars_base_internal_oxygen': str(random.randrange(4, 8)) + '%'
        }

    def get_sensor_data(self):
        print('Sensor Data:', self.env_values)

    def get_mission_computer_info(self):
        print('Mission Computer Info:', self.system_info)

    def get_mission_computer_load(self):
        print('Mission Computer Load:', self.system_load)

def task(interval, target_function): # 작업을 수행하는 함수, 작업 수행 간격와 작업 내용 전달
    while True:
        target_function()
        time.sleep(interval)

if __name__ == '__main__':
    # 인스턴스 생성
    runComputer1 = MissionComputer()
    runComputer2 = MissionComputer()
    runComputer3 = MissionComputer()

    # 스레드를 사용하여 인스턴스가 20초마다 함수가 실행되도록 함
    #t1 = threading.Thread(target=task, args=(20, runComputer1.get_mission_computer_info))
    #t2 = threading.Thread(target=task, args=(20, runComputer1.get_mission_computer_load))
    #t3 = threading.Thread(target=task, args=(20, runComputer1.get_sensor_data))

    # 실행
    #t1.start()
    #t2.start()
    #t3.start()

    # 멀티프로세서를 이용하여 인스턴스가 20초마다 함수가 실행되도록 함
    p1 = multiprocessing.Process(target=task, args=(20, runComputer2.get_mission_computer_info))
    p2 = multiprocessing.Process(target=task, args=(20, runComputer2.get_mission_computer_load))
    p3 = multiprocessing.Process(target=task, args=(20, runComputer3.get_sensor_data))

    # 실행
    p1.start()
    p2.start()
    p3.start()
