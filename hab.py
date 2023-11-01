import random as mia
li = [0,1,2,3,4,5,6,7,8,9]
mia.shuffle(li)
lim = str(li)
lis = lim.replace(',','').replace('[','').replace(' ','').replace(']','')
a = lis[:4]
count = 0
m = 0

while m == 0:
  b = input(">>>")
  count += 1
  if len(b) == 4:
    n1,n2,n3,n4 = b[0],b[1],b[2],b[3]
    if n1!=n2 and n2!=n3 and n3!=n4 and n1!=n4 and n1!=n3 and n2!=n4:
      if a == b:
        print("おめでとう！",str(count)+'回目でクリア！')
        break
      else:
        r1,r2,r3,r4 = a[0],a[1],a[2],a[3]
        hit = [n1==r1,n2==r2,n3==r3,n4==r4].count(True)
        blow = [n1 in r2+r3+r4,n2 in r1+r3+r4,n3 in r1+r2+r4,n4 in r1+r2+r3].count(True)
        print("hit:",hit,"blow:",blow)
    else:
      print("異なる4桁を入れてください。")
  else:
     print("4文字で入れてください。")




