p=5**.5
def f1b(n=None):
 i=0
 while 1:
  if i==n:
   return
  if i<=69:
   j=int(sum((((sum((1,p))/2)**i)/p,.5)))
   yield j
  elif i==70:
   k=sum((j,int(sum((((sum((1,p))/2)**68)/p,.5)))))
   yield k
  else:
   j,k=k,sum((j,k))
   yield k
  i+=1
