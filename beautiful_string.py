s=input()
x=len(s)-1
if((s[0]=='a' or s[0]=='A') and (s[-1]=='z' or s[-1]=='Z') and (s[int(x/2)]=='m' or s[int(x/2)]=='M')):
  print(1)
else:
  print(0)
