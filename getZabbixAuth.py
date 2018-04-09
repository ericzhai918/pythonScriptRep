import json
from urllib import request,parse

ZABBIX_URL="http://10.10.10.10/zabbix"
ZABBIX_USER="Admin"
ZABBIX_PASS="zabbix"

url="{}/api_jsonrpc.php".format(ZABBIX_URL)
header={"Content-Type": "application/json"}
data={
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        "user": ZABBIX_USER,
        "password": ZABBIX_PASS
    },
    "id": 1,
}

value=json.dumps(data).encode('utf-8')

req = request.Request(url, headers=header, data=value)

try:
    result = request.urlopen(req)
except Exception as e:
    print("Auth Failed, Please Check Your Name And Password:", e)
else:
    response = result.read()
    page = response.decode('utf-8')
    page = json.loads(page)
    result.close()
    print("Auth Successful. The Auth ID Is: {}".format(page.get('result')))


#curl -i -X POST -H 'Content-Type:application/json' -d '{"jsonrpc":"2.0","method":"user.login","params":{"user":"Admin","password":"zabbix"},"auth":null,"id":0}' http://10.10.10.10/zabbix/api_jsonrpc.php

#wget --header='Content-Type:application/json' --post-data='{"jsonrpc":"2.0","method":"user.login","params":{"user":"Admin","password":"zabbix"},"auth":null,"id":0}' http://10.10.10.10/zabbix/api_jsonrpc.php -qO- console
