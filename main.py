import requests # requests 라이브러리 설치 필요
from bs4 import BeautifulSoup
from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')
# 파싱 : 원하는 값을 가공해서 가져오는 것. 스크래핑을 파싱한다 라고도 함.

#############################
# (입맛에 맞게 코딩)
#############################

for item in soup.select('table > tbody > tr') :
    rank = item.select_one('.ac > img')
    if rank : 
        rank = rank['alt']
        # print(item.select_one('.ac > img')['alt']) 
        # 파이썬에서 어트리뷰트 가져올때 [] 활용.
        title = item.select_one('.title > .tit5 > a').text
        # print(title.text)
        point = item.select_one('.point').text
        # print(point.text)
        db.movies.insert_one({
            'rank':rank, 
            'title':title, 
            'point':point
        })
        print(rank, title, point)

# titles = soup.select('table > tbody > tr')

# for title in titles :
#     print(title.text)


# r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
# rjson = r.json()

# gus = rjson['RealtimeCityAir']['row']

# for gu in gus :
#     if gu['IDEX_MVL'] < 100:
#         print (gu['MSRSTE_NM'], gu['IDEX_MVL'])