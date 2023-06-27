from datetime import datetime, timedelta
import random
import requests
import http.client, urllib, json

nowtime = datetime.utcnow() + timedelta(hours=8)
today = datetime.strptime(str(nowtime.date()), "%Y-%m-%d")


def get_time():
    dictDate = {'Monday': '星期一', 'Tuesday': '星期二', 'Wednesday': '星期三', 'Thursday': '星期四',
                'Friday': '星期五', 'Saturday': '星期六', 'Sunday': '星期天'}
    a = dictDate[nowtime.strftime('%A')]
    return nowtime.strftime("%Y年%m月%d日 %H时%M分 ") + a

def get_words():
  conn = http.client.HTTPSConnection('api.tianapi.com')
  params = urllib.parse.urlencode({'key':'ef4370c0fbe5eed37c23c7ba6e48e948','astro':'pisces'})
  headers = {'Content-type':'application/x-www-form-urlencoded'}
  conn.request('POST','/star/index',params,headers)
  res = conn.getresponse()
  data = res.read()
  data = json.loads(data)
  data = str(data["newslist"][8]["content"]) + "\n爱情指数：" + str(data["newslist"][2]["content"]) + "\n"
  return data 

def get_random_color():
    return "#%06x" % random.randint(0, 0xFFFFFF)


def get_weather(city, key):
    url = f"https://api.seniverse.com/v3/weather/daily.json?key={key}&location={city}&language=zh-Hans&unit=c&start=-1&days=5"
    res = requests.get(url).json()
    weather = (res['results'][0])["daily"][0]
    city = (res['results'][0])["location"]["name"]
    return city, weather


def get_count(born_date):
    delta = today - datetime.strptime(born_date, "%Y-%m-%d")
    return delta.days


def get_birthday(birthday):
    nextdate = datetime.strptime(str(today.year) + "-" + birthday, "%Y-%m-%d")
    if nextdate < today:
        nextdate = nextdate.replace(year=nextdate.year + 1)
    return (nextdate - today).days
