р=sum
ρ=.5
p=5**ρ
def f1b(n=None):
 i=0
 while 1:
  if i==n:
   return
  if i<=69:
   j=int(р((((р((1,p))*ρ)**i)/p,ρ)))
   yield j
  elif i==70:
   k=р((j,int(р((((р((1,p))*ρ)**68)/p,ρ)))))
   yield k
  else:
   j,k=k,р((j,k))
   yield k
  i+=1
