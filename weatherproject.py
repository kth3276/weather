'''
tkinter(tk) : Python에서 그래픽 사용자 인터페이스(GUI)를 개발할 때 필요한 모듈
GUI : 메뉴, 툴바 및 다양한 위젯들을 통해 사용자와 대화 진행하여 결과출력
-이벤트 처리방식(메시지 구동방식) : 해당 이벤트 처리 함수 호출
-사용된 위젯 : Frame(다른 위젯을 수용하는 컨테이너 위젯), Canvas(그래프 및 도안 위젯), Message(텍스트 출력 위젯)
'''

import tkinter as tk # "tk"로 이름을 변경하여 타이핑을 저장
from tkinter import* # 모든 노출 된 객체를 현재 네임 스페이스로 가져오기
from tkinter import messagebox
import urllib.request # url로 표기된 네트워크 객체를 지역파일로 가져오기
import json # json파일 불러오기 위해

# 0. API 값 받아오기
apiurl = 'http://api.openweathermap.org/data/2.5/forecast?q='
apikey = '&APPID=b9d33ef7c9243e70efdc44370aca35d0'
city = ['London', 'Paris', 'Prague', 'Florence', 'Budapest']

# 1. 데이터를 받아 출력 형태 만들기
class WT :
    def weather(self, num, num2):   # num은 도시를 위한 변수, num2는 날짜를 위한 변수
        self.num = num
        self.num2 = num2
        url = urllib.request.urlopen(apiurl + city[num - 1] + apikey)
        apid = url.read()
        data = json.loads(apid)
        cityname = data['city']['name']
        weather = data['list'][3+8*num2]['weather'][0]['main']
        temp = int(data['list'][3+8*num2]['main']['temp'] - 273.15)
        return "도시:", cityname, "날씨:", weather, "온도:", str(temp), "˚C"

    def getWeather(self, num, num2):
        url = urllib.request.urlopen(apiurl + city[num - 1] + apikey)
        apid = url.read()
        data = json.loads(apid)
        weather = data['list'][3+8*num2]['weather'][0]['main']
        return weather

    def getTemp(self, num, num2):
        url = urllib.request.urlopen(apiurl + city[num - 1] + apikey)
        apid = url.read()
        data = json.loads(apid)
        temp = int(data['list'][3+8*num2]['main']['temp'] - 273.15)
        return str(temp)

# 2. 출력 데이터 입력(준비물, 추천 일정)
class Trip:
    unclearW = {"Rain": "우산,장화,비옷,가방 방수덮개", "Snow": "장갑,목도리,우산,가방 방수덮개", "Haze": "마스크,지도,물", "Mist": "마스크,지도,물"}
    clearW = {"Sun": "물,선글라스,선크림,카메라", "Clouds": "물,바람막이,선크림,카메라", "Clear": "음료수,선글라스,사진빨 잘받는 옷"}
    act = {
        "LondonIn": "(아침) 빌즈 브런치 -> 영국박물관 -> (점심) 플랫아이언 스테이크 -> 버버리아울렛 "
                    "-> 영국도서관(해리포터특별전) -> (저녁) 파이브가이즈(칼로리 폭탄 햄버거) -> 뮤지컬관람(라이언킹,위키드)"
        , "LondonOut": "세인트제임스파크 -> 버킹엄궁전(근위병교대식) -> (점심) 피쉬앤칩스 (빅토리아파크) -> 빅밴"
                       " -> 타워브릿지 -> (저녁) 버로우마켓 -> 런던아이"
        , "ParisIn": "포숑초콜릿 -> 루브르박물관 -> (점심) 레종브레 양고기 스테이크 -> 샹젤리제거리 쇼핑"
                     " -> 몽쥬약국 핸드크림 쓸어담기 -> (저녁) 사랑 한식집에서 간만에 한식 -> 에펠탑 야경"
        , "ParisOut": "베르사유궁전 -> (점심) 레몽드브뤼셀 홍합스튜 -> 몽마르뜨언덕 초상화 그리고 젤라또 냠냠"
                      " -> (저녁) 리로얄 에스까르고 -> 바토무슈 유람선 -> 개선문"
        , "PragueIn": "(아침) 굴뚝빵 -> 프라하성 -> (점심) 소세지세트 -> 루돌피눔(공연관람) -> (저녁) 콜레뇨&다크코젤"
                      " -> 세계3대클럽가기(5층규모)"
        , "PragueOut": "체스키 스카이다이빙 -> (점심) 크레이지카우 티본스테이크 -> 팁투어(구시가광장, 존레논벽)"
                       " -> (저녁) 밥리츠에서 김치찌개 -> 까를교"
        , "BudapestIn": "세체니온천 -> (점심) 굴라쉬 -> 성이슈트반 대성당 -> 부다페스트 시장"
                        " -> (저녁) 오리스테이크 -> 뉴욕카페에서 맥쭈우"
        , "BudapestOut": "영웅광장 -> (점심) 멘자 오믈렛 -> 어부의요새 -> 부다왕궁 -> (저녁) 바치거리에서 맥주 캬!"
                         " -> 세체니다리 -> 세체니유람선 -> 국회의사당"
        , "FlorenceIn": "더몰(구찌털기) or 프라다스페이스(프라다털기) -> (점심) 중앙시장 마르게리따 피자"
                        " -> 우피치미술관 -> (저녁) 봉골레파스타 -> 가죽시장"
        , "FlorenceOut": "피사의사탑 -> (점심) 이탈리아 맥도날드 가즈아!! -> 친퀘테레 마을 -> (저녁) 부르스게타"
                         " -> 미켈란젤로광장 -> 두오모성당 가는 길 젤라또 마시썽 -> 베키오다리에서 인생샷"}


# 3. 출력 프로그램(비행기와 지도)
class Gui(tk.Frame): # 뼈대
    def __init__(self, parent): # parent는 부모클래스 의미 -> Tk의미
        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(parent, width=800, height=580) # 이미지 크기에 맞는 창크기 설정
        self.wall = PhotoImage(file='europe.png')
        self.canvas.create_image(0, 0, image=self.wall, anchor=NW) # anchor: 위치설정
        self.canvas.pack(fill="both", expand=True) # 위젯들을 부모 위젯에 모두 패킹하여 불필요한 공간 없애기
        self.imp = PhotoImage(file='tplane2.png')
        # self.ball=self.canvas.create_image(50, 50, anchor=NE, image=self.imp)
        self.objects = [self.canvas.create_image(780, 550, image=self.imp)] # 비행기 위치

        for i in range(0, N): #0~도시의 수
            if journey[i] == 1: # 런던
                self.destinations = [[296,168]]
                self.speed = 5
                self.start_move_sequence()
                messagebox.showinfo("여행할 도시: 런던", "Weather in London : " + s[i] +
                                    "\nTemperature in London : " + t[i] +
                                    "\n추천 일정을 확인하시겠습니까?")
                messagebox.showinfo("2018년 2월 %d일" % (8+i), "런던 추천일정: \n" + activity[i] +
                                    "\n\n준비물: " + item[i])
            elif journey[i] == 2: # 파리
                self.destinations = [[356, 272]]
                self.speed = 5
                self.start_move_sequence()
                messagebox.showinfo("여행할 도시: 파리", "Weather in Paris : " + s[i] +
                                    "\nTemperature in Paris : " + t[i] +
                                    "\n추천 일정을 확인하시겠습니까?")
                messagebox.showinfo("2018년 2월 %d일" % (8+i), "파리 추천일정: \n" + activity[i] +
                                    "\n\n준비물: " + item[i])
            elif journey[i] == 3: # 프라하
                self.destinations = [[610,224]]
                self.speed = 5
                self.start_move_sequence()
                messagebox.showinfo("여행할 도시: 프라하", "Weather in Prague : " + s[i] +
                                    "\nTemperature in Prague : " + t[i] +
                                    "\n추천 일정을 확인하시겠습니까?")
                messagebox.showinfo("2018년 2월 %d일" % (8+i), "프라하 추천일정: \n" + activity[i] +
                                    "\n\n준비물: " + item[i])
            elif journey[i] == 4: # 부다페스트
                self.destinations = [[719,322]]
                self.speed = 5
                self.start_move_sequence()
                messagebox.showinfo("여행할 도시: 플로렌스", "Weather in Florence : " + s[i] +
                                    "\nTemperature in Florence : " + t[i] +
                                    "\n추천 일정을 확인하시겠습니까?")
                messagebox.showinfo("2018년 2월 %d일" % (8+i), "플로렌스 추천일정: \n" + activity[i] +
                                    "\n\n준비물: " + item[i])
            elif journey[i] == 5: # 플로렌스
                self.destinations = [[567,447]]
                self.speed = 5
                self.start_move_sequence()
                messagebox.showinfo("여행할 도시: 부다페스트", "Weather in Budapest : " + s[i] +
                                    "\nTemperature in Budapest : " + t[i] +
                                    "\n추천 일정을 확인하시겠습니까?")
                messagebox.showinfo("2018년 2월 %d일" % (8+i), "부다페스트 추천일정: \n" + activity[i] +
                                    "\n\n준비물: " + item[i])
        else:
            messagebox.showinfo("(주)개추엉투어", "이용해주셔서 감사합니다.")

    def start_move_sequence(self): # 캔버스의 여러 객체들의 기본값 설정
           # sequence : 여러 객체들을 저장하는 저장 자료형. (객체들은 순서를 갖는다)
           #             []()를 통해 공통연산 가능
        self.moveDone = False
        self.count = 0
        self.run_move_sequence()

    def run_move_sequence(self): # 캔버스의 항목을 순차적으로 이동하기위해 메소드를 정의
        if self.moveDone == False:
            self.move_object(self.objects[self.count], self.destinations[self.count])
            self.canvas.after(self.speed, self.run_move_sequence)
        else:
            # Start run_move_sequence on the next object
            self.count += 1
            if self.count < len(self.objects):
                self.moveDone = False
                self.run_move_sequence()

    def move_object(self, object_id, destination): # 비행기 경로 지정
        dest_x, dest_y = destination
        coords = self.canvas.coords(object_id)
        current_x, current_y = coords[1], coords[0] # 비행기 경로 지정
                                                    #  0,0 : 4사분면-1,2사분면      #1,0 : 4사분면-1사분면

        new_x, new_y = current_x, current_y
        delta_x = delta_y = 0
        if current_x < dest_x:
            delta_x = 1
        elif current_x > dest_x:
            delta_x = -1

        if current_y < dest_y:
            delta_y = 1
        elif current_y > dest_y:
            delta_y = -1

        if (delta_x, delta_y) != (0, 0):
            self.canvas.move(object_id, delta_x, delta_y)

        if (new_x, new_y) == (dest_x, dest_y):
            self.moveDone = True


# 4. 프로그램 개요
print("====================== 프로그램 개요 ===========================")
print("2월 8일부터 최대 5일간 밑에있는 목록의 도시들을 여행하고자 한다.")
print("1: London / 2: Paris / 3: Prague / 4: Florence / 5: Budapest")

# 5. 도시 수 입력받기
while 1:
    N = int(input("가고싶은 도시 수를 입력하세요(최대 5개): "))
    if N <= 0 or N > 5:
        print("1~5 사이의 수를 입력해 주세요")
        continue
    else:
        break

# 6. 여정 입력받기
wt = WT()
while True:
    journey = input("날짜별 방문 도시를 숫자로 입력해주세요(띄어쓰기 구분): ").split()  # journey 에는 일정이 저장되어 있음
    s = ["", "", "", "", ""]  # 날씨를 받는다
    t = [0, 0, 0, 0, 0]       # 기온을 받는다
    for i in range(len(journey)):
        journey[i] = int(journey[i])
        if journey[i] <= 0 or journey[i] > 5:
            print("주어진 도시의 범위를 벗어났습니다. 다시 입력해주세요.(1~5)")
            break
        if len(journey) != N:
            print("입력한 도시의 개수가 다릅니다. 다시 입력해주세요.")
            break
        s[i] = WT.getWeather(wt, journey[i], i)
        t[i] = WT.getTemp(wt, journey[i], i)
    if s[N-1] == "":
        continue
    else:
        break

#  7. 도시별, 날짜별 날씨 출력
print()
print("==== 도시별 날씨 ====")
for i in range(0, len(journey)):
    print("    2018년 2월 %d일"%(8+i))
    journey[i] = int(journey[i])
    print(WT.weather(wt, journey[i], i))
print()

# 8. 도시, 날씨별 추천 활동 받기
activity = []  # 날씨별 활동
item = []  # 날씨별 준비물
for i in range(0, len(journey)):
    if journey[i] == 1: # 런던
        if s[i] in Trip.clearW:
            activity.append(Trip.act.get('LondonOut'))
            item.append(Trip.clearW.get(WT.getWeather(wt, journey[i], i)))
        else:
            activity.append(Trip.act.get('LondonIn'))
            item.append(Trip.unclearW.get(WT.getWeather(wt, journey[i], i)))
    elif journey[i] == 2: # 파리
        if s[i] in Trip.clearW:
            activity.append(Trip.act.get('ParisOut'))
            item.append(Trip.clearW.get(WT.getWeather(wt, journey[i], i)))
        else:
            activity.append(Trip.act.get('ParisIn'))
            item.append(Trip.unclearW.get(WT.getWeather(wt, journey[i], i)))
    elif journey[i] == 3: # 프라하
        if s[i] in Trip.clearW:
            activity.append(Trip.act.get('PragueOut'))
            item.append(Trip.clearW.get(WT.getWeather(wt, journey[i], i)))
        else:
            activity.append(Trip.act.get('PragueIn'))
            item.append(Trip.unclearW.get(WT.getWeather(wt, journey[i], i)))
    elif journey[i] == 4: # 플로렌스
        if s[i] in Trip.clearW:
            activity.append(Trip.act.get('FlorenceOut'))
            item.append(Trip.clearW.get(WT.getWeather(wt, journey[i], i)))
        else:
            activity.append(Trip.act.get('FlorenceIn'))
            item.append(Trip.unclearW.get(WT.getWeather(wt, journey[i], i)))
    elif journey[i] == 5: # 부다페스트
        if s[i] in Trip.clearW:
            activity.append(Trip.act.get('BudapestOut'))
            item.append(Trip.clearW.get(WT.getWeather(wt, journey[i], i)))
        else:
            activity.append(Trip.act.get('BudapestIn'))
            item.append(Trip.unclearW.get(WT.getWeather(wt, journey[i], i)))

# 9. 출력 프로그램 실행
if __name__ == "__main__":  #부모 클래스 (뼈대역할) # 직접 파일 실행시만 if 문 실행, 대화형 인터프리터나 다른 파일에서 실행시 if문 미실행 (p217참고)
    root = tk.Tk()
    root.title('(주)개추엉투어')
    root.geometry('800x580+0+0') # tk창 위치 (0,0)
    Gui(root)
    root.mainloop() # 이벤트 메시지루프 : 다양한 이벤트로부터 오는 메시지를 받고 전달하는 역할