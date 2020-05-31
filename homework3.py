import requests # requests 라이브러리 설치 필요
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

soup = BeautifulSoup(data.text,'html.parser')

songs = soup.select('table > tbody > tr')

for song in songs :
    rank = song.select_one('.number')
    title = song.select_one('.check > .select-check')
    artist = song.select_one('.info > .artist.ellipsis')
    # song_title = song.select_one('.info > .title ellipsis').text.strip()
    # artist = song.select_one('.info > .artist ellipsis').text.strip()
    if song : 
        rank = rank.text.split("\n")[0]
        title = title['title']
        artist = artist.text
        print(rank, title, artist)
    