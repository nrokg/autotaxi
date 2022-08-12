import requests
from random import randint
import time

###################################################
token = ""
###################################################

while 1 == 1:
    try:
        time.sleep(7)
        g = requests.get("https://api.vk.com/method/messages.send?access_token=" + token + "&peer_id=-166948584&random_id=" + str(randint(0,999999999999)) + "&message=я&v=5.131")
        g = g.text
        g = g.replace("{", "")
        g = g.replace('response":', "")
        g = g.replace("}", "")
        g = g.replace('"', "")
        g = int(g) + 1
        time.sleep(5)
        p = requests.get("https://api.vk.com/method/messages.getById?access_token=" + token + "&message_ids=" + str(g) + "&v=5.131")
        p = p.text
        a = p.rfind("$")
        b = p.rfind(".")
        g = p[a:]
        g = g.replace(".'}]}", '')
        if g != "}":
            g = g.replace('."}]}}', "")
            print("Баланс: " + g)

        time.sleep(5)
        requests.get("https://api.vk.com/method/messages.send?access_token=" + token + "&peer_id=-166948584&random_id=" + str(randint(0,99999999999)) + '&message=работа&payload={\"menu\":\"jobs\"}&v=5.131')
        time.sleep(5)
        requests.get("https://api.vk.com/method/messages.send?access_token=" + token + "&peer_id=-166948584&random_id=" + str(randint(0,99999999999)) + '&message=🚖 таксист&payload={\"jobs.menu\":\"taxi\"}&v=5.131')
        time.sleep(5)
        g = requests.get("https://api.vk.com/method/messages.send?access_token=" + token + "&peer_id=-166948584&random_id=" + str(randint(0,99999999999)) + '&message=отправиться в путь&payload={\"taxi1\":\"W19jYA==\"}&v=5.131')
        g = g.text
        g = g.replace("{", "")
        g = g.replace('response":', "")
        g = g.replace("}", "")
        g = g.replace('"', "")
        g = int(g) + 1
        time.sleep(5)
        p = requests.get("https://api.vk.com/method/messages.getById?access_token=" + token + "&message_ids=" + str(g) + "&v=5.131")
        p = p.text
        time.sleep(5)
        if p.find("TAX4") != -1:
            g = requests.get("https://api.vk.com/method/messages.send?access_token=" + token + "&peer_id=-166948584&random_id=" + str(randint(0,99999999999)) + '&message=🔼&payload={\"taxi.begin1\":1,\"if\":1,\"city\":3}&v=5.131')
            g = g.text
            g = g.replace("{", "")
            g = g.replace('response":', "")
            g = g.replace("}", "")
            g = g.replace('"', "")
            g = int(g) + 1
            time.sleep(5)
            p = requests.get("https://api.vk.com/method/messages.getById/?access_token=" + token + "&message_ids=" + str(g) + "&v=5.131")
            p = p.text
            if p.find("35 сек") != -1:
                print("В пути. Ждём 35 сек")
                time.sleep(38)
            elif p.find("з 18 сек") != -1:
                print("В пути. Ждём 20 секунд")
                time.sleep(21)
            else:
                print("В пути. Ждём 52 секунды")
                time.sleep(55)
            requests.get("https://api.vk.com/method/messages.send?access_token=" + token + "&peer_id=-166948584&random_id=" + str(randint(0,99999999999)) + '&message=обновить время&payload={\"taxi.road\":\"upd\"}&v=5.131')


        elif p.find("TAX8") != -1:
            g = requests.get("https://api.vk.com/method/messages.send?access_token=" + token + "&peer_id=-166948584&random_id=" + str(randint(0,99999999999)) + '&message=🔼&payload={\"taxi.begin1\":1,\"if\":1,\"city\":3}&v=5.131')
            g = g.text
            g = g.replace("{", "")
            g = g.replace('response":', "")
            g = g.replace("}", "")
            g = g.replace('"', "")
            g = int(g) + 1
            time.sleep(5)
            p = requests.get("https://api.vk.com/method/messages.getById/?access_token=" + token + "&message_ids=" + str(g) + "&v=5.131")
            p = p.text
            if p.find("35 сек") != -1:
                print("В пути. Ждём 35 сек")
                time.sleep(38)
            elif p.find("з 18 сек") != -1:
                print("В пути. Ждём 20 секунд")
                time.sleep(21)
            else:
                print("В пути. Ждём 52 секунды")
                time.sleep(55)
            requests.get("https://api.vk.com/method/messages.send?access_token=" + token + "&peer_id=-166948584&random_id=" + str(randint(0,99999999999)) + '&message=обновить время&payload={\"taxi.road\":\"upd\"}&v=5.131')

        elif p.find("TAX5") != -1:
            g = requests.get("https://api.vk.com/method/messages.send?access_token=" + token + "&peer_id=-166948584&random_id=" + str(randint(0,99999999999)) + '&message=🔼&payload={\"taxi.begin1\":1,\"if\":1,\"city\":3}&v=5.131')
            g = g.text
            g = g.replace("{", "")
            g = g.replace('response":', "")
            g = g.replace("}", "")
            g = g.replace('"', "")
            g = int(g) + 1
            time.sleep(5)
            p = requests.get("https://api.vk.com/method/messages.getById/?access_token=" + token + "&message_ids=" + str(g) + "&v=5.131")
            p = p.text
            if p.find("35 сек") != -1:
                print("В пути. Ждём 35 сек")
                time.sleep(38)
            elif p.find("з 18 сек") != -1:
                print("В пути. Ждём 20 секунд")
                time.sleep(21)
            else:
                print("В пути. Ждём 52 секунды")
                time.sleep(55)
            requests.get("https://api.vk.com/method/messages.send?access_token=" + token + "&peer_id=-166948584&random_id=" + str(randint(0,99999999999)) + '&message=обновить время&payload={\"taxi.road\":\"upd\"}&v=5.131')
    except requests.exceptions.ConnectionError:
        print("интернет отключили")
        time.sleep(5)
    except requests.exceptions.ReadTimeout:
        print("интернет отключили")
        time.sleep(5)
