#-*-coding:utf-8-*-
import urllib2, json, time
from flask import Flask, request

app = Flask(__name__)
token = ''

def alert(msg):
    data = {
        'msgtype': 'text',
        'text': {
            'content': msg
        }
    }
    headers = {'Content-Type': 'application/json'}
    req = urllib2.Request('https://oapi.dingtalk.com/robot/send?access_token=' + token, headers=headers, data=json.dumps(data))
    response = urllib2.urlopen(req)

@app.route('/dingding/alert', methods=['POST'])
def execute_async():
    parameter = request.json
    alert("构建镜像成功\n" + json.dumps(parameter, indent=2, sort_keys=True))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)