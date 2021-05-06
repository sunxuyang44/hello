import time
import datetime
import sys
print('输入指定日期即可穿越(只能到未来)'"\n"'请输入今天星期几：')
wed=int(input('nummber'))

print('输入指定日期即可穿越(只能到未来)'"\n"'请输入目标年月日：')
y=int(input('年'))
m=int(input('月'))
d=int(input('日'))
sj=str(y)+' '+str(m)+' '+str(d)
d1=datetime.datetime(y,m,d)
print('启动中，还需要')
while True:
   d2=datetime.datetime.now()
   sec=round((d1-d2).total_seconds())
   op=[int(sec/86400),'天',int((sec-int(sec/86400)*86400)/3600),'小时',int((sec-int(sec/3600)*3600)/60),'分',int((sec-int(sec/60)*60)),'秒']
   

   nn=(''.join('%s' %id for id in op))
   sys.stdout.write("\r%s"%nn)
   sys.stdout.write('即可启动')
   sys.stdout.flush()
   time.sleep(1)
   if int(sec/86400)%7==1:
     out=wed+1
    
   if int(sec/86400)%7==2:
     out=wed+1
    
   if int(sec/86400)%7==3:
     out=wed+1
    
   if int(sec/86400)%7==4:
     out=wed+1
    
   if int(sec/86400)%7==5:
     out=wed+1
    
   if int(sec/86400)%7==6:
     out=wed+1
    
   if int(sec/86400)%7==0:
     out=wed+1
    
   if out==1:
      print('周一') 
   if out==2:
      print('周二') 
   if out==3:
      print('周三') 
   if out==4:
      print('周四') 
   if out==5:
      print('周五') 
   if out==6:
      print('周六') 
   if out==7:
      print('周日') 
   if out==8:
      print('周一') 
   if out==9:
      print('周二') 
   if out==10:
      print('周三') 
   if out==11:
      print('周四') 
   if out==12:
      print('周五') 
   if out==13:
      print('周六') 
   if out==14:
      print('周日') 
   break
