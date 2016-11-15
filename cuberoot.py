n=input('Enter the number')
epsilon=0.0000000002
x =0.0
y = max(1.0,n)
p = (x+y)/ 2.0
while (abs(p**3 -n)>= epsilon):
    if (p*p*p <= n):
        x= p
    else:
        y= p
    p = (x+y)/2.0
    print p

print 'Cube root = ', p
