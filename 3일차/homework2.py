import requests
from bs4 import BeautifulSoup
import string

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

#music = soup.select("#body-content > div.newest-list > div > table > tbody > tr > a")
# input_list = soup.select("#body-content > div.newest-list > div > table > tbody > tr > td > input")
# for title in input_list:
#     print(title['title'])
    #body-content > div.newest-list > div > table > tbody > tr:nth-child(2) > td.number
 
input_list = soup.select("#body-content > div.newest-list > div > table > tbody > tr")
for title in input_list:
    rank = title.select_one('td.number').text.split()
    song_title = title.select_one('td.info > a.title.ellipsis').text
    artist = title.select_one('td.info > a.artist.ellipsis').text
    # print(rank[0], song_title[0], artist[0-1])
    print(rank[0], song_title.strip(), artist)


