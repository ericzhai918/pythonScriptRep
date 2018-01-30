from dateutil.parser import parse

a1=input("请输入开始日期:")
a2=input("请输入结束日期:")
#a1='201801041800'
#a2='201801052200'
start=parse(a1)
end=parse(a2)
myTime = end - start
oneDay=8*60*60
print("加班天数为:",myTime.total_seconds()/oneDay,"天")
