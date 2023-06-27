from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage
import os
import json
from function import *


if __name__ == '__main__':
    app_id = os.getenv("APP_ID")
    app_secret = os.getenv("APP_SECRET")
    template_id = os.getenv("TEMPLATE_ID")
    weather_key = "SuPZBMGRxx-M1uA66"

    client = WeChatClient(app_id, app_secret)
    wm = WeChatMessage(client)

    f = open("./users_info.json", encoding="utf-8")
    js_text = json.load(f)
    f.close()
    data = js_text['data']
    num = 0
    words=get_words()
    for user_info in data:
        born_date1 = user_info['born_date1']
        birthday1 = born_date1[5:]
        born_date2 = user_info['born_date2']
        birthday2 = born_date2[5:]
        city = user_info['city']
        user_id = user_info['user_id']
        start_date = user_info['start_date']
        name1 = user_info['user_name_1'].upper()
        name2 = user_info['user_name_2'].upper()


        wea_city,weather = get_weather(city,weather_key)
        data = dict()
        data['time'] = {
            'value': get_time(),
            'color': '#470024'
        }
        data['words'] = {
            'value': words,
            'color': get_random_color()
        }
        data['weather'] = {
            'value': weather['text_day'],
            'color': '#002fa4'
        }
        data['city'] = {
            'value': wea_city,
            'color': get_random_color()
        }
        data['tem_high'] = {
            'value': weather['high'],
            'color': '#D44848'
        }
        data['tem_low'] = {
            'value': weather['low'],
            'color': '#01847F'
        }
        data['born_days'] = {
            'value': get_count(born_date1),
            'color': get_random_color()
        }
        data['birthday_left1'] = {
            'value': get_birthday(birthday1),
            'color': get_random_color()
        }
        data['birthday_left2'] = {
            'value': get_birthday(birthday2),
            'color': get_random_color()
        }
        data['start_date'] = {
            'value': get_count(start_date),
            'color': get_random_color()
        }
        data['wind'] = {
            'value': weather['wind_direction'],
            'color': get_random_color()
        }
        data['name1'] = {
            'value': name1,
            'color': get_random_color()
        }
        data['name2'] = {
            'value': name2,
            'color': get_random_color()
        }
        print(data)
        res = wm.send_template(user_id, template_id, data)
        print(res)
        num += 1
    print(f"成功发送{num}条信息")
