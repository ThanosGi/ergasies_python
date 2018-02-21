import urllib2
import json
import datetime

cur_date=datetime.datetime.now()


def compare_lists(l1,l2):
  s=0
  for i in l1:
    if i in l2:
      s+=1
  return s

mynums=[]
maxall=[]
countmax=[]
maxday=[]
print "Give 10 numbers with space"
mynums = raw_input()
items = mynums.split()
lst2 = [eval(x) for x in items]
print "Wait.."
for i in range (31):
  cur_date= cur_date - datetime.timedelta(days=1)
  date_str= cur_date.strftime("%d-%m-%Y")
  url='http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json'%date_str
  req= urllib2.Request(url)
  response = urllib2.urlopen(req)
  data = response.read()
  data = json.loads(data)
  klhrwseis= data['draws']['draw']
  r=[]
  for k in klhrwseis:
    tmp=k["results"]
    r.append (compare_lists(lst2,tmp))
  if max(r)>4:
      maxall.append(max(r))
      countmax.append(r.count(max(r)))
      maxday.append(date_str)
pos = []
for i in range(31):
    if maxall[i]==max(maxall):
        pos.append(i)
temp=countmax[0]
for i in pos:
    if countmax[i] > temp :
        temp=countmax[i]
print "Oi imera/imeres me tis perissoteres epitixies einai:"
for i in pos:
    print maxday[i]
