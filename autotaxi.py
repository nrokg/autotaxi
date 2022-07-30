import requests
import vk_api
from random import randint
import time

token = open("token.txt", "r").read()
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()

while 1 == 1:
    try:
        time.sleep(7)
        g = vk.messages.send(peer_id=-166948584, random_id=randint(0,999999999999), message="я")
        str(g).replace("	", "")
        g = int(g) + 1
        time.sleep(5)
        p = vk.messages.getById(message_ids=g)
        p = str(p)
        a = p.rfind("$")
        b = p.rfind(".")
        g = p[a:]
        g = g.replace(".'}]}", '')
        if g != "}":
            print("Баланс: " + g)

        time.sleep(5)
        vk.messages.send(peer_id=-166948584, random_id=randint(0, 999999999999), message="работа", payload="{\"menu\":\"jobs\"}")
        time.sleep(5)
        vk.messages.send(peer_id=-166948584, random_id=randint(0, 999999999999), message="🚖 таксист", payload="{\"jobs.menu\":\"taxi\"}")
        time.sleep(5)
        g = vk.messages.send(peer_id=-166948584, random_id=randint(0, 999999999999), message="отправиться в путь", payload="{\"taxi1\":\"W19jYA==\"}")
        str(g).replace("	", "")
        g = int(g) + 1
        time.sleep(5)
        p =  vk.messages.getById(message_ids=g)
        p = str(p)
        time.sleep(5)
        if p.find("TAX4") != -1:
            g = vk.messages.send(peer_id=-166948584, random_id=randint(0, 999999999999), message="🔼", payload="{\"taxi.begin1\":1,\"if\":1,\"city\":3}")
            str(g).replace("	", "")
            g = int(g) + 1
            time.sleep(5)
            p = vk.messages.getById(message_ids=g)
            p = str(p)
            if p.find("35 сек") != -1:
                print("В пути. Ждём 35 сек")
                time.sleep(38)
            elif p.find("з 18 сек") != -1:
                print("В пути. Ждём 20 секунд")
                time.sleep(21)
            else:
                print("В пути. Ждём 52 секунды")
                time.sleep(55)
            vk.messages.send(peer_id=-166948584, random_id=randint(0, 999999999999), message="обновить время", payload="{\"taxi.road\":\"upd\"}")
        elif p.find("TAX8") != -1:
            g = vk.messages.send(peer_id=-166948584, random_id=randint(0, 999999999999), message="🔼", payload="{\"taxi.begin1\":2,\"if\":1,\"city\":3}")
            str(g).replace("	", "")
            g = int(g) + 1
            time.sleep(5)
            p = vk.messages.getById(message_ids=g)
            p = str(p)
            if p.find("35 сек") != -1:
                print("В пути. Ждём 35 сек")
                time.sleep(38)
            elif p.find("з 18 сек") != -1:
                print("В пути. Ждём 20 секунд")
                time.sleep(21)
            else:
                print("В пути. Ждём 52 секунды")
                time.sleep(55)
            vk.messages.send(peer_id=-166948584, random_id=randint(0, 999999999999), message="обновить время", payload="{\"taxi.road\":\"upd\"}")

        elif p.find("TAX5") != -1:
            g = vk.messages.send(peer_id=-166948584, random_id=randint(0, 999999999999), message="🔼", payload="{\"taxi.begin1\":3,\"if\":1,\"city\":3}")
            str(g).replace("	", "")
            g = int(g) + 1
            time.sleep(5)
            p = vk.messages.getById(message_ids=g)
            p = str(p)
            if p.find("35 сек") != -1:
                print("В пути. Ждём 35 сек")
                time.sleep(38)
            elif p.find("з 18 сек") != -1:
                print("В пути. Ждём 20 секунд")
                time.sleep(21)
            else:
                print("В пути. Ждём 52 секунды")
                time.sleep(55)
            vk.messages.send(peer_id=-166948584, random_id=randint(0, 999999999999), message="обновить время", payload="{\"taxi.road\":\"upd\"}")
    except requests.exceptions.ConnectionError:
        print("интернет атключили")
        time.sleep(5)
    except requests.exceptions.ReadTimeout:
        print("интернет атключили")
        time.sleep(5)
    except vk_api.exceptions.Captcha:
        print("НУЖНА КАПЧА! Ждем 30 сек.")
        time.sleep(30)
    except vk_api.exceptions.ApiError:
        time.sleep(5)