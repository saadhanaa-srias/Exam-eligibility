a=int(input("enter total number of working days:"))
b=int(input("enter total number of days absent:"))
per=b/a*100
print("this is your percentage rate of absence:",per)
if per< 75:
 print("you are allowed to sit for your exam")
elif per> 100:
  print("please make sure your absence does not exceed attendence")
else:
  print("you are disallowed to sit for your exam")