import sys
def getDayIndex(day):
    weekend = ['sunday','monday','tuesday','thursday','friday','saturday']
    return weekend.index(day)

def getMonthIndex(month):
    months = ['january','february','march','april','may','june','july','august','sepetmber','october','november','december']
    return months.index(month)+1
def getDate(order,day,month,startday_index,days):
    day_index = getDayIndex(day)
    first_day = (startday_index + sum(days[:month-1])) % 7
    first_weekday_date = (day_index - first_day + 7) % 7 + 1

    if order == last:
        dates = [d for d in range(first_weekday_date,days[month-1]+1,7)]
        return dates[-1]
    else :
        order_case = {
            "first" : 0,
            "second" : 1,
            "third" : 2,
            "fourth" : 3
        }
        return first_weekday_date + order_case[order] * 7
        
def calculateHoliday(year_type, start_day, holidays):
    results = []
    startday_index = getDayIndex(start_day):
    if year_type == "leap": # 윤년일 경우
        days = [31,29,31,30,31,30,31,31,30,31,30,31]
    else : 
        days = [31,28,31,30,31,30,31,31,30,31,30,31]
    for i in range(len(holidays)) :
        info = holidays[i].split()
        print(info)
        order = info[0] # 몇번째 주인지
        day = info[1] # 무슨 요일
        month = info[3] # 몇 월
        getDate(order,day,month,startday_index,days)
        results.append(f"{month} {date}")
    return results
        
year_type = input()
start_day = input()
T = int(input())
holidays = [input().strip() for _ in range(T)]
results = calculateHoliday(year_type, start_day, holidays)
for day in results:
    print(day)