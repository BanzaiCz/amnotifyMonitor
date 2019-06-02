""" MADE BY Syre#9999 & samueI#0001 """


import requests
import json
import time
import datetime


delay = 0.01
datetime.datetime.now().time()
datetime.time(15, 8, 24, 78915)


stockEndpoint = "https://amnotify.com/api/stock/available"
webhook_url = 'https://discordapp.com/api/webhooks/XXXXXXXXXXXXXXXXXX/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

in_stock = {
    "username": "AMNotify Monitor",
    "avatar_url": "https://i.imgur.com/ELyJcw2.png",
    "embeds": [{
        "color": 16721733,
        "description": "Monthly memberships just restocked.",
        "author": {
            "name": "AMNotify",
            "url": "https://amnotify.com/",
            "icon_url": "https://i.imgur.com/ELyJcw2.png"
         },
        "fields": [
            {
                "name": "Links",
                "value": "[Purchase](https://amnotify.com/purchase) | [Twitter](https://twitter.com/AMNotify)"
            },
            {
                "name": "Status",
                "value": "In Stock"
            }
        ],
        "footer": {
            "text": "Monitor by Syre#9999 & samueI#0001"
        }
    }]
}

running = {
    "username": "AMNotify Monitor",
    "avatar_url": "https://i.imgur.com/ELyJcw2.png",
    "embeds": [{
        "color": 16721733,
        "description": "Monitor is now up and running.",
        "author": {
            "name": "AMNotify",
            "url": "https://amnotify.com/",
            "icon_url": "https://i.imgur.com/ELyJcw2.png"
         },
    }]
}


print("           __  __ _   _       _   _  __       ")
print("     /\   |  \/  | \ | |     | | (_)/ _|      ")
print("    /  \  | \  / |  \| | ___ | |_ _| |_ _   _ ")
print("   / /\ \ | |\/| | . ` |/ _ \| __| |  _| | | |")
print("  / ____ \| |  | | |\  | (_) | |_| | | | |_| |")
print(" /_/    \_\_|  |_|_| \_|\___/ \__|_|_|  \__, |")
print("                                         __/ |")
print("                                        |___/ ")
print("")
print("AMNotify Monitor by Syre#9999 & samueI#0001")
time.sleep(2)
print("")

response = requests.post(
webhook_url, data=json.dumps(running),
headers={'Content-Type': 'application/json'})


def waitForStock():
    s = requests.session()
    notLoaded = True
    while notLoaded:
        try:
            response = json.loads(s.get(stockEndpoint, headers=headers).text)
        except Exception as e:
            print("[", datetime.datetime.now().time(), "] Weird error, cuz AMN is doodoo." + str(e))

        if response['available']:
            response = requests.post(
            webhook_url, data=json.dumps(in_stock),
            headers={'Content-Type': 'application/json'})
            notLoaded = False
        else:
            print("[", datetime.datetime.now().time(), "] AMNotify is currently sold out.")
            time.sleep(delay)

            
waitForStock()