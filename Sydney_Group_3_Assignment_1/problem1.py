#Group: Sydney_Group_3
#Ayan Roy - S388800
#Pronab Sarker - S388867
#Ahmed Zabir Hussain - S387391
#Shashika Mihiranga Puwakdandawe Gam Acharige - S385832



mylist = []
for i in range(1,4):
  print(f'User input {i}:')
  x = input()
  mylist.append(x)

mylist.sort()

if int(mylist[0]) + int(mylist[1]) > int(mylist[2]):
  print('Yes, these three lengths can form a triangle.')
else:
  print('NO, these three lengths CANNOT form a triangle.')


