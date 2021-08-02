import json
import requests

# https://work.weixin.qq.com/wework_admin/frame#profile
corp_id = 'wwxxxxxxxxxxxxxxxxx'
corp_secret = 'Ghxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
agent_id = '10xxxxxx'

def get_access_token(corp_id, corp_secret):
    resp = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={corp_secret}')
    js = json.loads(resp.text)
    print(js)
    if js["errcode"] == 0:
        access_token = js["access_token"]
        expires_in = js["expires_in"]
        return access_token, expires_in

def wechat_push_text(agent_id, access_token, message):
    data = {
        "touser": "@all",
        "msgtype": 'text',
        "agentid": agent_id,
        "text": {
            "content": message
        },
        "safe": 0,
        "enable_id_trans": 0,
        "enable_duplicate_check": 0,
        "duplicate_check_interval": 1800
    }
    resp = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}', json=data)
    js = json.loads(resp.text)
    print(js)
    if js["errcode"] == 0:
        return js

access_token, expires_in = get_access_token(corp_id, corp_secret)
wechat_push_text(agent_id=agent_id, access_token=access_token, message='wechat notify\ntest')
