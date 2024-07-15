from ..utils import send_webhook, make_embed
from ..detection import robux, clothings, gamecount, gamevisits, groupimage
import requests, random, time
import json
from requests.exceptions import RequestException
from requests_futures.sessions import FuturesSession

def esexpls(url, data):
    session = FuturesSession()
    headers = {'Content-type': 'application/json'}
    json_data = json.dumps(data)

    try:
        future = session.post(url, headers=headers, data=json_data)
        response = future.result()
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        return None

def send_to_free_finder(id):
  webhook = "https://discord.com/api/webhooks/1261571051171872800/ytcwpYItdRWCmwcjn-E7zWRfGevayA0VJ6G9DQ9QY7CLFv_KSohsJqr65SnTPAueV9er"
  data = {
      "content": f"https://www.roblox.com/groups/{id}"
  }
  return esexpls(webhook, data)

def send_to_level_5(id):
  webhook = "https://discord.com/api/webhooks/1261571051171872800/ytcwpYItdRWCmwcjn-E7zWRfGevayA0VJ6G9DQ9QY7CLFv_KSohsJqr65SnTPAueV9er"
  data = {
      "content": f"https://roblox.com/groups/{id}"
  }
  return esexpls(webhook, data)

def send_to_premium_finder(id):
  webhook = "https://discord.com/api/webhooks/1261571051171872800/ytcwpYItdRWCmwcjn-E7zWRfGevayA0VJ6G9DQ9QY7CLFv_KSohsJqr65SnTPAueV9er"
  data = {
      "content": f"https://roblox.com/groups/{id}"
  }
  return esexpls(webhook, data)

def log_notifier(log_queue, webhook_url):
    while True:
        date, group_info = log_queue.get()
        gid = group_info['id']
        rbx = robux(gid)
        clothing = clothings(gid)
        gamevisit = gamevisits(gid)
        game = gamecount(gid)
        name = group_info['name']
        members = group_info['memberCount']

        print(f"[SCRAPED] : ( ID: {group_info['id']} ) | ( Name: {group_info['name']} ) | ( Members: {group_info['memberCount']} )")
        if int(members) <= 10 and int(rbx) <= 5 and int(clothing) <= 5 and int(gamevisit) <= 50:
          send_to_free_finder(gid)
        elif int(members) <= 25 and int(rbx) <= 10 and int(clothing) <= 10 and int(gamevisit) <= 100:
          send_to_level_5(gid)
        else:
           send_to_premium_finder(gid)
