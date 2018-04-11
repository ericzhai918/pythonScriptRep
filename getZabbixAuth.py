import json
from urllib import request,parse

ZABBIX_URL="http://10.11.12.192/zabbix"
ZABBIX_USER="Admin"
ZABBIX_PASS="zabbix"

url="{}/api_jsonrpc.php".format(ZABBIX_URL)
header={"Content-Type": "application/json"}

def userLogin():    
    data={
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
            "user": ZABBIX_USER,
            "password": ZABBIX_PASS
        },
        "id": 0,
    }

    value=json.dumps(data).encode('utf-8')

    req = request.Request(url, headers=header, data=value)

    try:
        result = request.urlopen(req)
    except Exception as e:
        print("Auth Failed, Please Check Your Name And Password:", e)
    else:
        response = json.loads(result.read().decode('utf-8'))
        result.close()
        authID=response['result']
        return authID

def getHosts(authID):
    data={
        "jsonrpc": "2.0",
        "method": "host.get",
        "params": {
            "output": [
                "hostid",
                "host"
            ],
            "selectInterfaces": [
                "interfaceid",
                "ip"
            ]
        },

        "id": 2,
        "auth": authID
    }    
    value=json.dumps(data).encode('utf-8')
    req = request.Request(url, headers=header, data=value)
    try:
        result = request.urlopen(req)
    except Exception as e:
        print("Auth Failed, Please Check Your Name And Password:", e)
    else:
        response = json.loads(result.read().decode('utf-8'))
        result.close()
        host=response['result']
        return host
'''
def getProc(data):
    dict = {}
    list = data
    for i in list:
        host = i['host']
        inter = i['interfaces']
        for j in inter:
           ip = j['ip']
           dict[host] = ip
    return dict

#排序ip列表
def getData(dict):
    data = dict
    ip_list = [ ]
    for key in data.keys():
        
        ip =  data[key]
        ip_list.append(ip)
    ip_list = list(set(ip_list))
    ip_list.sort()
    return ip_list 
#整理输出ip

def getGroup(ip_list):
    ip_group = { }
    ips = ip_list
    for i in ips:
         print(i)
'''

hosts=getHosts(userLogin())

print("hostid  host")
for i in hosts:
        print(i['hostid'],'|',i['host'])

#curl -i -X POST -H 'Content-Type:application/json' -d '{"jsonrpc":"2.0","method":"user.login","params":{"user":"Admin","password":"zabbix"},"auth":null,"id":0}' http://10.10.10.10/zabbix/api_jsonrpc.php

#wget --header='Content-Type:application/json' --post-data='{"jsonrpc":"2.0","method":"user.login","params":{"user":"Admin","password":"zabbix"},"auth":null,"id":0}' http://10.10.10.10/zabbix/api_jsonrpc.php -qO- console
