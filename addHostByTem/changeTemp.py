from template import tem

with open('nameList') as name:
    names=[]
    for line in name:
        line=line.strip()
        if not line:
            continue
        names.append(line)

with open('ipList') as ip:
    ips=[]
    for line in ip:
        line=line.strip()
        if not line:
            continue
        ips.append(line) 

for ip in ips:
    if ip.startswith("10.2"):
        proxy="10.20.28.10"
    if ip.startswith("10.1"):
        proxy="10.10.32.18"
    name=""
    for _name in names:
        if ip in _name:
            name=_name
    print(tem.format(proxy=proxy,ip=ip,name=name))
   
