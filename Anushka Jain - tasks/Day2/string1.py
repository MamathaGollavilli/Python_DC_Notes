s1 = "anushka"
s2 = "jain"
length = min(len(s1), len(s2))
for i in range (0,length):
    print(s1[i]+s2[i],end="")
if(len(s1) > length):
   a = s1[length:]
   print(a)
if(len(s2) > length):
   a = s2[length:]
   print(a)
