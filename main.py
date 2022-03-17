import os
t1=int(input("几小时？没有请输入0："))
t2=int(input("几分钟？没有请输入0："))
t3=int(input("几秒?没有请输入0："))
y=str(t1*60*60+t2*60+t3)
os.system("shutdown /s /t "+y)
print(y,"秒后关机")
input("按回车取消")
os.system("shutdown -a")