a=int(input())
a1=a//100
a2=(a-a1*100)//10
a3=a-a1*100-a2*10
print(a3,a2,a1,sep='')
